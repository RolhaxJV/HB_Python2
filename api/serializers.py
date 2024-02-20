# serializers.py
from rest_framework import serializers
from polls.models import D_AgeGRP,D_Date,D_Federation,D_Departement,D_Sex,D_Type,D_City,F_Licence,F_Club

# region FAIT
class F_Club_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_Club
        fields = '__all__'

class F_Licence_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_Licence
        fields = '__all__'
# endregion

# region DIMENSION
class D_AgeGRP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_AgeGRP
        fields = '__all__'

class D_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Type
        fields = '__all__'

class D_Date_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Date
        fields = '__all__'

class D_Federation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Federation
        fields = '__all__'

class D_Departement_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Departement
        fields = '__all__'
        
class D_Sex_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_Sex
        fields = '__all__'
        
class D_City_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_City
        fields = '__all__'
# endregion