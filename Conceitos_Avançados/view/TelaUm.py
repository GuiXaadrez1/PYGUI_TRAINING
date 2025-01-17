from tkinter import Tk # importando a classe
from tkinter import ttk # método 

# janela de busca

class TelaUm():
    
    # Método construtor para intanciar a classe em um objeto
    # Toda vez que o objeto for criado vai vir com as propriedades 
    # definidas dentro do construtor 
    
    def __init__(self): # método construtor
        self.janela_main = Tk() # instancia a class TK
        self.config_janela() # método de configuração da janela
        self.janela_main.mainloop() # método do tkinter para abrir janela
    

    # método de configuração da janela
    def config_janela(self):
        # adciona título na janela
        self.janela_main.title("Automatizador de Relatório")
        # define tamanho da janela
        self.janela_main.geometry("400x300")
        # ativa ou desativa modo responsivo 
        self.janela_main.resizable(False,False)


if __name__ == "__main__":

    # instanciando a nossa classe TelaPrincipal
    tela_main = TelaUm()