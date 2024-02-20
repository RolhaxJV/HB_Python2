from django.db import models

# region ODS
class ODS_CLUBS(models.Model):
    """ Class d'objets ODS Clubs """

    code_commune = models.CharField(max_length = 100, default='0')
    commune = models.CharField(max_length = 100, default='0')
    code_QPV = models.CharField(max_length = 100, default='0')
    nom_QPV = models.CharField(max_length = 100, default='0')
    departement = models.CharField(max_length = 100, default='0')
    region = models.CharField(max_length = 100, default='0')
    statut_geo = models.CharField(max_length = 100, default='0')
    code = models.CharField(max_length = 100, default='0')
    federation = models.CharField(max_length = 100, default='0')
    clubs = models.CharField(max_length = 100, default='0')
    EPA = models.CharField(max_length = 100, default='0')
    Total = models.CharField(max_length = 100, default='0')
    Date = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"{self.code_commune} - {self.commune}"

class ODS_Player(models.Model):
    """ Class d'objets ODS Player """
    
    code_commune = models.CharField(max_length = 100, default='0')
    commune = models.CharField(max_length = 100, default='0')
    code_QPV = models.CharField(max_length = 100, default='0')
    nom_QPV = models.CharField(max_length = 100, default='0')
    departement = models.CharField(max_length = 100, default='0')
    region = models.CharField(max_length = 100, default='0')
    statut_geo = models.CharField(max_length = 100, default='0')
    code = models.CharField(max_length = 100, default='0')
    federation = models.CharField(max_length = 100, default='0')
    F_1_4_ans = models.CharField(max_length = 100, default='0')
    F_5_9_ans = models.CharField(max_length = 100, default='0')
    F_10_14_ans = models.CharField(max_length = 100, default='0')
    F_15_19_ans = models.CharField(max_length = 100, default='0')
    F_20_24_ans = models.CharField(max_length = 100, default='0')
    F_25_29_ans = models.CharField(max_length = 100, default='0')
    F_30_34_ans = models.CharField(max_length = 100, default='0')
    F_35_39_ans = models.CharField(max_length = 100, default='0')
    F_40_44_ans = models.CharField(max_length = 100, default='0')
    F_45_49_ans = models.CharField(max_length = 100, default='0')
    F_50_54_ans = models.CharField(max_length = 100, default='0')
    F_55_59_ans = models.CharField(max_length = 100, default='0')
    F_60_64_ans = models.CharField(max_length = 100, default='0')
    F_65_69_ans = models.CharField(max_length = 100, default='0')
    F_70_74_ans = models.CharField(max_length = 100, default='0')
    F_75_79_ans = models.CharField(max_length = 100, default='0')
    F_80_99_ans = models.CharField(max_length = 100, default='0')
    F_NR = models.CharField(max_length = 100, default='0')
    H_1_4_ans = models.CharField(max_length = 100, default='0')
    H_5_9_ans = models.CharField(max_length = 100, default='0')
    H_10_14_ans = models.CharField(max_length = 100, default='0')
    H_15_19_ans = models.CharField(max_length = 100, default='0')
    H_20_24_ans = models.CharField(max_length = 100, default='0')
    H_25_29_ans = models.CharField(max_length = 100, default='0')
    H_30_34_ans = models.CharField(max_length = 100, default='0')
    H_35_39_ans = models.CharField(max_length = 100, default='0')
    H_40_44_ans = models.CharField(max_length = 100, default='0')
    H_45_49_ans = models.CharField(max_length = 100, default='0')
    H_50_54_ans = models.CharField(max_length = 100, default='0')
    H_55_59_ans = models.CharField(max_length = 100, default='0')
    H_60_64_ans = models.CharField(max_length = 100, default='0')
    H_65_69_ans = models.CharField(max_length = 100, default='0')
    H_70_74_ans = models.CharField(max_length = 100, default='0')
    H_75_79_ans = models.CharField(max_length = 100, default='0')
    H_80_99_ans = models.CharField(max_length = 100, default='0')
    H_NR = models.CharField(max_length = 100)
    NR_NR = models.CharField(max_length = 100)
    Total = models.CharField(max_length = 100)
    Date = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"{self.code_commune} - {self.commune}"
# endregion

# region DWH

class D_City(models.Model):
    """summary

    Args:
        models (type): description
    """
    postal_code = models.CharField(max_length=5, primary_key=True,default=None)
    name = models.CharField(max_length=300, default=None)
    department = models.CharField(max_length=300, default=None)
    region = models.CharField(max_length=300, default=None)
    country = models.CharField(max_length=300, default=None)


# region Class Dimension
class D_Sex(models.Model):
    """ """
    code = models.CharField(max_length = 1, primary_key=True, default=None)

    def __str__(self) -> str:
        return f"{self.code}"

class D_AgeGRP(models.Model):
    """ """
    label = models.CharField(max_length = 100, primary_key=True, default=None)

    def __str__(self) -> str:
        return f"{self.label}"

class D_Type(models.Model):
    """ """
    label = models.CharField(max_length = 100, primary_key=True, default=None)

    def __str__(self) -> str:
        return f"{self.label}"

# region Dimension Commune
class D_Federation(models.Model):
    """ """
    code = models.IntegerField(primary_key=True)
    label = models.CharField(max_length = 100, default=None)

    def __str__(self) -> str:
        return f"{self.code} - {self.label}"

class D_Date(models.Model):
    """ """
    date = models.DateField(primary_key=True)
    
    def __str__(self) -> str:
        return f"{self.date}"

class D_Departement(models.Model):
    """ """
    code_Commune = models.CharField(max_length = 5, default='0')
    code_QPV = models.CharField(max_length = 5, default='0')
    code_Departement = models.CharField(max_length=5,default=0)

    pk_depart = models.CharField(max_length=100, primary_key=True, default=None)

    label_Commune = models.CharField(max_length = 100, default='0')
    label_QPV = models.CharField(max_length = 100, default='0')
    label_Departement = models.CharField(max_length = 100, default='0')

    label_Region = models.CharField(max_length = 100, default='0')
    statut = models.CharField(max_length = 100, default='0')

    def __str__(self) -> str:
        return f"{self.pk_depart} - {self.code_QPV}"

# endregion
# endregion


# region Class Fait
class F_Licence(models.Model):
    """ """
    nomber = models.IntegerField(default=0)

    Federation = models.ForeignKey(D_Federation, on_delete=models.CASCADE)
    Sex = models.ForeignKey(D_Sex, on_delete=models.CASCADE)
    Age_grp = models.ForeignKey(D_AgeGRP, on_delete=models.CASCADE)
    Date = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    Geo = models.ForeignKey(D_Departement, on_delete=models.CASCADE)

    pk_L = models.CharField(max_length=100, primary_key=True, default=None)
    
    def __str__(self) -> str:
        return f"{self.pk_L} - {self.nomber}"

class F_Club(models.Model):
    """ """
    nomber = models.IntegerField(default=None)

    Type = models.ForeignKey(D_Type, on_delete=models.CASCADE)
    Federation = models.ForeignKey(D_Federation, on_delete=models.CASCADE)
    Date = models.ForeignKey(D_Date, on_delete=models.CASCADE)
    Geo = models.ForeignKey(D_Departement, on_delete=models.CASCADE)

    pk_F = models.CharField(max_length=100, primary_key=True, default=None)

    def __str__(self) -> str:
        return f"{self.pk_F} - {self.nomber}"
# endregion

# endregion