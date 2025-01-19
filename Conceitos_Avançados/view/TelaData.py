from tkinter import Tk
from tkinter import ttk
from tkinter import Frame, Label, Button, Entry, messagebox
import awesometkinter as atk
import os
import sys

class TelaData:

    # definindo o método construtor
    def __init__(self):
        self.janela_main = Tk() # instancia a class TK
        self.config_janela() # configurações de janela
        self.frame() # frame e configurações de frame
        self.create_styles()  # Cria estilos personalizados
        self.widgets_frame1() # widgets e suas configurações
        self.janela_main.mainloop() # abre janela

    def config_janela(self):
        self.janela_main.title("Automatizador de Relatório")
        self.janela_main.iconbitmap(os.path.join(os.getcwd(), "Conceitos_Avançados", "view", "Grupo-3.ico"))
        self.janela_main.geometry("400x300")
        self.janela_main.configure(background="#000")
        self.janela_main.resizable(False, False)

    def frame(self):
        self.frame1 = atk.Frame3d(self.janela_main, bg='#f6cd34')
        self.frame1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

    def create_styles(self): # para o método tkk{} precisamos fazer funções para personalizar nossos wedgets
        # Criando estilos personalizados para os campos Entry
        self.style = ttk.Style()
        self.style.configure("Placeholder.TEntry", foreground="gray")
        self.style.configure("Default.TEntry", foreground="black")

    def widgets_frame1(self):
        lb_data_i = Label(self.frame1, text='DIGITE A DATA INICIAL', bg='red', fg='#fff', font=('Arial', 12, 'bold'))
        lb_data_i.place(relx=0.23, rely=0.15, relwidth=0.55, relheight=0.1)

        # Entry com placeholder
        self.et_data_i = ttk.Entry(self.frame1, font=("Arial", 12), justify='center', style="Placeholder.TEntry")
        self.et_data_i.place(relx=0.23, rely=0.3, relwidth=0.55, relheight=0.1)
        self.et_data_i.insert(0, "Exemplo: 01/01/2025")
        self.et_data_i.bind('<FocusIn>', self.remove_placeholder_data_i)
        self.et_data_i.bind('<FocusOut>', self.add_placeholder_data_i)

        lb_data_f = Label(self.frame1, text='DIGITE A DATA FINAL', bg='red', fg='#fff', font=('Arial', 12, 'bold'))
        lb_data_f.place(relx=0.23, rely=0.46, relwidth=0.55, relheight=0.1)

        self.et_data_f = ttk.Entry(self.frame1, font=("Arial", 12), justify='center', style="Placeholder.TEntry")
        self.et_data_f.place(relx=0.23, rely=0.6, relwidth=0.55, relheight=0.1)
        self.et_data_f.insert(0, "Exemplo: 31/01/2025")
        self.et_data_f.bind('<FocusIn>', self.remove_placeholder_data_f)
        self.et_data_f.bind('<FocusOut>', self.add_placeholder_data_f)
        

        self.bt_confirm_data = Button(self.frame1, text="Confirmar", bd=4, command=self.converter_data)
        self.bt_confirm_data.place(relx=0.39, rely=0.8, relwidth=0.2, relheight=0.15)

    def remove_placeholder_data_i(self, event):
        if self.et_data_i.get() == "Exemplo: 01/01/2025":
            self.et_data_i.delete(0, "end")
            self.et_data_i.config(style="Default.TEntry")

    def add_placeholder_data_i(self, event):
        if not self.et_data_i.get():
            self.et_data_i.insert(0, "Exemplo: 01/01/2025")
            self.et_data_i.config(style="Placeholder.TEntry")

    def remove_placeholder_data_f(self, event):
        if self.et_data_f.get() == "Exemplo: 31/01/2025":
            self.et_data_f.delete(0, "end")
            self.et_data_f.config(style="Default.TEntry")

    def add_placeholder_data_f(self, event):
        if not self.et_data_f.get():
            self.et_data_f.insert(0, "Exemplo: 31/01/2025")
            self.et_data_f.config(style="Placeholder.TEntry")


    def converter_data(self):
        data_i = self.et_data_i.get()
        data_f = self.et_data_f.get()

        if data_i == '' and data_f == '':
            messagebox.showwarning('Aviso!', 'Preencha todos campos para realizar\n o relatório automático')

        elif data_i == '' or data_f == '':
            messagebox.showwarning('Aviso!', 'Preencha todos campos para realizar\n o relatório automático')

        elif  data_i == "Exemplo: 01/01/2025" and  data_f == "Exemplo: 31/01/2025":
            messagebox.showwarning('Aviso!', 'Preencha todos campos para realizar\n o relatório automático')
        
        elif  data_i == "Exemplo: 01/01/2025" or data_f == "Exemplo: 31/01/2025":
            messagebox.showwarning('Aviso!', 'Preencha todos campos para realizar\n o relatório automático')
        
        else:
            tela_confirm = messagebox.askyesno(
                'CONFIRME PARA REALIZAR RELATÓRIO',
                "Clique em 'sim' para confirmar operação\npara cancelar clique em 'não'"
            )

            if tela_confirm:
                dados_data_i = data_i.split("/")
                dados_data_f = data_f.split("/")

                self.data_i_formatada = f'{dados_data_i[2]}-{dados_data_i[1]}-{dados_data_i[0]}'
                self.data_f_formatada = f'{dados_data_f[2]}-{dados_data_f[1]}-{dados_data_f[0]}'

                self.janela_main.destroy()
            else:
                messagebox.showinfo("info", "Automação Relatório Cancelada!\nClique em 'ok' para finalizar o programa")
                self.janela_main.destroy()
                sys.exit(0)


if __name__ == "__main__":

    tela = TelaData()

    data_i = tela.data_i_formatada
    data_f = tela.data_f_formatada
    
    caminho_relatório = os.path.join(os.getcwd(),"Conceitos_Avançados", "view", "relatorio.txt")
    messagebox.showinfo('info',f'Relatório foi Gerado! no caminho: {caminho_relatório}')
