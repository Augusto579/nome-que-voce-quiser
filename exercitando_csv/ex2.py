import csv

def calcular_vendas_total():
    total = 0.0
    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # pula o cabeçalho
        for row in reader:
            preco = float(row[2])       # coluna Preço
            quantidade = int(row[3])    # coluna Quantidade
            total += preco * quantidade
    return total

# Exemplo de uso
print(f"Valor total das vendas: R$ {calcular_vendas_total():.2f}")
