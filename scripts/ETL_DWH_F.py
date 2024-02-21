import pandas as pd
from polls.models import ODS_Player,ODS_CLUBS,D_AgeGRP,D_Date,D_Federation,D_Departement,D_Sex,D_Type,F_Licence,F_Club

def run():
    """ Remplis les tables DWH """
    try:
        # Table de dimension
        sex_cache = {sex.code: sex for sex in D_Sex.objects.all()}
        age_grp_cache = {age_grp.label: age_grp for age_grp in D_AgeGRP.objects.all()}
        type_cache = {type.label: type for type in D_Type.objects.all()}
        date = D_Date.objects.get(date = "2021-01-01")
        departement_cache = {departement.pk_depart: departement for departement in D_Departement.objects.all()}
        federation_cache = {federation.code: federation for federation in D_Federation.objects.all()}

        # Table de Fait Licence
        print("Licence")

        F_Licence.objects.all().delete()
        df = pd.DataFrame(list(ODS_Player.objects.all().values().filter(region="Auvergne-Rhône-Alpes")))
        id_vars = ['code_commune', 'commune', 'code_QPV', 'nom_QPV', 'departement', 'region', 'statut_geo', 'code', 'federation']
        value_vars = [col for col in df.columns if col.startswith('F_') or col.startswith('H_')]
        melted_df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='age_group', value_name='nombre').query('age_group.str.contains("NR") != True and nombre != "0"')

        licences = []
        for index, row in melted_df.iterrows():

            nombre = row['nombre']
            sex_code = 'F' if row['age_group'].startswith('F_') else 'H'

            sex = next((value for value in sex_cache.values() if value.code == sex_code), None)

            federation = next((value for value in federation_cache.values() if value.code == int(row['code'])), None)

            age_grp = next((value for value in age_grp_cache.values() if value.label == "_".join(row['age_group'].split("_")[1:3])), None)

            geo = next((value for value in departement_cache.values() if value.pk_depart == "_".join([row['code_commune'], row['code_QPV']])), None)

            licence = F_Licence(
                nomber = nombre,
                Sex = sex,
                Federation = federation,
                Age_grp = age_grp,
                Date = date,
                Geo = geo,
                pk_L="_".join([str(federation.code), str(sex.code), str(age_grp.label), str(date.date), str(geo.pk_depart)])
            )
            licences.append(licence)

            if len(licences) % 1000 == 0 :
                print("Insert")
                F_Licence.objects.bulk_create(licences)
                licences.clear()
        F_Licence.objects.bulk_create(licences)
        licences.clear()
        
        # Tables de Fait Club
        print("Clubs")

        F_Club.objects.all().delete()
        df = pd.DataFrame(list(ODS_CLUBS.objects.all().values().filter(region="Auvergne-Rhône-Alpes")))
        id_vars = ['code_commune', 'commune', 'code_QPV', 'nom_QPV', 'departement', 'region', 'statut_geo', 'code', 'federation']
        value_vars = ['clubs', 'EPA']
        melted_df = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name='Type', value_name='nombre').query('code_commune.str.contains("NR - Non réparti") != True and nombre != "0"')

        clubs = []
        for index, row in melted_df.iterrows():
            date = D_Date.objects.get(date = "2021-01-01")

            federation = next((value for value in federation_cache.values() if value.code == int(row['code'])), None)

            geo = next((value for value in departement_cache.values() if value.pk_depart == "_".join([row['code_commune'], row['code_QPV']])), None)

            nombre = row['nombre']
            typ = next((value for value in type_cache.values() if value.label == row['Type']), None)

            club = F_Club(
                nomber = nombre,

                Type = typ,
                Federation = federation,
                Date = date,
                Geo = geo,
                pk_F = "_".join([str(federation.code), str(typ.label), str(date.date), str(geo.pk_depart)])
            )

            clubs.append(club)
            if len(clubs) % 1000 == 0 :
                print("Insert")
                F_Club.objects.bulk_create(clubs)
                clubs.clear()

        F_Club.objects.bulk_create(clubs)
        clubs.clear()
    except KeyError as e:
        print(e)
