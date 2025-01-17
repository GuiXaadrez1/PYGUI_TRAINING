from tkinter import Tk # class
from tkinter import ttk # módulo da classe

# matetializando a class TK()
tela = Tk()

# adcionando títulos na janela
tela.title("Minha Janela")

# adcionando um icon
# passe o caminho do arquivo.icon para colocar o icon na janela
# caso o icon esteja na mesma pasta, passe apenas o nome com a extensão
tela.iconbitmap("icons8-knight-shield-32.ico")

# Dimensionamento da janela, o método geometry serve para isso
# Aqui você vai passar um string widthxhight em pixels
# width -> largura
# higth -> altura
tela.geometry("300x300") 
# com geometry realizamos um padrão inicial que a janela vai ter
# isso não impede do usuário aumentar ou diminuir a janela

# caso queiramos limitar o tamanho máximo da janela, pode usar o método wm_maxsize
# ele recebe parâmetros de largura e altura

#tela.wm_maxsize(300,300)

# podemos usar o método wm_minsize para limitar até onde o usuário pode diminuir
# tamanho mínimo da janela

#tela.wm_minsize(150,150)

# Caso queira realmente proibir o usuário de dimensionar a tela e deixar ela padrão
# do método geometry podemos usar outro método em conjunto que é o método resizable
tela.resizable(False,False)
# esse método desabilita o dimensionamento das janelas, primeior para largura depois para altura
# False desabilita e True habilita 

# o método maxsize também serve porém utilize a anterior

# label é uma descrição
# o método place é onde vamos posicionar o elemento label
# o arg x -> horizontal em pixels
# o arg y -> vertigal em pixels
lb1 = ttk.Label(text="Primeira Label realizada com PYGUI").place(x = 10, y = 20 )

# podemos utilizar o grid
# os args do grid em relação a posição é row e colums

# grid não achei interessante usar
#lb2 = ttk.Label(text="Usando grid").grid(row= 200, column= 5000)

tela.mainloop() # irá abrir a janela


