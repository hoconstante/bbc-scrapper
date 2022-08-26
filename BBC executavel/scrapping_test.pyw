import win32print 
import win32api
import requests
from bs4 import BeautifulSoup
import os
from tkinter import *


def Imprimir():
    lista_impressoras = win32print.EnumPrinters(2)
    #for impressora in lista_impressoras:
    #    print(impressora)
    impressora = lista_impressoras[4]

    win32print.SetDefaultPrinter(impressora[2])
    caminho = "projeto-1"
    arquivo = "noticias_lista.txt"
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

def BBCWebScrapper():
    # https://www.bbc.com/news/world
  #  url = input("insira o URL: ")
    url = url_entry.get()
    url_print = 'URL -' + url + '\n' + '\n'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.105 Safari/537.36 Vivaldi/5.4.2753.40" }

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    noticias = soup. find_all('div', class_='gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--flex gs-u-mt@xs gs-u-mt0@xs gs-u-mt@m gel-1/2@xs gel-1/1@s')

    # noticia = noticias[0]
    if os.path.exists("noticias_lista.txt"):
        os.remove("noticias_lista.txt")

    with open  ('noticias_lista.txt', 'a', newline='', encoding = 'UTF-8') as f:
        f.write(url_print)
        for noticia in noticias : 
            title = noticia.find('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor').get_text()
            text = noticia.find('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m').get_text()
            value = title + ' - ' + text + '\n'+ '\n'        
            f.write(value) 


janela = Tk()
janela.title("BBC News Webscrapper")
janela.configure(background='#1e3743', highlightbackground='white', highlightthickness=3, highlightcolor='white')
janela.geometry("400x300+760+180")
janela.resizable(False,  False)  
#janela.resizable(True, True)
#janela.maxsize(width= 900, height= 700)
#janela.minsize(width=400, height=300)


frame_1 = Frame(janela)
frame_1.configure(background='#d9d8da', highlightbackground='#adc1c9', highlightthickness=3,highlightcolor='#adc1c9')
frame_1.place(relx=0.1,rely=0.2, relwidth=0.8,relheight=0.2)


texto_url = Label(janela, text="Insira a URL no campo abaixo", font='Calibri, 11')
texto_url.configure(background='#1e3743', foreground='white')
texto_url.place(relx=0.24,rely=0.1)


url_entry = Entry(frame_1)
url_entry.configure(background='#d9d8da', selectbackground='black', selectforeground='white')
url_entry.place(relx=0,rely=0, relwidth=1,relheight=1)


botao_arquivo = Button(janela, text="Gerar Arquivo", command=BBCWebScrapper)
botao_arquivo.configure(background='#efe4b1')
botao_arquivo.place(relx=0.4,rely=0.5)

botao_imprimir = Button(janela, text="Imprimir", command=Imprimir)
botao_imprimir.configure(background='#efe4b1', highlightbackground='#b1efe6', highlightthickness=2)
botao_imprimir.place(relx=0.43,rely=0.63)

janela.mainloop()