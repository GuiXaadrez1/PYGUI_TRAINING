# Vamos colocar widgest na janela

from tkinter import Tk # class
from tkinter import ttk # módulo da classe

# materializando a class TK()
janela = Tk()

# adcionando títulos na janela
janela.title("Minha Janela")

# adcionando um icon
janela.iconbitmap("icons8-knight-shield-32.ico")

# Dimensionamento inicial da janela
# porém o usuário pode dimensionar com liberdade
janela.geometry("300x300") 

# limitando o tamanho máximo a ser dimensionado
#tela.wm_maxsize(300,300)

# limitando o tamanho mínimo a ser dimensionado
#tela.wm_minsize(150,150)

# Desabilitando dimensionamento
janela.resizable(False,False)

# colocando background na janela
janela.configure(background='red')

# em blackground podemos usar nomes ou códigos das cores


# label é uma descrição
# o método place é onde vamos posicionar o elemento label
# o arg x -> horizontal em pixels
# o arg y -> vertigal em pixels
# o foregroung = cor do texto
lb1 = ttk.Label(text="Primeira Label realizada com PYGUI", foreground= 'blue').place(x = 10, y = 20 )

janela.mainloop() # irá abrir a janela


