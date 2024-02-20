from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api.views import Detail_Table,List_Table
import json


factory = APIRequestFactory()
req = factory.get('Detail/')
view = Detail_Table.as_view()

li_res_tg = view(req, table="licence", pk='605_F_1_4_2021-01-01_1001_CSZ')
li_res_tg.render()
li_json_res_tg = json.loads(li_res_tg.content)

li_res_tgonf = view(req, table="licence", pk='12345')
li_res_tgonf.render()

li_res_git = view(req, table="invalid_table", pk='12345')
li_res_git.render()

li_res_gip = view(req, table="licence", pk='invalid_pk')
li_res_gip.render()

cl_res_tg = view(req, table="club", pk='124_clubs_2021-01-01_01001_CSZ')
cl_res_tg.render()
cl_json_res_tg = json.loads(cl_res_tg.content)

cl_res_tgonf = view(req, table="club", pk='5678')
cl_res_tgonf.render()

cl_res_git = view(req, table="invalid_table", pk='12345')
cl_res_git.render()

cl_res_gip = view(req, table="club", pk='invalid_pk')
cl_res_gip.render()

req = factory.get('List/',{'table': 'Club'})
view = List_Table.as_view()

cl_res_ndl = view(req)

req = factory.get('List/',{'table': 'Licence'})
li_res_ndl = view(req)


class TestLicence(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        data = {
            "pk_L": "605_F_1_4_2021-01-01_1001_CSZ",
            "nomber": 8,
            "Federation": 605,
            "Sex": "F",
            "Age_grp": "1_4",
            "Date": "2021-01-01",
            "Geo": "1001_CSZ"
        }
        self.assertEqual(li_json_res_tg, data)
    
    def test_get_object_not_found(self):
        self.assertEqual(li_res_tgonf.status_code, 404)
        self.assertEqual(li_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        self.assertEqual(li_res_git.status_code, 404)
        self.assertEqual(li_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        self.assertEqual(li_res_gip.status_code, 404)
        self.assertEqual(li_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        self.assertEqual(li_res_ndl.status_code, 200)
        self.assertEqual(li_res_ndl.data['nombre_de_lignes'], 14000)

class TestClub(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        data = {
                    "pk_F": "124_clubs_2021-01-01_01001_CSZ",
                    "nomber": 1,
                    "Type": "clubs",
                    "Federation": 124,
                    "Date": "2021-01-01",
                    "Geo": "01001_CSZ"
                }
        self.assertEqual(cl_json_res_tg, data)
    
    def test_get_object_not_found(self):
        self.assertEqual(cl_res_tgonf.status_code, 404)
        self.assertEqual(cl_res_tgonf.data['message'], 'Objet non trouvé')

    def test_get_invalid_table(self):
        self.assertEqual(cl_res_git.status_code, 404)
        self.assertEqual(cl_res_git.data['message'], 'queryset nonetype')

    def test_get_invalid_pk(self):
        self.assertEqual(cl_res_gip.status_code, 404)
        self.assertEqual(cl_res_gip.data['message'], 'Objet non trouvé')

    def test_nombre_de_lignes(self):
        self.assertEqual(cl_res_ndl.status_code, 200)
        self.assertEqual(cl_res_ndl.data['nombre_de_lignes'], 11000)