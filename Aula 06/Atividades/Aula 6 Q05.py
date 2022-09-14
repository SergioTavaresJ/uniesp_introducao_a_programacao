lista_celebridades = [
    "Neymar",
    "Charlie Brown",
    "Bob Marley",
    "Matuê",
    "JayZ"]

# Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.

for nome in lista_celebridades:
    print(f"{nome}, Olá é com enorme satisfação que envio esse convite a você, para te receber em um jantar que darei dia 29/10/2022 Quinta-feira ,o jantar será realizado no Dolphin Hotel na ilha de Fernando de Noronha,te espero lá  ")

# Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.

print("Charlie Brown e JayZ não poderão ir ao jantar")

# Modifique sua lista, substitua os desistentes por novos convidados.

nova_lista_celebridades = [
    "Neymar",
    "Bob Marley",
    "Marquezine",
    "Matuê",
    "Will Smith"]

# Exiba um novo convite para cada pessoa que continua presente em sua lista.

for nome in nova_lista_celebridades:
    print(f"{nome},É com muita alegria que venho lhe convidar para uma festa na minha residência no Hotel California,420.Domingo,04/02, às 22 horas")