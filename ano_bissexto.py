def contar_bissextos(limite):
    contador = 0
    for ano in range(2000, limite + 1):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            contador += 1
    return contador

# Programa principal
ano_final = int(input("Digite o ano final: "))
qtd = contar_bissextos(ano_final)

print(f"Quantidade de anos bissextos de 2000 até {ano_final}: {qtd}")