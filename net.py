from urllib.request import Request, urlopen
import urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import simplekml

class Coletor:
    def __init__(self, city):
        self.city=self.limpa_input(city)
        self.lista_bairros_cidades()

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
                print('Cidade encontrada! Por favor aguarde enquanto coleto os elementos para você\n')
                break
            else: 
                print(u'Cidade não encontrada!\nPor favor, verifique o nome da cidade e tente novamente.\n')
                self.input_cidade()
        self.verificador = self.city == 'campo grande'

    def verifica_bairro(self):
        print(u'Antes de prosseguir, verifique como está o nome do bairro no site do Infoimóveis :)\n')
        if self.verificador:
            while True:
                self.input_bairro()
                if self.bairro in self.bairros: 
                    print('Bairro encontrado! Por favor aguarde enquanto coleto os elementos para você\n')
                    break
                else: print(u'Bairro não encontrado!\nPor favor, verifique o nome do bairro e tente novamente.\n')

    def adequa_p_link(value):
        aux = value.split()
        value_link=''
        for i in aux:
            value_link += i + '-'
        value_link = value_link.rstrip('-')
        return value_link