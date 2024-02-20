import pandas as pd
from polls.models import ODS_Player,ODS_CLUBS,D_AgeGRP,D_Date,D_Federation,D_Departement,D_Sex,D_Type,D_City

def run():
    """ Remplis les tables DWH """
    try:
        # Table de dimension
        # colonnes_Sex()
        # colonnes_AgeGRP()
        # colonnes_Type()
        # colonnes_Date()
        # colonnes_Departement()
        # colonnes_Federation()
    except KeyError as e:
        print(e)



def colonnes_AgeGRP():
    """ """
    # Récupérer les noms de toutes les colonnes de l'ODS
    colonnes = ODS_Player._meta.fields
    l = set()
    D_AgeGRP.objects.all().delete()

    # Parcourir chaque colonne et afficher son nom
    for colonne in colonnes:
        if colonne.name.startswith('F_') or colonne.name.startswith('H_'):
            if 'NR' in colonne.name:
                continue
            age_grp =  "_".join(colonne.name.split("_")[1:3])
            l.add(age_grp)
        else:
            continue
    u = [D_AgeGRP(label=age_group) for age_group in l]
    D_AgeGRP.objects.bulk_create(u)
    print("AgeGRP : OK")

def colonnes_Sex():
    """ """
    D_Sex.objects.all().delete()
    
    l = [D_Sex(code='F'), D_Sex(code='H')]
    D_Sex.objects.bulk_create(l)
    print("Sex : OK")

def colonnes_Federation():
    """ """
    queryset1 = ODS_Player.objects.values('code', 'federation').distinct()
    queryset2 = ODS_CLUBS.objects.values('code', 'federation').distinct()
    queryset = queryset1.union(queryset2, all=False)
    D_Federation.objects.all().delete()
    l = []
    for item in queryset:
        obj = D_Federation(code = int(item['code']), label = item['federation'])
        l.append(obj)
    D_Federation.objects.bulk_create(l)
    print("Fed : OK")


def colonnes_Date():
    """ """
    D_Date.objects.all().delete()

    D_Date.objects.get_or_create(date="2021-01-01")

def colonnes_Departement():
    """ """
    queryset1 = ODS_Player.objects.values('code_commune', 'code_QPV', 'departement', 'commune', 'nom_QPV', 'region', 'statut_geo').distinct()
    queryset2 = ODS_CLUBS.objects.values('code_commune', 'code_QPV', 'departement', 'commune', 'nom_QPV', 'region', 'statut_geo').distinct()
    queryset = queryset1.union(queryset2, all=False)
    l = []
    existing_pks = set()
    D_Departement.objects.all().delete()
    try :
        for item in queryset:
            pk_depart = "_".join([item['code_commune'], item['code_QPV']])

            if pk_depart in existing_pks:
                continue  
            existing_pks.add(pk_depart)

            obj = D_Departement(
                code_Commune = item['code_commune'],
                code_QPV = item['code_QPV'],
                code_Departement = item['departement'],
                label_Commune = item['commune'],
                label_QPV = item['nom_QPV'],
                label_Departement = "",
                label_Region = item['region'],
                statut = item['statut_geo'],
                pk_depart = pk_depart
                )
            l.append(obj)
        D_Departement.objects.bulk_create(l)
        
        print("Depart : OK")
    except KeyError as e:
        print(e)
    

def colonnes_Type():
    """ """
    D_Type.objects.all().delete()

    l = [D_Type(label='clubs'), D_Type(label='EPA')]
    D_Type.objects.bulk_create(l)