import imprimir
import bbcwebscrapper  # https://www.bbc.com/news/world
from tkinter import *

def sendUrl():
    url = url_entry.get()
    bbcwebscrapper.BBCWebScrapper(url)


janela = Tk()
janela.title("Webscrapper de Notícias")
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


botao_arquivo = Button(janela, text="Gerar Arquivo", command=sendUrl)
botao_arquivo.configure(background='#efe4b1')
botao_arquivo.place(relx=0.4,rely=0.5)

botao_imprimir = Button(janela, text="Imprimir", command=imprimir.Imprimir)
botao_imprimir.configure(background='#efe4b1', highlightbackground='#b1efe6', highlightthickness=2)
botao_imprimir.place(relx=0.43,rely=0.63)

janela.mainloop()