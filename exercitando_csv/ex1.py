#1- Leitura de dados
import csv

def ler_dados_csv():
    with open('livros.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

ler_dados_csv()