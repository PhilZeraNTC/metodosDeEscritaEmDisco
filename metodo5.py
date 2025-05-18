import pandas as pd

def escritaDelimitando(arquivoSaida, dataset):
    # Lê o arquivo CSV e armazena em um DataFrame
    df = pd.read_csv(dataset)
    # Converte cada linha em uma string com campos separados por espaço
    registros = [' '.join(map(str, row)) for _, row in df.iterrows()]
    # Junta todos os registros com '#' e escreve no arquivo
    with open(arquivoSaida, 'w', encoding='utf-8') as file:
        file.write('#'.join(registros))

if __name__ == '__main__':
    escritaDelimitando('saida1.txt', 'animes.csv')