from tkinter import Tk
from tkinter import ttk
from tkinter import Frame, Label, Button
from tkinter import messagebox
from datetime import datetime
import sys
import os


class TelaBKP:
    # realizando construtor
    def __init__(self):
        self.janela_main = Tk()
        self.janela_main.title("Automatizador de Relatório")
        self.config_janela()
        self.create_styles()
        self.widgets_frame1()
        self.janela_main.mainloop()  # abrindo janela

    def config_janela(self):
        self.janela_main.geometry('760x300')
        self.janela_main.resizable(False, False)
        self.janela_main.iconbitmap(os.path.join(os.getcwd(), "interface", "Grupo-3.ico"))
        self.janela_main.configure(background='#fff')

        self.frame1 = Frame(self.janela_main, bg='#f6cd34', relief="ridge", bd=3)
        self.frame1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

    def create_styles(self):  # para o método ttk, precisamos criar estilos personalizados
        self.style = ttk.Style()
        self.style.configure("Placeholder.TEntry", foreground="gray")
        self.style.configure("Default.TEntry", foreground="black")

    def widgets_frame1(self):
        lb_arq_xlsx = Label(self.frame1, text='RENOMEIE O ARQUIVO EXCEL PARA BKP', bg='red', fg='#fff', font=('Arial', 12, 'bold'))
        lb_arq_xlsx.place(relx=0.23, rely=0.15, relwidth=0.55, relheight=0.1)

        # Entry com placeholder
        self.et_arq_xlsx = ttk.Entry(self.frame1, font=("Arial", 9), justify='center', style="Placeholder.TEntry")
        self.et_arq_xlsx.place(relx=0.23, rely=0.3, relwidth=0.55, relheight=0.1)
        self.et_arq_xlsx.insert(0, "Exemplo: DER_MULTAS_SENHA")
        self.et_arq_xlsx.bind('<FocusIn>', self.remove_placeholder_data_i)
        self.et_arq_xlsx.bind('<FocusOut>', self.add_placeholder_data_i)

        lb_data_f = Label(self.frame1, text='RENOMEIE O ARQUIVO DB PARA BKP', bg='red', fg='#fff', font=('Arial', 12, 'bold'))
        lb_data_f.place(relx=0.23, rely=0.46, relwidth=0.55, relheight=0.1)

        self.et_arq_db = ttk.Entry(self.frame1, font=("Arial", 9), justify='center', style="Placeholder.TEntry")
        self.et_arq_db.place(relx=0.23, rely=0.6, relwidth=0.55, relheight=0.1)
        self.et_arq_db.insert(0, "Exemplo: DER_MULTAS_SENHA")
        self.et_arq_db.bind('<FocusIn>', self.remove_placeholder_data_f)
        self.et_arq_db.bind('<FocusOut>', self.add_placeholder_data_f)

        self.bt_confirm_data = Button(self.frame1, text="Confirmar", bd=4, command= self.confirmar)
        self.bt_confirm_data.place(relx=0.39, rely=0.8, relwidth=0.2, relheight=0.15)

    def remove_placeholder_data_i(self, event):
        if self.et_arq_xlsx.get() == "Exemplo: DER_MULTAS_SENHA":
            self.et_arq_xlsx.delete(0, "end")
            self.et_arq_xlsx.config(style="Default.TEntry")

    def add_placeholder_data_i(self, event):
        if not self.et_arq_xlsx.get():
            self.et_arq_xlsx.insert(0, "Exemplo: DER_MULTAS_SENHA")
            self.et_arq_xlsx.config(style="Placeholder.TEntry")

    def remove_placeholder_data_f(self, event):
        if self.et_arq_db.get() == "Exemplo: DER_MULTAS_SENHA":
            self.et_arq_db.delete(0, "end")
            self.et_arq_db.config(style="Default.TEntry")

    def add_placeholder_data_f(self, event):
        if not self.et_arq_db.get():
            self.et_arq_db.insert(0, "Exemplo: DER_MULTAS_SENHA")
            self.et_arq_db.config(style="Placeholder.TEntry")

    def confirmar(self):
        
        # puxando dados das entrys e formatando as String
        self.arq_xlsx = self.et_arq_xlsx.get().upper()
        self.arq_db = self.et_arq_db.get().upper()

        if self.arq_xlsx == '' and self.arq_db == '':
            messagebox.showwarning('Aviso!', 'Preencha todos os campos para realizar\n o relatório automático')

        elif self.arq_xlsx == '' or self.arq_db == '':
            messagebox.showwarning('Aviso!', 'Preencha todos os campos para realizar\n o relatório automático')

        elif self.arq_xlsx == "Exemplo: DER_MULTAS_SENHA" and self.arq_db == "Exemplo: DER_MULTAS_SENHA":
            messagebox.showwarning('Aviso!', 'Preencha todos os campos para realizar\n o relatório automático')

        elif self.arq_xlsx == "Exemplo: DER_MULTAS_SENHA" or self.arq_db == "Exemplo: DER_MULTAS_SENHA":
            messagebox.showwarning('Aviso!', 'Preencha todos os campos para realizar\n o relatório automático')

        else:
            tela_confirm = messagebox.askyesno(
                'CONFIRME PARA REALIZAR BKP NO SERVIDOR',
                "Clique em 'sim' para confirmar a operação\npara cancelar clique em 'não'"
            )

            if tela_confirm:
                # Gerando o mês e ano automaticamente
                meses = {
                    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
                    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
                    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
                }
                self.mes_atual = meses[datetime.now().month]
                self.ano_atual = datetime.now().year

                # Corrigindo self.arq_xlsx
                if not self.arq_xlsx.endswith('.xlsx'):
                    self.arq_xlsx += f'_{self.mes_atual}{self.ano_atual}.xlsx'

                # Formatando para o backup do servidor
                self.arq_xlsx = f"Relatório_{self.arq_xlsx.replace(' ', '_')}"

                # Corrigindo self.arq_db
                if not self.arq_db.endswith('.db'):
                    self.arq_db += f'_{self.mes_atual}{self.ano_atual}.db'

                # Formatando para o backup do servidor
                self.arq_db = f"s3db_{self.arq_db.replace(' ', '_')}"

                # Fechando a janela
                self.janela_main.destroy()

            else:
                messagebox.showinfo("Info", "Automação Relatório Cancelada!\nClique em 'ok' para finalizar o programa")
                self.janela_main.destroy()
                sys.exit(0)
            
        
        
    
# realizar debug
if __name__ == '__main__':
    
    tela = TelaBKP()


    arq_xlsx = tela.arq_xlsx
    arq_db = tela.arq_db
    
    print(f'{arq_xlsx}\n{arq_db}')

