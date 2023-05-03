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
        if self.verificador:
            print(u'Antes de prosseguir, verifique como está o nome do bairro no site do Infoimóveis :)\n')
            while True:
                self.input_bairro()
                if self.bairro in self.bairros: 
                    print('Bairro encontrado!\n')
                    break
                else: print(u'Bairro não encontrado!\nPor favor, verifique o nome do bairro e tente novamente.\n')

    def get_local(self):
        if self.verificador: return self.bairro
        else: return self.city
 

class PegaURL():
    def __init__(self, local):
        self.local_link = self.adequa_p_link(local)

    def adequa_p_link(self, value):
            value_link = value.replace(" ",'-')
            return value_link

local = VerificadorLocal().get_local()
PegaURL(local).local_link