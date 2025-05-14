def escritaQtdeCampos(arquivo, dataset):
    with open(arquivo, 'w') as file:
        for registro in dataset:
            novoregistro = registro.replace(',', '|')
            novoregistro = novoregistro.replace('\n', '')
            file.write(novoregistro)
            
            
            
if __name__ == '__main__':
    
    with open('animes.csv', 'r', encoding='utf-8') as f:
        animes = f.readlines()
    
    animes.pop(0)
    
    escritaQtdeCampos('saida1.txt', animes) 