from excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if self.valor_de_lance_invalido(valor):
            raise LanceInvalido("Não há dinheiro disponível na carteira.")

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def valor_de_lance_invalido(self, valor):
        return valor > self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self.lance_valido(lance):
            if not self.tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def tem_lances(self):
        return self.__lances

    def usuarios_diferentes(self, lance: Lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar 2 lances seguidos.")

    def valor_maior_que_lance_anterior(self, lance: Lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O valor do lance não pode ser menor que o valor do lance anterior.")

    def lance_valido(self, lance: Lance):
        return not self.tem_lances() or self.usuarios_diferentes(lance) and self.valor_maior_que_lance_anterior(lance)
