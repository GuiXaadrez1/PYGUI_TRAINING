# vamos usas tkinter, é uma lib que já vem embutida no python
from tkinter import Tk # class
from tkinter import ttk # módulo da classe

# matetializando a class TK()
tela = Tk()

# label é uma descrição
# o método place é onde vamos posicionar o elemento label
# o arg x -> horizontal em pixels
# o arg y -> vertigal em pixels
lb1 = ttk.Label(text="Primeira Label realizada com PYGUI").place(x = 700, y = 360 )

tela.mainloop() # irá abrir a janela