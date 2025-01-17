from tkinter import Tk # class
from tkinter import ttk # módulo da classe

# Vamos adcionar títulos e icon personalizado


# matetializando a class TK()
tela = Tk()

# adcionando títulos na janela
tela.title("Minha Janela")

# passe o caminho do arquivo.icon para colocar o icon na janela
# caso o icon esteja na mesma pasta, passe apenas o nome com a extensão
tela.iconbitmap("icons8-knight-shield-32.ico")

# label é uma descrição
# o método place é onde vamos posicionar o elemento label
# o arg x -> horizontal em pixels
# o arg y -> vertigal em pixels
lb1 = ttk.Label(text="Primeira Label realizada com PYGUI").place(x = 700, y = 360 )

# podemos utilizar o grid
# os args do grid em relação a posição é row e colums

# grid não achei interessante usar
lb2 = ttk.Label(text="Usando grid").grid(row= 200, column= 5000)

tela.mainloop() # irá abrir a janela


