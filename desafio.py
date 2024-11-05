import csv

nome_arquivo = 'files/vendas.csv'

def ler_csv(caminho_do_arquivo: str) -> list[dict]:
    lista = []
    with open(caminho_do_arquivo, mode="r", encoding="UTF-8") as csv_file:
        arquivo = csv.DictReader(csv_file)

        for linha in arquivo:
            lista.append(linha)

    return lista


def processar_dados(lista_dicionario: list[dict]) -> dict:
    dicionario_produto = {}

    for linha in lista_dicionario:
        categoria = linha['Categoria']
        produto = [linha['Produto'], linha['Quantidade'], linha['Venda']]

        if categoria in dicionario_produto:
            dicionario_produto[categoria].append(produto)
        else:
            dicionario_produto[categoria] = [produto]
    return dicionario_produto


# dados_funcao1 = ler_csv(nome_arquivo)
# dados_funcao2 = processar_dados(dados_funcao1)
# print(dados_funcao2)