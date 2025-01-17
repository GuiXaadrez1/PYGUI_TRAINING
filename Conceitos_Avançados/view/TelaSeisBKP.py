from tkinter import Tk # importando a classe TK do pacote tkinter
from tkinter import Frame # importando a classe Frame do pacote tkinter para fazer conteiners
from tkinter import Button # importando a class Button do pacote tkinter para criação de botoes 
from tkinter import Label # importando a classe Label do pacote tkinter para criação de Labels
from tkinter import Entry # importando a classe Entry do pacote tkinter para criação de inputs
#from tkinter import tix # esse é um sub-módulo do tkinter para criarmos balão de aviso
# colocando bordas redondas no frame e no botões com awesometkinter
import awesometkinter as atk # vai ser necessário renomear os frames que tem a class Frame

class TelaQuatro():
    
    def __init__(self): # método construtor
        self.janela_main = Tk() #instanciando a classe TK() através do módulo tix
        self.config_janela() # método de configuração da janela
        self.config_frames() # método de configuração das Frames
        self.widgets_frame_1() # método de widgets do primeiro Frame
        self.janela_main.mainloop() # método do tkinter para abrir janela

    def config_janela(self):
        self.janela_main.title("Automatizador de Relatório")
        self.janela_main.iconbitmap(r"C:\PYGUI_TRAINING\Conceitos_Avançados\view\Grupo-3.ico")
        self.janela_main.configure(background='#FFF')
        self.janela_main.geometry("400x300")
        self.janela_main.resizable(False, False)
    
    def config_frames(self):
        self.frame_1 = atk.Frame3d(self.janela_main, bg='#f6cd34')
        self.frame_1.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.95)

    def widgets_frame_1(self):
        lb_1 = Label(self.frame_1, text="DIGITE O DO NOME GRUPO DO AGENTE:", bg="#252520", fg="#fff", font=("Arial", 9, 'bold'))
        lb_1.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.1)

        self.et_1 = Entry(self.frame_1, font=("Arial", 9), fg="gray")
        self.et_1.place(relx=0.15, rely=0.30, relwidth=0.7, relheight=0.1)
        self.et_1.insert(0, "Exemplo: DER")  # Placeholder inicial
        self.et_1.bind("<FocusIn>", self.remove_placeholder_et_1)
        self.et_1.bind("<FocusOut>", self.add_placeholder_et_1)

        lb_2 = Label(self.frame_1, text="DIGITE O NOME DO AGENTE:", bg="#252520", fg="#fff", font=("Arial", 9, 'bold'))
        lb_2.place(relx=0.24, rely=0.46, relwidth=0.5, relheight=0.1)

        self.et_2 = Entry(self.frame_1, font=("Arial", 9), fg="gray")
        self.et_2.place(relx=0.15, rely=0.60, relwidth=0.7, relheight=0.1)
        self.et_2.insert(0, "Exemplo: DER_MULTAS_SENHA")  # Placeholder inicial
        self.et_2.bind("<FocusIn>", self.remove_placeholder_et_2)
        self.et_2.bind("<FocusOut>", self.add_placeholder_et_2)

        bt_buscar = Button(self.frame_1, text="Buscar", bd=4, font=("Arial", 9, "bold"), fg="#000", command=self.confirmar)
        bt_buscar.place(relx=0.37, rely=0.8, relwidth=0.2, relheight=0.15)
    
    # Funções para placeholder no Entry 1
    def remove_placeholder_et_1(self, event):
        if self.et_1.get() == "Exemplo: DER":
            self.et_1.delete(0, "end")
            self.et_1.config(fg="black")

    def add_placeholder_et_1(self, event):
        if not self.et_1.get():
            self.et_1.insert(0, "Exemplo: DER")
            self.et_1.config(fg="gray")

    # Funções para placeholder no Entry 2
    def remove_placeholder_et_2(self, event):
        if self.et_2.get() == "Exemplo: DER_MULTAS_SENHA":
            self.et_2.delete(0, "end")
            self.et_2.config(fg="black")

    def add_placeholder_et_2(self, event):
        if not self.et_2.get():
            self.et_2.insert(0, "Exemplo: DER_MULTAS_SENHA")
            self.et_2.config(fg="gray")

    def confirmar(self):
        try:
            valor_et_1 = self.et_1.get().strip()
            valor_et_2 = self.et_2.get().strip()

            # Verifica se os campos possuem os placeholders ou estão vazios
            if not valor_et_1 or valor_et_1 == "Digite o nome do grupo" or not valor_et_2 or valor_et_2 == "Digite o nome do agente":
                print("Coloque os dados corretamente.")
            else:
                print(f"O Grupo é: {valor_et_1} e o Agente é: {valor_et_2}")
                self.janela_main.destroy()
                return f"O Grupo é: {valor_et_1} e o Agente é: {valor_et_2}"

        except Exception as e:
            print(f"Aconteceu algum erro: {e}")

if __name__ == "__main__":
    tela_main = TelaQuatro()