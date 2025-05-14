def escritaIndexRegistro(arquivo, nomeSaida):
    with open(arquivo, 'r', encoding='utf-8') as arquivo_entrada, \
             open(nomeSaida, 'w', encoding='utf-8') as arquivo_saida:
            for linha in arquivo_entrada:
                tamanho_linha = len(linha.strip('\n'))  
                arquivo_saida.write(str(tamanho_linha) + '\n')
            


if __name__ == '__main__':
    
    with open('animes.csv', 'r', encoding='utf-8') as f:
        animes = f.readlines()
    
    animes.pop(0)
    
    escritaIndexRegistro('saida2.txt', animes)
    
