from unittest import TestCase
from dominio import Usuario, Leilao, Lance, Avaliador


class TestAvaliador(TestCase):

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
        self.leilao.lances.append(self.lance_do_pato)
        self.leilao.lances.append(self.lance_do_roger)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    # Este teste avalia se o valor do lance é maior ou menor em ordem crescente.
    def test_avalia2(self):
        self.leilao.lances.append(self.lance_do_pato)
        self.leilao.lances.append(self.lance_do_roger)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    #Verifica se os valores do menor e maior lance estão corretos em caso de um unico lance
    def teste_avalia3(self):
        self.leilao.lances.append(self.lance_do_roger)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(35.0, avaliador.menor_lance)
        self.assertEqual(35.0, avaliador.maior_lance)

    # Verifica se os valores do menor e maior lance estão corretos em caso de 3 lances
    def teste_avalia4(self):
        self.leilao.lances.append(self.lance_do_pato)
        self.leilao.lances.append(self.lance_do_roger)
        self.leilao.lances.append(self.lance_da_poli)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 10.0
        maior_valor_esperado = 35.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)