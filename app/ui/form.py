import customtkinter as ctk
import datetime

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.title('MIMO - Formulário Laboratório')
        self.geometry('640x480')
        
        hoje = ctk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))

        self.label_titulo = ctk.CTkLabel(self, text='Formulário- MIMO')
        self.label_titulo.grid(row=0, columnspan= 3, padx=10, pady= 10, sticky= 'new')

        self.label_data = ctk.CTkLabel(self, text='Data').grid(row=1, column= 0, padx=10, pady= 10)
        self.entry_data = ctk.CTkEntry(self, textvariable= hoje).grid(row=2, column=0, padx= 10, pady= 10)


        self.label_OS = ctk.CTkLabel(self, text= 'O.S.' ).grid(row= 1, column= 1, padx=10, pady= 10)
        self.entry_OS = ctk.CTkEntry(self, placeholder_text='Ex: S-5660 ou 11076').grid(row=2, column=1, padx= 10, pady= 10)

        #Opções- Tipos de montagens
        self.servicos = ['Montagem', 'Solda Simples', 'Caixa de Mola']
        self.servico_var = ctk.StringVar(value= self.servicos[0])

        self.label_servico = ctk.CTkLabel(self, text= 'Serviço').grid(row=1, column= 2, padx=10, pady= 10)
        self.servico_menu = ctk.CTkOptionMenu(self, variable=self.servico_var, values=self.servicos, command=self.atualizar_preco_automaticamente)
        self.servico_menu.grid(row=2, column= 2, padx=10, pady= 10)

        self.valor_var = ctk.StringVar(value="0,00")

        self.label_valor = ctk.CTkLabel(self, text='Valor(R$)').grid(row=1, column=3, padx= 10, pady=10)
        self.entry_valor = ctk.CTkEntry(self, textvariable=self.valor_var).grid(row=2, column=3, padx= 10, pady=10)

    def atualizar_preco_automaticamente(self, event=None):
        servico_escolhido = self.servico_var.get()

        if servico_escolhido == "Montagem":
            self.valor_var.set("10,00")
        elif servico_escolhido == "Solda Simples":
            self.valor_var.set("15,00")
        elif servico_escolhido == "Caixa de Mola":
            self.valor_var.set("20,00")
        else:
            self.valor_var.set("0,00")

if __name__ == "__main__":
    app = App()
    app.mainloop()



