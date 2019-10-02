from unittest import TestCase
from dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):

    def setUp(self) -> None:
        self.roger = Usuario("Rogerio")
        self.pato = Usuario("Pato")
        self.poli = Usuario("Poliana")
        self.lance_do_roger = Lance(self.roger, 35.0)
        self.lance_do_pato = Lance(self.pato, 10.0)
        self.lance_da_poli = Lance(self.poli, 17.0)
        self.leilao = Leilao("Celular")

    #Este teste avalia se o valor do lance é maior ou menor em ordem decrescente.
    def test_avalia(self):
        self.leilao.propoe(self.lance_do_pato)
        self.leilao.propoe(self.lance_do_roger)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Este teste avalia se o valor do lance é maior ou menor em ordem crescente.
    def test_avalia2(self):
        self.leilao.propoe(self.lance_do_pato)
        self.leilao.propoe(self.lance_do_roger)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    #Verifica se os valores do menor e maior lance estão corretos em caso de um unico lance
    def teste_avalia3(self):
        self.leilao.propoe(self.lance_do_roger)

        self.assertEqual(35.0, self.leilao.menor_lance)
        self.assertEqual(35.0, self.leilao.maior_lance)

    # Verifica se os valores do menor e maior lance estão corretos em caso de 3 lances
    def teste_avalia4(self):
        self.leilao.propoe(self.lance_do_pato)
        self.leilao.propoe(self.lance_da_poli)
        self.leilao.propoe(self.lance_do_roger)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Se o leilao não tiver lances, deve permitir propor um lance
    def teste_avalia5(self):
        self.leilao.propoe(self.lance_do_roger)

        self.assertEqual(1, len(self.leilao.lances))

    # Se o ultimo usuário for diferente, deve permitir propor o lance
    def teste_avalia6(self):
        self.leilao.propoe(self.lance_da_poli)
        self.leilao.propoe(self.lance_do_roger)

        quantidade_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebidos)

    # Se o ultimo usuário for o mesmo, não deve permitir propor o lance
    def teste_avalia7(self):
        lance_roger_2 = Lance(self.roger, 20)

        # try:
        #     self.leilao.propoe(self.lance_do_roger)
        #     self.leilao.propoe(lance_roger_2)
        # except ValueError:
        #     quantidade_lances_recebidos = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_lances_recebidos)

        # Outra forma de fazer o tratamento de erro
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_roger)
            self.leilao.propoe(lance_roger_2)
