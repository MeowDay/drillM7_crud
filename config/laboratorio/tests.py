from django.test import TestCase
#importadas
from django.test import SimpleTestCase # para el testo de paginas estaticas
from django.urls import reverse
from .models import Laboratorio
# Create your tests here.


#Selenium libreria

class InicioTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/inicio_test')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'inicio_test.html')
    
    def test_template_content(self):
        response = self.client.get(reverse('inicio'))
        self.assertContains(response, '<h1>Página de prueba</h1>')
        self.assertNotContains(response, 'No es la pagina')


class LabTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre = 'Laboratorio 5',
                                              ciudad = 'Santiago',
                                              pais='Chile')
    
    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio 5')
        self.assertEqual(self.laboratorio.ciudad, 'Santiago')
        self.assertEqual(self.laboratorio.pais, 'Chile')