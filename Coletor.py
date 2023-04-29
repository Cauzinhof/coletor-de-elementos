from urllib.request import Request, urlopen
import urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import simplekml

class Terreno:
    dados = {'Area (m2)': [], 'Valor':[], 'Localizacao':[], 'Link':[]} #Criando o DF

    def gera_kml(city):
        index = 1
        kml=simplekml.Kml()
        for item in Terreno.dados['Localizacao']:
            item=item.split(',')
            lat=item[0]
            lon = item[1]
            kml.newpoint(name=index, coords=[(lon,lat)])
            index += 1   
        if city == 'campo grande': kml.save('Elementos '+bairro.title()+'.kml')
        else: kml.save('Elementos '+city.title()+'.kml')

    def get_area(html):
        html = html.find_all('td')
        for i in html:
            i=str(i)
            if ' m²' in i:
                area = i.lstrip('<td>').rstrip(' m²</td>')
                break
        Terreno.dados['Area (m2)'].append(area)

    def get_valor(html):
        html = html.find_all('span')
        for i in html:
            i=str(i)
            if i != None and 'R$' in i:
                valor = i.lstrip('<span class="valor">').rstrip('</span>')
                break
        Terreno.dados['Valor'].append(valor)
    
    def get_linkloc(tags):
        loc = None
        for i in tags:
            if i.get('onclick') == None: continue
            if 'posiciona' in i.get('onclick'):
                loc = i.get('onclick').split('(')[1]
                loc = loc[:len(loc)-1]
                break
        if loc != None:
            Terreno.dados['Link'].append(url)
            Terreno.dados['Localizacao'].append(loc)
        return loc

# Ignorar erros de certificado SSL

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#comunicar com o site

def coletahtml(url):

    req=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req,timeout=10).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def adequa_p_link(value):
    aux = value.split()
    value_link=''
    for i in aux:
        value_link += i + '-'
    value_link = value_link.rstrip('-')
    return value_link

def header():
    print('##########################################')
    print('\n\n   Desenvolvido por Carlos Fernandes\n\n')
    print('##########################################\n')
    print(u'Para usar esta aplicação, não use acentos ou cedilha!\n')

with open('cidades.txt', 'r') as arquivo:
    cidades= [i.rstrip('\n') for i in arquivo]

with open('bairros.txt', 'r') as arquivo:
    bairros= [i.rstrip('\n') for i in arquivo]

header()

while True:
    city = input('Insira a cidade: ').lower()
    cidade_link = adequa_p_link(city)
    if city in cidades: 
        print('Cidade encontrada! Por favor aguarde enquanto coleto os elementos para você\n')
        break
    else: print(u'Cidade não encontrada!\nPor favor, verifique o nome da cidade e tente novamente.\n')

#Se a cidade for Campo Grande, a pesquisa será feita por bairro
if city == 'campo grande':
    print(u'Antes de prosseguir, verifique como está o nome do bairro no site do Infoimóveis :)\n')
    while True:
        bairro = input('Insira o bairro: ').lower()
        bairro_link = adequa_p_link(bairro)        
        if bairro in bairros: 
            print('Bairro encontrado! Por favor aguarde enquanto coleto os elementos para você\n')
            break
        else: print(u'Bairro não encontrado!\nPor favor, verifique o nome do bairro e tente novamente.\n')

# Coletar todas as anchor tags da pg de pesquisa
links = []
for page in range(1,6):
    if city == 'campo grande':
        url = 'https://www.infoimoveis.com.br/busca/venda/terreno/ms/campo-grande/'+bairro_link+'?pagina='+str(page)
    else:
        url = 'https://www.infoimoveis.com.br/busca/venda/terreno/ms/'+cidade_link+'?pagina='+str(page)
    soup = coletahtml(url)
    hrefs = soup('a')
 
    #Filtrar apenas as tags com link de venda de terreno
    for tag in hrefs:
        #print(tag.get('href', None))
        if 'venda-terreno' in tag.get('href', None):
            if tag.get('href', None) not in links:
                links.append(tag.get('href', None))

if links != []:
    print('Coletando terrenos em '+city.title()+'. Por favor, aguarde...\n')
        
        #Aqui coletaremos a localização dos links extraídos
    for l in links:
        url = l
        tags = coletahtml(url).find_all('button')
        loc = Terreno.get_linkloc(tags)

            #Aqui coletaremos a area e o valor
        if loc != None:
            infoimovel = coletahtml(url)
            Terreno.get_area(infoimovel)
            Terreno.get_valor(infoimovel)
            
        #Criando o dataframe e salvando como .xlsx        
    df = pd.DataFrame(Terreno.dados)
    df.index += 1
    if city == 'campo grande': df.to_excel('Elementos '+bairro.title()+'.xlsx',index_label='#')
    else: df.to_excel('Elementos '+city.title()+'.xlsx',index_label='#')
        
    Terreno.gera_kml(city)     

    print('Elementos coletados\nArquivos EXCEL e KML salvos na pasta\nObrigado!\n')

else: print(u'Poxa! Não há elementcos para coleta nesse lugar. Boa sorte =/.')
    
while True:
    if input('Pressione Enter para sair') != None : break #Finalização