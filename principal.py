from dominio import Usuario, Leilao, Lance, Avaliador


roger = Usuario("Rogerio")
pato = Usuario("Pato")

lance_do_roger = Lance(roger, 35.0)
lance_do_pato = Lance(pato, 10.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_pato)
leilao.lances.append(lance_do_roger)

for lance in leilao.lances:
    print(f"Usuário {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O maior lance foi {avaliador.maior_lance} e o menor lance foi {avaliador.menor_lance}.")


