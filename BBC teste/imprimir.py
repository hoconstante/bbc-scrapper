
import win32print
import win32api

def Imprimir():
    lista_impressoras = win32print.EnumPrinters(2)
    #for impressora in lista_impressoras:
    #    print(impressora)
    impressora = lista_impressoras[4]

    win32print.SetDefaultPrinter(impressora[2])
    caminho = "projeto-1"
    arquivo = "noticias_lista.txt"
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
