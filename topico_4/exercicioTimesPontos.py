# **********************************************************************************************************************
# ******   Programação II -  2º Ciclo Jogos Digitais                                                              ******
# ******   Programa: Crie um programa para acompanhar os jogos do campeonato brasileiro, para os times :          ******
# ******            (Corinthians, São Paulo, Palmeiras, Santos e Flamengo). O campeonato é composto por 30 jogos. ******
# ******            a) Crie uma matriz para guardar estas informações                                             ******
# ******            b) Faça um código que peça os pontos dos jogos de cada time e coloque as informações nas      ******
# ******               posições corretas da matriz.                                                               ******
# ******            c) Faça um código que informe a média de pontos dos jogos.                                    ******
# ******            d) Faça um código para mostrar qual time manteve a maior pontuação dos jogos.                 ******
# ******   Nome....: Diego Vinicius de Mello Munhoz    RA: 1430961723002                                          ******
# ******   Data....: 07/04/2018                                                                                   ******
# **********************************************************************************************************************

import statistics

def separa_pontos(campeonato):
    print("\nResultado do Campeonato")
    for time in campeonato:
        if time.get('time') == 'CORINTHIANS':
            pontos_corinthians.append(time.pop('pontos'))
        elif time.get('time') == 'SAOPAULO':
            pontos_saopaulo.append(time.pop('pontos'))
        elif time.get('time') == 'PALMEIRAS':
            pontos_palmeiras.append(time.pop('pontos'))
        elif time.get('time') == 'SANTOS':
            pontos_santos.append(time.pop('pontos'))
        else:
            pontos_flamengo.append(time.pop('pontos'))
    pontos_corinthians.sort()
    pontos_saopaulo.sort()
    pontos_palmeiras.sort()
    pontos_santos.sort()
    pontos_flamengo.sort()

def media_pontos():
    media_corinthians = statistics.mean(pontos_corinthians)
    media_saopaulo = statistics.mean(pontos_saopaulo)
    media_palmeiras = statistics.mean(pontos_palmeiras)
    media_santos = statistics.mean(pontos_santos)
    media_flamengo = statistics.mean(pontos_flamengo)

    if (media_corinthians > media_saopaulo) and (media_corinthians > media_palmeiras) and (media_corinthians > media_santos) and (media_corinthians > media_flamengo):
        media_pt = {"time": 'Corinthians', "pontos": media_corinthians}
    elif(media_saopaulo > media_corinthians) and (media_saopaulo > media_palmeiras) and (media_saopaulo> media_santos) and (media_saopaulo > media_flamengo):
        media_pt = {"time": 'Sao Paulo', "pontos": media_saopaulo}
    elif(media_palmeiras > media_saopaulo) and (media_palmeiras > media_corinthians) and (media_palmeiras > media_santos) and (media_palmeiras > media_flamengo):
        media_pt = {"time": 'Palmeiras', "pontos": media_palmeiras}
    elif(media_santos > media_saopaulo) and (media_santos > media_palmeiras) and (media_santos > media_corinthians) and (media_santos > media_flamengo):
        media_pt = {"time": 'Santos', "pontos": media_santos}
    else:
        media_pt = {"time": 'Flamengo', "pontos": media_flamengo}

    print(("O {} teve a maior media com {} pontos").format(media_pt['time'],media_pt.get('pontos')))

def mediana_pontos():
    mediana_corinthians = statistics.mean(pontos_corinthians)
    mediana_saopaulo = statistics.mean(pontos_saopaulo)
    mediana_palmeiras = statistics.mean(pontos_palmeiras)
    mediana_santos = statistics.mean(pontos_santos)
    mediana_flamengo = statistics.mean(pontos_flamengo)

    if (mediana_corinthians > mediana_saopaulo) and (mediana_corinthians > mediana_palmeiras) and (mediana_corinthians > mediana_santos) and (mediana_corinthians > mediana_flamengo):
        mediana_pt = {"time":'Corinthians', "pontos": mediana_corinthians}
    elif(mediana_saopaulo > mediana_corinthians) and (mediana_saopaulo > mediana_palmeiras) and (mediana_saopaulo> mediana_santos) and (mediana_saopaulo > mediana_flamengo):
        mediana_pt = {"time":'Sao Paulo', "pontos": mediana_saopaulo}
    elif(mediana_palmeiras > mediana_saopaulo) and (mediana_palmeiras > mediana_corinthians) and (mediana_palmeiras > mediana_santos) and (mediana_palmeiras > mediana_flamengo):
        mediana_pt = {"time":'Palmeiras', "pontos": mediana_palmeiras}
    elif(mediana_santos > mediana_saopaulo) and (mediana_santos > mediana_palmeiras) and (mediana_santos > mediana_corinthians) and (mediana_santos > mediana_flamengo):
        mediana_pt = {"time":'Santos', "pontos": mediana_santos}
    else:
        mediana_pt = {"time":'Flamengo', "pontos": mediana_flamengo}

    print(("O {} manteve a maior pontuação dos jogos - maior sequencia de pontos: {}").format(mediana_pt['time'], mediana_pt['pontos']))

times = ['CORINTHIANS', 'SAOPAULO', 'PALMEIRAS', 'SANTOS', 'FLAMENGO']

dicionario = {}

media_pt = {}
mediana_pt = {}

campeonato = []

pontos_corinthians = []
pontos_saopaulo = []
pontos_palmeiras = []
pontos_santos = []
pontos_flamengo = []

for time in times:
    print(('Informe os pontos do {}:').format(time))
    for r in range(1,31):

        invalido = True
        while invalido:
            try:
                pontos = int(input(("Pontos da {}° rodada:").format(r)))
                if (pontos <= 0) or (pontos > 3):
                    print("Um numero entre 0 e 3!")
                    invalido = True
                else:
                    invalido = False
            except ValueError:
                print("Informe um numero valido!")
                continue

        dicionario = {"time": time, "pontos": pontos, "rodada": r}
        campeonato.append(dicionario)

separa_pontos(campeonato)
media_pontos()
mediana_pontos()