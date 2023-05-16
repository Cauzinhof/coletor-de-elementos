from urllib.request import Request, urlopen
import urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import simplekml

class VerificadorLocal:
    def __init__(self):
        self.input_cidade()
        self.lista_bairros_cidades()
        self.verifica_cidade()
        self.verifica_bairro()

    def lista_bairros_cidades(self):
        with open('cidades.txt', 'r') as arquivo:
            self.cidades= [i.rstrip('\n') for i in arquivo]
        with open('bairros.txt', 'r') as arquivo:
            self.bairros= [i.rstrip('\n') for i in arquivo]

    def input_cidade(self):
        self.city = self.limpa_input(input('Insira a cidade: '))

    def input_bairro(self):
        self.bairro = self.limpa_input(input('Insira o bairro: '))

    def limpa_input(self, value):
        return value.lower().strip()

    def verifica_cidade(self):
        while True:
            if self.city in self.cidades: 
                print('Cidade encontrada!\n')
                break
            else: 
                print(u'Cidade não encontrada!\nPor favor, verifique o nome da cidade e tente novamente.\n')
                self.input_cidade()
        self.verificador = self.city == 'campo grande'

    def verifica_bairro(self):
        if self.verificador: #Se a cidade for Campo Grande, a pesquisa será feita por bairro
            print(u'Antes de prosseguir, verifique como está o nome do bairro no site do Infoimóveis :)\n')
            while True:
                self.input_bairro()
                if self.bairro in self.bairros: 
                    print('Bairro encontrado!\n')
                    break
                else: print(u'Bairro não encontrado!\nPor favor, verifique o nome do bairro e tente novamente.\n')

    def get_local(self):
        if self.verificador: return (self.bairro, self.verificador)
        else: return (self.city, self.verificador)
 
class PegaURL:
    def __init__(self, tupla_local):
        self.local, self.verificador = tupla_local
        self.local_link = self.adequa_p_link(self.local)
        self.ignorar_erros()
        self.gera_links()

    def adequa_p_link(self, value):
            value_link = value.replace(" ",'-')
            return value_link

    def ignorar_erros(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    def coletahtml(self, url):
        req=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req,timeout=10).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def gera_links(self):
        self.links = []
        for page in range(1,6): # Coletar todas as anchor tags da pg de pesquisa
            if self.verificador:
                url = 'https://www.infoimoveis.com.br/busca/venda/terreno/ms/campo-grande/'+self.local_link+'?pagina='+str(page)
            else:
                url = 'https://www.infoimoveis.com.br/busca/venda/terreno/ms/'+self.local_link+'?pagina='+str(page)
            soup = self.coletahtml(url)
            hrefs = soup('a')
            for tag in hrefs:
                href = tag.get('href', None)
                if 'venda-terreno' in href and href not in self.links: #Filtrar apenas as tags com link de venda de terreno
                    self.links.append(href)
        if len(self.links): 
            print('Verificando terrenos em '+self.local.title()+'. Por favor, aguarde...\n')
        else:
            print(u'Poxa! Não há elementos com localização para coleta nesse lugar. Boa sorte =/.')
            #quit()

    def __getitem__ (self, key):
        return self.links[key]

class Coletor:
    def __init__(self, links:list):
        self.links = []
        for i in links:
            self.links.append(i)
        self.dados = {'Area (m2)': [], 'Valor':[], 'Localizacao':[], 'Link':[]} #Criando o DF
        self.coleta_parametros()
        if len(self.dados['Link']): 
            print('Elementos coletados!\n')
        else:
            print(u'Poxa! Não há elementos com localização para coleta nesse lugar. Boa sorte =/.')

    def coletahtml(self, url):
        req=Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req,timeout=10).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_area(self, html):
        html = html.find_all('td')
        area = '0'
        for i in html:
            i=str(i)
            if ' m²' in i:
                area = i.lstrip('<td>').rstrip(' m²</td>')
                break
        self.dados['Area (m2)'].append(area)

    def get_valor(self, html):
        html = html.find_all('span')
        for i in html:
            i=str(i)
            if i != None and 'R$' in i:
                valor = i.lstrip('<span class="valor">').rstrip('</span>')
                break
        self.dados['Valor'].append(valor)

    def get_linkloc(self, tags, url):
        loc = None
        for i in tags:
            if i.get('onclick') == None: continue
            if 'posiciona' in i.get('onclick'):
                loc = i.get('onclick').split('(')[1]
                loc = loc[:len(loc)-1]
                break
        if loc:
            self.dados['Link'].append(url)
            self.dados['Localizacao'].append(loc)
        return loc
    
    def coleta_parametros(self):
        for url in self.links:
            html=self.coletahtml(url)
            tags = html.find_all('button')
            loc = self.get_linkloc(tags, url)

            if loc:
                self.get_area(html)
                self.get_valor(html)
    
class GeradorDeArquivos:
    def __init__(self, tupla_local, dados):
        self.local, self.verificador = tupla_local
        self.dados = dados
        if len(self.dados['Link']):
            self.gera_kml()
            self.gera_xlsx()

    def gera_kml(self):
        index = 1
        kml=simplekml.Kml()
        for item in self.dados['Localizacao']:
            item=item.split(',')
            lat=item[0]
            lon = item[1]
            kml.newpoint(name=index, coords=[(lon,lat)])
            index += 1   
        kml.save('Elementos '+self.local.title()+'.kml')

    def gera_xlsx(self):
        df = pd.DataFrame(self.dados)
        df.index += 1
        df.to_excel('Elementos '+self.local.title()+'.xlsx',index_label='#')

def header():
    print('*********************************************')
    print('******Desenvolvido por Carlos Fernandes******')
    print('*********************************************\n')
    print(u'Para usar esta aplicação, não use acentos ou cedilha!\n')

def finaliza():
    while True:
        if input('Pressione Enter para sair') != None : break #Finalização

header()
local = VerificadorLocal().get_local()
links = PegaURL(local)
coleta = Coletor(links)
GeradorDeArquivos(local, coleta.dados)
finaliza()