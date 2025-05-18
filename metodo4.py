def escritaIndexRegistro(arquivo, nomeSaida):
    with open(arquivo, 'r', encoding='utf-8') as arquivo_entrada, \
         open(nomeSaida, 'w', encoding='utf-8') as arquivo_saida:
        next(arquivo_entrada)  # Pula a primeira linha (cabeçalho)
        for linha in arquivo_entrada:
            tamanho_linha = len(linha.strip('\n').encode('utf-8'))  # Tamanho em bytes, sem \n
            arquivo_saida.write(str(tamanho_linha) + '\n')

if __name__ == '__main__':
    escritaIndexRegistro('animes.csv', 'saida2.txt')