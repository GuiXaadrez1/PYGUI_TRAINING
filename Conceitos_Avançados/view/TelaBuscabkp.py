from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
import awesometkinter as atk
import sys
import os

class TelaBusca():
    
    def __init__(self):
        self.janela_main = Tk()
        self.config_janela()
        self.config_frames()
        self.widgets_frame_1()
        self.janela_main.mainloop()

    def config_janela(self):
        self.janela_main.title("Automatizador de Relatório")
        self.janela_main.iconbitmap(os.path.join(os.getcwd(),"Conceitos_Avançados","view","Grupo-3.ico"))
        self.janela_main.configure(background='#000')
        self.janela_main.geometry("400x300")
        self.janela_main.resizable(False, False)
    
    def config_frames(self):
        self.frame_1 = atk.Frame3d(self.janela_main, bg='#f6cd34')
        self.frame_1.place(relx= 0.05 ,rely = 0.07, relwidth= 0.9, relheight = 0.85)

    def widgets_frame_1(self):
        lb_1 = Label(self.frame_1, text="DIGITE O NOME DO GRUPO DO AGENTE", bg="red", fg="#fff", font=("Arial", 11, 'bold'))
        lb_1.place(relx=0.08, rely=0.15, relwidth=0.85, relheight=0.1)

        self.et_1 = Entry(self.frame_1, font=("Arial", 12), fg="gray")
        self.et_1.place(relx=0.15, rely=0.30, relwidth=0.7, relheight=0.1)
        self.et_1.insert(0, "Exemplo: DER")
        self.et_1.bind("<FocusIn>", self.remove_placeholder_et_1)
        self.et_1.bind("<FocusOut>", self.add_placeholder_et_1)

        lb_2 = Label(self.frame_1, text="DIGITE O NOME DO AGENTE", bg="red", fg="#fff", font=("Arial", 11, 'bold'))
        lb_2.place(relx=0.2, rely=0.46, relwidth=0.61, relheight=0.1)

        self.et_2 = Entry(self.frame_1, font=("Arial", 12), fg="gray")
        self.et_2.place(relx=0.15, rely=0.60, relwidth=0.7, relheight=0.1)
        self.et_2.insert(0, "Exemplo: DER_MULTAS_SENHA")
        self.et_2.bind("<FocusIn>", self.remove_placeholder_et_2)
        self.et_2.bind("<FocusOut>", self.add_placeholder_et_2)

        bt_buscar = Button(self.frame_1, text="Buscar", bd=4, font=("Arial", 9, "bold"), fg="#000", command=self.confirmar)
        bt_buscar.place(relx=0.37, rely=0.8, relwidth=0.2, relheight=0.15)
    
    def remove_placeholder_et_1(self, event):
        if self.et_1.get() == "Exemplo: DER":
            self.et_1.delete(0, "end")
            self.et_1.config(fg="black")

    def add_placeholder_et_1(self, event):
        if not self.et_1.get():
            self.et_1.insert(0, "Exemplo: DER")
            self.et_1.config(fg="gray")

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
            self.valor_et_1 = self.et_1.get().strip()
            self.valor_et_2 = self.et_2.get().strip()

            if not self.valor_et_1 or self.valor_et_1 == "Exemplo: DER" or not self.valor_et_2 or self.valor_et_2 == "Exemplo: DER_MULTAS_SENHA":
                messagebox.showwarning("Aviso", "Por favor, preencha os campos corretamente.")
                            
            elif self.valor_et_1 == "Exemplo: DER" and self.valor_et_2 == "Exemplo: DER_MULTAS_SENHA":
                messagebox.showwarning("Aviso", "Por favor, preencha os campos corretamente.")
            
            else:
                
                tela_confirm = messagebox.askyesno("CONFIRME PARA REALIZAR BUSCA!","Clique em 'sim' para confirmar e 'não' para cancelar.")
                
                if tela_confirm == True:
                    self.janela_main.destroy()
                    
                else: 
                    messagebox.showinfo("info","Busca cancelada!\nClique em 'ok' para finalizar o programa")
                    self.valor_et_1 = None
                    self.valor_et_2 = None
                    self.janela_main.destroy()
                    sys.exit(0)
        
        except Exception as e:
            print(f"Aconteceu algum erro: {e}")
            messagebox.showerror("Erro", f"Aconteceu um erro: {e}")

if __name__ == "__main__":
    
    tela_dw = TelaBusca()

    grupo = tela_dw.valor_et_1
    agente = tela_dw.valor_et_2

    #print(f"{grupo}, {agente}")

    if not grupo == "Exemplo: DER" and not agente == "Exemplo: DER_MULTAS_SENHA":
        messagebox.showinfo('info','Foi iniciada a busca do agente remotamente.')
    
    tela_data = TelaData()