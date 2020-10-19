# This dataset report of the number of forest fires in Brazil divided by states. The series comprises the period of approximately 10 years (1998 to 2017).
#  The data were obtained from the official website of the Brazilian government.

import csv
import statistics as sts
import matplotlib.pyplot as plt
import numpy as np

def dadosQueimadas():
    
    # parte do dataset que contém perto de 1200 dados. 
    norte = ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]

    dadosQueimadasNorte = []
    numQueimadas = []

    # salvando apenas os dados do norte
    with open('amazon.csv', 'r', encoding = "ISO-8859-1") as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')

        for coluna in leitor:
            if(coluna[1] in norte):
                dadosQueimadasNorte.append(coluna)

    for dado in dadosQueimadasNorte:    
        numQueimadas.append(dado[3])

    #trocando os números como: "1.024", para "1024" para que o max e min funcionem perfeitamente
    numQueimadasAux=[]
    for dado in numQueimadas:
        if '.' in dado:
            dado = dado.replace('.', '')
            numQueimadasAux.append(int(dado))
        else:
            numQueimadasAux.append(int(dado))
    
    return numQueimadasAux

#Distribuição de frequência
def distribuicaoDeFrequencia():
    numQueimadas = dadosQueimadas()
    n_classes = 10
    n_ocorrencias = len(numQueimadas)
    frequencias = {'classe1': 0, 'classe2': 0, 'classe3': 0, 'classe4': 0, 'classe5': 0, 'classe6': 0, 'classe7': 0, 'classe8': 0, 'classe9': 0, 'classe10': 0}

    #calculando amplitude
    maior = max(numQueimadas)
    menor = min(numQueimadas)

    amplitude = maior-menor

    amplitude_classe = round(amplitude/n_classes)

    limites_inf = [menor]
    for i in range(n_classes):
        limites_inf.append(limites_inf[i]+amplitude_classe)
    
    for dado in numQueimadas:
        if(dado < limites_inf[1]):
            frequencias['classe1'] +=1
        elif(dado < limites_inf[2]):
            frequencias['classe2'] +=1
        elif(dado < limites_inf[3]):
            frequencias['classe3'] +=1
        elif(dado < limites_inf[4]):
            frequencias['classe4'] +=1
        elif(dado < limites_inf[5]):
            frequencias['classe5'] +=1
        elif(dado < limites_inf[6]):
            frequencias['classe6'] +=1
        elif(dado < limites_inf[7]):
            frequencias['classe7'] +=1
        elif(dado < limites_inf[8]):
            frequencias['classe8'] +=1
        elif(dado < limites_inf[9]):
            frequencias['classe9'] +=1
        else:            
            frequencias['classe10'] +=1

    
    print("--------------------------------------------------------------------------------------------")
    print("|             CLASSE           |           FREQUENCIA         |              %             |")    
    print("|          ",limites_inf[0]," - ", (limites_inf[0]+(amplitude_classe-1)),"        |           ", frequencias['classe1'],"             |           ", round((frequencias['classe1']/n_ocorrencias)*100, 2) ,"%         |")
    print("|        ",limites_inf[1]," - ", (limites_inf[1]+(amplitude_classe-1)),"       |           ", frequencias['classe2'],"               |           ", round((frequencias['classe2']/n_ocorrencias)*100, 2) ,"%          |")
    print("|        ",limites_inf[2]," - ", (limites_inf[2]+(amplitude_classe-1)),"       |           ", frequencias['classe3'],"               |           ", round((frequencias['classe3']/n_ocorrencias)*100, 2) ,"%          |")
    print("|        ",limites_inf[3]," - ", (limites_inf[3]+(amplitude_classe-1)),"       |           ", frequencias['classe4'],"               |           ", round((frequencias['classe4']/n_ocorrencias)*100, 2) ,"%          |")
    print("|       ",limites_inf[4]," - ", (limites_inf[4]+(amplitude_classe-1)),"      |           ", frequencias['classe5'],"                |           ", round((frequencias['classe5']/n_ocorrencias)*100, 2) ,"%          |")
    print("|       ",limites_inf[5]," - ", (limites_inf[5]+(amplitude_classe-1)),"      |           ", frequencias['classe6'],"                |           ", round((frequencias['classe6']/n_ocorrencias)*100, 2) ,"%          |")
    print("|       ",limites_inf[6]," - ", (limites_inf[6]+(amplitude_classe-1)),"      |           ", frequencias['classe7'],"                |           ", round((frequencias['classe7']/n_ocorrencias)*100, 2) ,"%          |")
    print("|       ",limites_inf[7]," - ", (limites_inf[7]+(amplitude_classe-1)),"      |           ", frequencias['classe8'],"                |           ", round((frequencias['classe8']/n_ocorrencias)*100, 2) ,"%           |")
    print("|       ",limites_inf[8]," - ", (limites_inf[8]+(amplitude_classe-1)),"      |           ", frequencias['classe9'],"                |           ", round((frequencias['classe9']/n_ocorrencias)*100, 2) ,"%           |")
    print("|       ",limites_inf[9]," - ", (maior),"      |           ", frequencias['classe10'],"                |           ", round((frequencias['classe10']/n_ocorrencias)*100, 2) ,"%          |")
    print('\n')
    
    print("Comentário: \nEh possível perceber com a distribuição de frequência acima que a maior quantidade de focos de queimadas reportados estão entre 0 - 2499 focos, chegando a quase 90% de frequência. \nOutro ponto interessante é que praticamente não houve meses onde foram reportados mais que 10.000 queimadas. \n")


    #histograma de frequência
    plt.hist(numQueimadas, 10)
    plt.xlabel('Classes')
    plt.ylabel('Quantidade')
    plt.title('Ocorrências das Classes')
    plt.grid(True)
    plt.show()


#Calculo Media, mediana e moda
def mediaMedianaModa():
    numQueimadas = dadosQueimadas();   

    media = sts.mean(numQueimadas)

    print("Media: ", round(media, 2))

    numQueimadas = sorted(numQueimadas)
    mediana = sts.median(numQueimadas)
    print("Mediana: ", mediana)

    moda = sts.mode(numQueimadas)
    print("Moda: ", moda)

    print("Comentário: \nPodemos perceber que há uma grande amplitude entre a média e a mediana, perceber também que o número de queimadas que foi mais reportado foi 0(nenhuma queimada). Porém, a média de queimadas por mês de 98 até 2017 ainda é muito alta, cerca de 841 queimadas por mês.\n")

#calculo das medidas de variação
def medidasDeVariação():
    numQueimadas = dadosQueimadas()
    
    amplitude = max(numQueimadas) - min(numQueimadas)

    variancia = np.var(numQueimadas)
    print("Variancia: ", round(variancia, 2))

    desviopadrao = np.std(numQueimadas)
    print("Desvio Padrão: ", round(desviopadrao, 2))

    print("Comentário:\nAqui é perceptível que mesmo com uma média de 841.76, o desvio padrão é de 2002.24 mostrando que os dados apresentados no dataset tem uma dispersão alta.\n")


def bloxPlot():
    numQueimadas = dadosQueimadas()

    print("Comentário:\nVisualizando o gráfico é possível perceber que os dados se apresentam principalmente nos pontos considerados fora da curva.\n")

    plt.boxplot(numQueimadas)
    plt.title("Boxplot do número de queimadas por mes no norte (1998 - 2017)")
    plt.xlabel("Quantidade")
    plt.grid()
    plt.show()

    


def menu():
    while(True):
        print("\n")
        print("Escolha uma das opções abaixo: ")
        print("1 - Distribuição de Frequência\n2 - Media, mediana e moda\n3 - Medidas de variação\n4 - Gráfico Box-Plot\n5 - Sair")
        print("Obs.: Os comentários foram feitos em forma de 'print()' ao fim de cada função, aparecendo no terminal/cmd. Ou no próprio código.'")
        
        opc = input()
        print("\n")
        if(opc == "1"):
            distribuicaoDeFrequencia()
        elif(opc == "2"):
            mediaMedianaModa()
        elif(opc == "3"):
            medidasDeVariação()
        elif(opc == "4"):
            bloxPlot()
        elif(opc == "5"):
            break
        else:
            print("ERRO: Opção errada\n\n\n\n\n\n\n")
        

menu()