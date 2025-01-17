# Aqui é uma continuação da TelaUm, TelaDois, TelaTres, TelaQuatro

from tkinter import Tk # importando a classe TK do pacote tkinter
from tkinter import Frame # importando a classe Frame do pacote tkinter para fazer conteiners
from tkinter import Button # importando a class Button do pacote tkinter para criação de botoes 
from tkinter import Label # importando a classe Label do pacote tkinter para criação de Labels
from tkinter import Entry # importando a classe Entry do pacote tkinter para criação de inputs

# colocando bordas redondas no frame e no botões com awesometkinter
import awesometkinter as atk # vai ser necessário renomear os frames que tem a class Frame
# esse pacote awesometkinter é um lib que precisa ser instalada

# Aqui vamos trabalhar com a estilização de widgets

class TelaCinco():
    
    # Método construtor para intanciar a classe em um objeto
    # Toda vez que o objeto for criado vai vir com as propriedades 
    # definidas dentro do construtor 
    
    def __init__(self): # método construtor
        self.janela_main = Tk() # instancia a class TK
        self.config_janela() # método de configuração da janela
        self.config_frames() # método de configuração das Frames
        self.widgets_frame_1() # método de widgets do primeiro Frame
        self.janela_main.mainloop() # método do tkinter para abrir janela
    

    # método de configuração da janela
    def config_janela(self):
        # adicionando título na janela
        self.janela_main.title("Automatizador de Relatório")
        # adicionando icon na janela 
        self.janela_main.iconbitmap(r"C:\PYGUI_TRAINING\Conceitos_Avançados\view\Grupo-3.ico")
        # colocando cor de fundo na janela
        self.janela_main.configure(background='#FFF')
        # define tamanho da janela
        self.janela_main.geometry("400x300")
        # ativa ou desativa modo responsivo 
        self.janela_main.resizable(False, False)

    
    # Criando Frames
    
    def config_frames(self):
        
        # Materializando a Classe Frame para criar conteiner da nossa janela
        self.frame_1 = atk.Frame3d(self.janela_main, bg='#f6cd34') # deixando o Frame redeondo dentro da janela_main
        # usando o método place com relx, rely, relwidth e relhight
        # ele funicona com porcentagem
        self.frame_1.place(relx = 0.05, rely= 0.02, relwidth= 0.9, relheight= 0.95)

    # Método para a criação das funções
    
    def widgets_frame_1(self):
        
        # materializando a classe Label e fazendo Label Título
         # o arg fg muda a cor do texto
        # o arg font colocamos o nome da fonte em string como primeiro valor e o tamanho da fonte como segundo valor, depois a estilização dela em string
        lb_1 = Label(self.frame_1, text="DIGITE O DO NOME GRUPO DO AGENTE:", bg="#252520", fg = "#fff", font=("Arial",9 , 'bold'))
        lb_1.place(relx = 0.15, rely= 0.15, relwidth= 0.7, relheight= 0.1)
        
        # Label de exemplo
        #lb_ex_1 = Label(self.frame_1, text="Exemplo: DER", bg="#fff")
        #lb_ex_1.place(relx = 0.05, rely= 0.2, relwidth= 0.9, relheight= 0.1)
        
        # materializando a classe Entry
        et_1 = Entry(self.frame_1, font=("Arial",9))
        et_1.place(relx = 0.15, rely= 0.30, relwidth= 0.7, relheight= 0.1 )
        # esse método coloca placeholder no campo de texto, porém ele insere um texto inicial dentro do campo
        et_1.insert(0, string = " Exemplo: DER")
        
        
        # Fazendo Label Titulo 2
        lb_2 = Label(self.frame_1, text="DIGITE O NOME DO AGENTE:", bg="#252520", fg = "#fff", font=("Arial",9 , 'bold'))
        lb_2.place(relx = 0.24, rely= 0.46, relwidth= 0.5, relheight= 0.1)
        
        # Label de exemplo
        #lb_ex_2 = Label(self.frame_1, text="Exemplo: DER", bg="#fff")
        #lb_ex_2.place(relx = 0.05, rely= 0.2, relwidth= 0.9, relheight= 0.1)
        
        # materializando a classe Entry
        et_2 = Entry(self.frame_1, font=("Arial",9))
        et_2.place(relx = 0.15, rely= 0.60, relwidth= 0.7, relheight= 0.1)
        et_2.insert(0," Exemplo: DER_MULTAS_SENHA")
        
        '''
        # puxando o atributo do método config_frames e colocando dentro da class Button3d como arg
        bt_buscar = atk.Button3d(self.frame_1, text="Buscar",bg="#b0abab")
        # posicionando o botão dentro do Frame
        bt_buscar.place(relx = 0.35,rely = 0.8, relwidth = 0.2, relheight = 0.15)
        '''
        # VOLTANDO A USAR A FORMA PADRÃO DO BOTÃO
        # o arg bd é a forma do botão o tipo do botão
        bt_buscar = Button(self.frame_1, text="Buscar", bd = 4, font=("Arial",9, "bold"), fg = "#000")
        # posicionando o botão dentro do Frame
        bt_buscar.place(relx = 0.37,rely = 0.8, relwidth = 0.2, relheight = 0.15)

if __name__ == "__main__":

    # instanciando a nossa classe TelaPrincipal
    tela_main = TelaCinco()