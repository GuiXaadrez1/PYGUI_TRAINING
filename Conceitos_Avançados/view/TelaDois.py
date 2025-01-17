# Aqui é uma continuação da telaUm
from tkinter import Tk # importando a classe TK
from tkinter import Frame # importando a classe Frame para fazer conteiners
from tkinter import ttk # método 


# Aqui vamos trabalhar com os Frames da nossa classe
# Frames são as divisórias, são conteiner ou partes da Tela

# Janela busca
class TelaDois():
    
    # Método construtor para intanciar a classe em um objeto
    # Toda vez que o objeto for criado vai vir com as propriedades 
    # definidas dentro do construtor 
    
    def __init__(self): # método construtor
        self.janela_main = Tk() # instancia a class TK
        self.config_janela() # método de configuração da janela
        self.config_frames() # método de configuração das Frames
        self.janela_main.mainloop() # método do tkinter para abrir janela
    

    # método de configuração da janela
    def config_janela(self):
        # adicionando título na janela
        self.janela_main.title("Automatizador de Relatório")
        # adicionando icon na janela 
        self.janela_main.iconbitmap(r"C:\PYGUI_TRAINING\Conceitos_Avançados\view\icons8-knight-shield-32.ico")
        # colocando cor de fundo
        self.janela_main.configure(background='blue')
        # define tamanho da janela
        self.janela_main.geometry("400x300")
        # ativa ou desativa modo responsivo 
        self.janela_main.resizable(False,False)

    # 
    def config_frames(self):
        self.frame_1 = Frame(self.janela_main)
        # usando o método place com relx, rely, relwidth e relhight
        # ele funicona com porcentagem
        self.frame_1.place(relx = 0.05, rely= 0.22, relwidth= 0.9, relheight= 0.3)
        self.frame_2 = Frame(self.janela_main)
        self.frame_2.place(relx = 0.05, rely= 0.62, relwidth= 0.9, relheight= 0.3)

if __name__ == "__main__":

    # instanciando a nossa classe TelaPrincipal
    tela_main = TelaDois()