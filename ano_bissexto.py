def contar_bissextos(limite):
    multiplos_4   = limite // 4   - (1999 // 4)
    multiplos_100 = limite // 100 - (1999 // 100)
    multiplos_400 = limite // 400 - (1999 // 400)
    return multiplos_4 - multiplos_100 + multiplos_400

# Programa principal com validador
while True:
    ano_final = int(input("Digite o ano final (entre 2000 e 4000): "))
    if 2000 <= ano_final <= 4000:
        break
    else:
        print("Ano inválido! Digite um valor entre 2000 e 4000.")

print(f"Quantidade de anos bissextos de 2000 até {ano_final}: {contar_bissextos(ano_final)}")
