def filtrar_vendas_por_produto(vendas, produto_nome):
    return [v for v in vendas if v[0].lower() == produto_nome.lower()]

# Exemplo de uso
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
    reader = list(csv.reader(csvfile))
    next(reader)  # pula cabeçalho
    filtradas = filtrar_vendas_por_produto(reader, "Dom Casmurro")
    print("Vendas filtradas:", filtradas)
