primeiroNome = input("digite seu primeiro nome: ")
dia = input("dia do nascimento:")
mês = input("mês do nascimento:")
ano = input("ano do nascimento:")

mensagem = "{} nasceu no dia: {}/{}/{}"

print (mensagem.format(primeiroNome, dia, mês, ano))