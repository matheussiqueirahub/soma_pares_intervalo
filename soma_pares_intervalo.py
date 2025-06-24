inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

soma_pares = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
else:
   
    if soma_pares == 0:
        print(f"Não há números pares no intervalo de {inicio} a {fim}.")
    else:
        print(f"A soma dos números pares no intervalo de {inicio} a {fim} é: {soma_pares}")