# Aqui é uma continuação da TelaUm e TelaDois

from tkinter import Tk # importando a classe TK
from tkinter import Frame # importando a classe Frame para fazer conteiners
from tkinter import Button # importando a class Button para criação de botoes 

# colocando bordas redondas no frame e no botões com awesometkinter
import awesometkinter as atk # vai ser necessário renomear os frames que tem a class Frame


# Aqui vamos trabalhar com os Frames da nossa classe
# Frames são as divisórias, são conteiner ou partes da Tela

# Janela busca
class TelaTres():
    
    # Método construtor para intanciar a classe em um objeto
    # Toda vez que o objeto for criado vai vir com as propriedades 
    # definidas dentro do construtor 
    
    def __init__(self): # método construtor
        self.janela_main = Tk() # instancia a class TK
        self.config_janela() # método de configuração da janela
        self.config_frames() # método de configuração das Frames
        self.botao_buscar() # método de criação de botão
        self.janela_main.mainloop() # método do tkinter para abrir janela
    

    # método de configuração da janela
    def config_janela(self):
        # adicionando título na janela
        self.janela_main.title("Automatizador de Relatório")
        # adicionando icon na janela 
        self.janela_main.iconbitmap(r"C:\PYGUI_TRAINING\Conceitos_Avançados\view\icons8-knight-shield-32.ico")
        # colocando cor de fundo
        self.janela_main.configure(background='#ADD7FF')
        # define tamanho da janela
        self.janela_main.geometry("400x300")
        # ativa ou desativa modo responsivo 
        self.janela_main.resizable(False, False)

    
    # Criando Frames
    
    def config_frames(self):
        # Materializando a Classe Frame para criar conteiner da nossa janela
        self.frame_1 = atk.Frame3d(self.janela_main, bg='#fff')
        # usando o método place com relx, rely, relwidth e relhight
        # ele funicona com porcentagem
        self.frame_1.place(relx = 0.05, rely= 0.10, relwidth= 0.9, relheight= 0.5)
        self.frame_2 = Frame(self.janela_main, bd = 2, bg = "#fff", highlightbackground="#000", highlightthickness= 3, )
        self.frame_2.place(relx = 0.05, rely= 0.62, relwidth= 0.9, relheight= 0.3)

    # Método para a criação das funções
    def botao_buscar(self):
        # puxando o atributo do método config_frames e colocando dentro da class Button como arg
        bt_buscar = Button(self.frame_1, text="Buscar")
        # posicionando o botão dentro do Frame
        bt_buscar.place(relx = 0.35,rely = 0.60, relwidth = 0.3, relheight = 0.25)

        bt_limpar = Button(self.frame_2,text="Limpar")
        bt_limpar.place(relx= 0.35, rely= 0.60, relwidth = 0.3, relheight = 0.25)

if __name__ == "__main__":

    # instanciando a nossa classe TelaPrincipal
    tela_main = TelaTres()