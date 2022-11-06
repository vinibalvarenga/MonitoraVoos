from django.test import TestCase,SimpleTestCase
from django.urls import reverse



# Essa primeira classe testa a pagina da area logada,
# a de gerenciamento de voos, monitoramento e a de relatorios
  
class NavegacaoInicialViewTest (SimpleTestCase):
  
# home page
    def test_view_home_page_avaible(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'areaLogada.html' )

    def test_view_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "<title>Área logada</title>")
        self.assertNotContains(response, "Not on the page")
#crud
    def test_view_crud_avaible(self):
        response = self.client.get(reverse('crud'))
        self.assertEqual(response.status_code, 200)

    def test_view_crud_template(self):
        response = self.client.get(reverse('crud'))
        self.assertTemplateUsed(response,'crud.html' )

    def test_view_home_page_content(self):
        response = self.client.get(reverse('crud'))
        self.assertContains(response, "Cadastramento CRUD")
        self.assertNotContains(response, "Not on the page") 

    def test_view_criar_rota(self):
        response = self.client.get(reverse('criar-rota'))
        self.assertEqual(response.status_code, 200)