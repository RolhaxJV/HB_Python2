import pandas as pd
from polls.models import ODS_Player
from project.settings import DATA_DIR

def run():
    """ Remplis la table ods_Player
    """
    try:
        # Lire CSV
        df = pd.read_csv(f"{DATA_DIR}/lic-data-2021.csv", delimiter=';')

        # Truncate
        ODS_Player.objects.all().delete()

        objs = []
        for index, row in df.iterrows():
            obj = ODS_Player(
                code_commune = row["Code Commune"],
                commune = row["Commune"],
                code_QPV = row["Code QPV"],
                nom_QPV = row["Nom QPV"],
                departement = row["Département"],
                region = row["Région"],
                statut_geo = row["Statut géo"],
                code = row["Code"],
                federation = row["Fédération"],
                F_1_4_ans = row["F - 1 à 4 ans"],
                F_5_9_ans = row["F - 5 à 9 ans"],
                F_10_14_ans = row["F - 10 à 14 ans"],
                F_15_19_ans = row["F - 15 à 19 ans"],
                F_20_24_ans = row["F - 20 à 24 ans"],
                F_25_29_ans = row["F - 25 à 29 ans"],
                F_30_34_ans = row["F - 30 à 34 ans"],
                F_35_39_ans = row["F - 35 à 39 ans"],
                F_40_44_ans = row["F - 40 à 44 ans"],
                F_45_49_ans = row["F - 45 à 49 ans"],
                F_50_54_ans = row["F - 50 à 54 ans"],
                F_55_59_ans = row["F - 55 à 59 ans"],
                F_60_64_ans = row["F - 60 à 64 ans"],
                F_65_69_ans = row["F - 65 à 69 ans"],
                F_70_74_ans = row["F - 70 à 74 ans"],
                F_75_79_ans = row["F - 75 à 79 ans"],
                F_80_99_ans = row["F - 80 à 99 ans"],
                F_NR = row["F - NR"],
                H_1_4_ans = row["H - 1 à 4 ans"],
                H_5_9_ans = row["H - 5 à 9 ans"],
                H_10_14_ans = row["H - 10 à 14 ans"],
                H_15_19_ans = row["H - 15 à 19 ans"],
                H_20_24_ans = row["H - 20 à 24 ans"],
                H_25_29_ans = row["H - 25 à 29 ans"],
                H_30_34_ans = row["H - 30 à 34 ans"],
                H_35_39_ans = row["H - 35 à 39 ans"],
                H_40_44_ans = row["H - 40 à 44 ans"],
                H_45_49_ans = row["H - 45 à 49 ans"],
                H_50_54_ans = row["H - 50 à 54 ans"],
                H_55_59_ans = row["H - 55 à 59 ans"],
                H_60_64_ans = row["H - 60 à 64 ans"],
                H_65_69_ans = row["H - 65 à 69 ans"],
                H_70_74_ans = row["H - 70 à 74 ans"],
                H_75_79_ans = row["H - 75 à 79 ans"],
                H_80_99_ans = row["H - 80 à 99 ans"],
                H_NR = row["H - NR"],
                NR_NR = row["NR - NR"],
                Total = row["Total"],
            )
            objs.append(obj)
            if index == 100000:
                break

        # Bulk create des objets
        ODS_Player.objects.bulk_create(objs)
    except KeyError as e:
        print(e)
