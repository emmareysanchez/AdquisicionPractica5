import requests
from bs4 import BeautifulSoup

def extract():#pasamos la url de web a html usando requests
    web = 'https://www.sportytrader.es/cuotas/baloncesto/usa/nba-306/'
    resultado = requests.get(web)
    # lo pasamos a texto para que beautiful soup pueda trabajar con ello
    soup = BeautifulSoup(resultado.content, 'html.parser')
    return soup

def transform(soup):
    cuotas = soup.find_all('span',{'class':'px-1 h-booklogosm font-bold bg-primary-yellow text-white leading-8 rounded-r-md w-14 md:w-18 flex justify-center items-center text-base'})
    lista_cuotas = []
    lista_tuplas = []
    for cuota in cuotas:
        lista_cuotas.append(float(cuota.text))

    i = 0
    while len(lista_tuplas) < (len(lista_cuotas)/2):
        tupla = (lista_cuotas[i], lista_cuotas[i+1])
        lista_tuplas.append(tupla)
        i += 2

    equipos = soup.find_all('span', {'class': 'font-medium w-full lg:w-1/2 text-center dark:text-white'})
    lista_equipos = []
    for equipo in equipos:
        equipo_basket = equipo.find('a').text
        equipo_basket = equipo_basket[1:-1].split('-')
        lista_equipos.append(tuple(equipo_basket))

    diccionario = {}
    for i in range(len(lista_tuplas)):
        diccionario[lista_equipos[i]] = lista_tuplas[i]
    return diccionario

def load(diccionario):
    for partido in diccionario:
        apuestas = diccionario[partido]
        apuesta_min = min(diccionario[partido])
        if apuesta_min == diccionario[partido][0]:
            ganador = partido[0]
        else:
            ganador = partido[1]

        print(f'El partido {partido[0]} contra {partido[1]} tiene las apuestas {apuestas}. El ganador será {ganador}')


if __name__ == '__main__':
    datos = extract()
    diccionario = transform(datos)
    load(diccionario)


