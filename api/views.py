from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics
from polls.models import D_AgeGRP,D_Date,D_Federation,D_Departement,D_Sex,D_Type,F_Licence,F_Club
from api.serializers import F_Club_Serializer, F_Licence_Serializer,D_AgeGRP_Serializer,D_Date_Serializer,D_Federation_Serializer,D_Departement_Serializer,D_Sex_Serializer,D_Type_Serializer

class Detail_Table(generics.RetrieveUpdateDestroyAPIView):

    def get_serializer_class(self):
        table = self.kwargs['table']
        serializer_class = None
        
        if table == 'date':
            serializer_class = D_Date_Serializer
        elif table == 'agegrp':
            serializer_class = D_AgeGRP_Serializer
        elif table == 'sex':
            serializer_class = D_Sex_Serializer
        elif table == 'type':
            serializer_class = D_Type_Serializer
        elif table == 'departement':
            serializer_class = D_Departement_Serializer
        elif table == 'federation':
            serializer_class = D_Federation_Serializer
        elif table == 'licence':
            serializer_class = F_Licence_Serializer
        elif table == 'club':
            serializer_class = F_Club_Serializer
        else:
            serializer_class = None
        
        return serializer_class

    def get_queryset(self):
        table = self.kwargs['table']
        pk = self.kwargs['pk']
        
        if table == 'date':
            return D_Date.objects.filter(date=pk)
        elif table == 'agegrp':
            return D_AgeGRP.objects.filter(pk=pk)
        elif table == 'sex':
            return D_Sex.objects.filter(pk=pk)
        elif table == 'type':
            return D_Type.objects.filter(pk=pk)
        elif table == 'departement':
            return D_Departement.objects.filter(pk=pk)
        elif table == 'federation':
            return D_Federation.objects.filter(pk=pk)
        elif table == 'licence':
            return F_Licence.objects.filter(pk=pk)
        elif table == 'club':
            return F_Club.objects.filter(pk=pk)
        else:
            return None

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        queryset = self.get_queryset()

        if queryset is None:
            return Response({'message': 'queryset nonetype'}, status=status.HTTP_404_NOT_FOUND)
        if serializer_class is None:
            return Response({'message': 'serializer_class nonetype'}, status=status.HTTP_404_NOT_FOUND)
            
        if queryset.exists():
            serializer = serializer_class(queryset.first())
            return Response(serializer.data)
        else:
            return Response({'message': 'Objet non trouvé'}, status=status.HTTP_404_NOT_FOUND)


class List_Table(APIView):
    def get(self, request, format=None):
        table = self.request.query_params.get('table', None)
        match table:
            case 'Club':
                queryset = F_Club.objects.all()
                serializer_class = F_Club_Serializer
            case 'Licence':
                queryset = F_Licence.objects.all()
                serializer_class = F_Licence_Serializer
            case 'Agegrp':
                queryset = D_AgeGRP.objects.all()
                serializer_class = D_AgeGRP_Serializer
            case 'Date':
                queryset = D_Date.objects.all()
                serializer_class = D_Date_Serializer
            case 'Federation':
                queryset = D_Federation.objects.all()
                serializer_class = D_Federation_Serializer
            case 'Departement':
                queryset = D_Departement.objects.all()
                serializer_class = D_Departement_Serializer
            case 'Sex':
                queryset = D_Sex.objects.all()
                serializer_class = D_Sex_Serializer
            case 'Type':
                queryset = D_Type.objects.all()
                serializer_class = D_Type_Serializer
            case _:
                return Response({'message': 'Table invalide'}, status=400)
        
        nombre_de_lignes = queryset.count()
        
        paginator = PageNumberPagination()
        paginator.page_size = 25
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = serializer_class(paginated_queryset, many=True)
        result = {
            'home' : 'http://localhost:8000/admin',
            'nombre_de_lignes': nombre_de_lignes,
            'nom_de_table': table,
            'data': serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }
        return Response(result, status=status.HTTP_200_OK)


class D_Date_Create(APIView):
    def post(self, request, format=None):
        serializer = D_Date_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

