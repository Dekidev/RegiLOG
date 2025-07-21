import customtkinter as ctk
import datetime
from services.spreadsheet import salvar_dados_excel

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.title('MIMO - Formulário Laboratório')
        self.geometry('750x480')
        
        hoje_var = ctk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))

        self.label_titulo = ctk.CTkLabel(self, text='Formulário- MIMO')
        self.label_titulo.grid(row=0, columnspan= 3, padx=10, pady= 10, sticky= 'new')

        self.label_data = ctk.CTkLabel(self, text='Data').grid(row=1, column= 0, padx=10, pady= 10)
        self.entry_data = ctk.CTkEntry(self, textvariable= hoje_var)
        self.entry_data.grid(row=2, column=0, padx= 10, pady= 10)

        self.os_var = ctk.StringVar()

        self.label_OS = ctk.CTkLabel(self, text= 'O.S.').grid(row= 1, column= 1, padx=10, pady= 10)
        self.entry_OS = ctk.CTkEntry(self, placeholder_text='Ex: S-5660 ou 11076', textvariable= self.os_var).grid(row=2, column=1, padx= 10, pady= 10)

        #Opções- Tipos de montagens
        self.servicos = ['Montagem', 'Solda Simples', 'Caixa de Mola']
        self.servico_var = ctk.StringVar(value= self.servicos[0])

        self.label_servico = ctk.CTkLabel(self, text= 'Serviço').grid(row=1, column= 2, padx=10, pady= 10)
        self.servico_menu = ctk.CTkOptionMenu(self, variable=self.servico_var, values=self.servicos, command=self.atualizar_preco_automaticamente)
        self.servico_menu.grid(row=2, column= 2, padx=10, pady= 10)

        self.check_var = ctk.BooleanVar(value=False)

        self.check_box = ctk.CTkCheckBox(self, text='1/2 Par', variable= self.check_var, onvalue=True, offvalue=False, command=self.atualizar_preco_automaticamente)
        self.check_box.grid(row= 2, column= 3, padx= (10,0), pady=10)

        self.valor_var = ctk.StringVar(value="0,00")

        self.label_valor = ctk.CTkLabel(self, text='Valor(R$)').grid(row=1, column=4, padx= 10, pady=10)
        self.entry_valor = ctk.CTkEntry(self, textvariable=self.valor_var).grid(row=2, column=4, padx= 10, pady=10)

        self.btn_salvar = ctk.CTkButton(self, text='Salvar', command=self.botao_apertado)
        self.btn_salvar.grid(row=4, column=1, padx=10, pady=10, columnspan= 2)

        self.btn_msg = ctk.CTkLabel(self, text='')
        self.btn_msg.grid(row=5, column=1, padx=10, pady=10, columnspan= 2)

    
    def botao_apertado(self):
        print("Botão salvar foi clicado")
        self.salvar_dados()
        self.os_var.set(" ")
        self.btn_msg.configure(text= 'Ordem de serviço salva com sucesso!')
        self.after(500, self.restaurar_btn)

    def restaurar_btn(self):
        self.btn_msg.configure(text=' ')

    def salvar_dados(self):
        data = self.entry_data.get()
        os_num = self.os_var.get()
        servico = self.servico_var.get()
        valor = self.valor_var.get()

        print(f"Salvando: {data}, {os_num}, {servico}, {valor}")
        salvar_dados_excel(data, os_num, servico, valor)


    def atualizar_preco_automaticamente(self, event=None):
        servico_escolhido = self.servico_var.get()
        meio_par = self.check_var.get()

        if servico_escolhido == "Montagem":
            self.valor_var.set("10,00")
            if meio_par:
                self.valor_var.set("5,00")
            else:
                self.valor_var.set("10,00")
        elif servico_escolhido == "Solda Simples":
            self.valor_var.set("15,00")
        elif servico_escolhido == "Caixa de Mola":
            self.valor_var.set("15,00")
        else:
            self.valor_var.set("Digite o valor (R$)")
    




if __name__ == "__main__":
    app = App()
    app.mainloop()



