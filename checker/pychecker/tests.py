from django.test import TestCase
from pychecker.utils.connecto import verifica_status_do_site

class teste(TestCase):
    def teste_site_sem_conexao_com_net(self):
        """
        Testando a conectividade de um site offline 
        """
        url = 'este-site-não-exite.org'
        status = verifica_status_do_site(url)
        self.assertIs(status, False)

    def teste_site_esta_online(self):
        """
        Testando a solicitação de um site que esta online
        """
        url = 'free.facebook.com'
        status = verifica_status_do_site(url)
        self.assertIs(status, True) 

class TesteDeViews(TestCase):
    def teste_da_home(self):
        """Testando a views home """
        resposta = self.client.get('/')
        self.assertEqual(resposta.status_code, 200)
