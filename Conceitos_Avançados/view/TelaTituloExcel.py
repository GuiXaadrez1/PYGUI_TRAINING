from tkinter import Tk
from tkinter import ttk
from tkinter import Frame, Label, Button
from tkinter import messagebox
from datetime import datetime
import sys
import os


class TelaTituloExcel:
    # realizando construtor
    def __init__(self):
        self.janela_main = Tk()
        self.janela_main.title("Automatizador de Relatório")
        self.config_janela()
        self.create_styles()
        self.widgets_frame1()
        self.janela_main.mainloop()  # abrindo janela

    def config_janela(self):
        self.janela_main.geometry('400x250')
        self.janela_main.resizable(False, False)
        self.janela_main.iconbitmap(os.path.join(os.getcwd(), "Conceitos_Avançados", "view", "Grupo-3.ico"))
        self.janela_main.configure(background='#fff')

        self.frame1 = Frame(self.janela_main, bg='#f6cd34', relief="ridge", bd=3)
        self.frame1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

    def create_styles(self):  # para o método ttk, precisamos criar estilos personalizados
        self.style = ttk.Style()
        self.style.configure("Placeholder.TEntry", foreground="gray")
        self.style.configure("Default.TEntry", foreground="black")

    def widgets_frame1(self):
        lb_titulo_xlsx = Label(self.frame1, text='RENOMEIE O TITULO DA PLANILHA EXCEL', bg='red', fg='#fff', font=('Arial', 12, 'bold'))
        lb_titulo_xlsx.place(relx=0.02, rely=0.2, relwidth=0.95, relheight=0.2)

        # Entry com placeholder
        self.et_titulo_xlsx = ttk.Entry(self.frame1, font=("Arial", 10), justify='center', style="Placeholder.TEntry")
        self.et_titulo_xlsx.place(relx=0.23, rely=0.5, relwidth=0.6, relheight=0.2)
        self.et_titulo_xlsx.insert(0, "Exemplo: MULTAS - Janeiro2025")
        self.et_titulo_xlsx.bind('<FocusIn>', self.remove_placeholder_data_i)
        self.et_titulo_xlsx.bind('<FocusOut>', self.add_placeholder_data_i)

        self.bt_confirm_data = Button(self.frame1, text="Confirmar", bd=4, command=self.confirmar)
        self.bt_confirm_data.place(relx=0.39, rely=0.8, relwidth=0.2, relheight=0.15)

    def remove_placeholder_data_i(self, event):
        if self.et_titulo_xlsx.get() == "Exemplo: MULTAS - Janeiro2025":
            self.et_titulo_xlsx.delete(0, "end")
            self.et_titulo_xlsx.config(style="Default.TEntry")

    def add_placeholder_data_i(self, event):
        if not self.et_titulo_xlsx.get():
            self.et_titulo_xlsx.insert(0, "Exemplo: MULTAS - Janeiro2025")
            self.et_titulo_xlsx.config(style="Placeholder.TEntry")

    def confirmar(self):
        # puxando dados da entry
        self.titulo_xlsx = self.et_titulo_xlsx.get()

        if not self.titulo_xlsx or self.titulo_xlsx == "Exemplo: MULTAS - Janeiro2025":
            messagebox.showwarning('Aviso!', 'Preencha o campo com um título válido para gerar o relatório.')
        else:
            tela_confirm = messagebox.showinfo('Finalizar Relatório', "Clique em 'OK' para finalizar o relatório")

            if tela_confirm:
                # Gerando o mês e ano automaticamente
                meses = {
                    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
                    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
                    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
                }
                self.mes_atual = meses[datetime.now().month]
                self.ano_atual = datetime.now().year

                self.janela_main.destroy()

            else:
                messagebox.showinfo("Info", "Automação do relatório cancelada!\nClique em 'OK' para finalizar o programa")
                self.janela_main.destroy()
                sys.exit(0)


# realizar debug
if __name__ == '__main__':
    tela = TelaTituloExcel()

    titulo = tela.titulo_xlsx

    print(f'{titulo}')
