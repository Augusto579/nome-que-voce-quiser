#ex3
import csv

def filtrar_vendas_por_produto(produto_nome):

    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))
        cabecalho = reader[0]
        vendas = reader[1:]  # tira o cabeçalho
        filtradas = [v for v in vendas if v[0].lower() == produto_nome.lower()]
        return [cabecalho] + filtradas  # devolve incluindo o cabeçalho

# Exemplo de uso
resultado = filtrar_vendas_por_produto("Dom Casmurro")
for linha in resultado:
    print(linha)


#ex4
def salvar_resultados_em_arquivo(dados, nome_arquivo="resultado.csv"):
    with open(nome_arquivo, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dados)  # grava todas as linhas
    print(f"Resultados gravados em {nome_arquivo}")

# Exemplo de uso junto com o filtro
dados_filtrados = filtrar_vendas_por_produto("Dom Casmurro")
salvar_resultados_em_arquivo(dados_filtrados, "dom_casmurro.csv")
