from django.test import TestCase

# Create your tests here.
from rota.models import Rota, Voo

class RotaModelCreateTest(TestCase): 
    @classmethod
    def setUpTestData(cls):
        Rota.objects.create(
            codigo='D0810', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
    def test_criacao_id(self):
        rota_1 = Rota.objects.get(codigo='D0810')
        self.assertEqual(rota_1.id, 1)

class RotaModelReadTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rota.objects.create(
            codigo='D0810', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
    def test_get_rota(self):
        rota_1 = Rota.objects.get(origem='Goiânia', destino='Rio de Janeiro', companhia_aerea='Varig')
        self.assertEqual(rota_1.codigo, 'D0810')

class RotaModelUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rota.objects.create(
            codigo='D0810', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
    def test_criacao_id(self):
        rota_1 = Rota.objects.get(codigo='D0810')
        self.assertEqual(rota_1.id, 1)


class VooModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        rota_1 = Rota.objects.create(
            codigo='D0810', 
            origem='Goiânia',
            destino='Rio de Janeiro',
            aeroporto_partida='Santa Genoveva',
            aeroporto_chegada='Santos Dumont',
            hora_partida_prevista='08:43',
            hora_chegada_prevista='10:00',
            aeronave='A320',
            companhia_aerea='Varig'
        )
        Voo.objects.create(
            rota=rota_1,
            data='2022-07-11',
            hora_partida='',
            hora_chegada='',
            piloto='Comandante Denio Almeida',
            status='Programado'
        )

    def test_criacao_id(self):
        rota_1 = Rota.objects.get(codigo='D0810')
        voo_1 = Voo.objects.get(rota=rota_1, data='2022-07-11')
        self.assertEqual(voo_1.id, 1)

class EmprestimoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(nome="Michelet")
        Livro.objects.create(titulo='Os Irmãos Karamazov')
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        usuario_1 = Usuario.objects.get(nome="Michelet")
        Emprestimo.objects.create(livro=livro_1, usuario=usuario_1)
    def test_criacao_emprestimo_id(self):
        emprestimo_1 = Emprestimo.objects.get(id=1)
        self.assertEqual(emprestimo_1.usuario.id,1)