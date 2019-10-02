from dominio import Usuario, Leilao
import pytest


@pytest.fixture
def roger():
    return Usuario("Roger", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Mustang")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(roger, leilao):
    roger.propoe_lance(leilao, 50.0)

    assert roger.carteira == 50.0


def test_deve_permitir_propor_lance_quando_valor_e_menor_que_o_valor_da_carteira(roger, leilao):
    roger.propoe_lance(leilao, 1.0)

    assert roger.carteira == 99.0


def test_deve_permitir_propor_lance_quando_valor_e_igual_ao_valor_da_carteira(roger, leilao):
    roger.propoe_lance(leilao, 100.0)

    assert roger.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(roger, leilao):
    with pytest.raises(ValueError):
        roger.propoe_lance(leilao, 200.0)
