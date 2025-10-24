import ttkbootstrap as tb
from tkinter import messagebox
from cadastro import Telacadastro
import sqlite3

class Telalogin:
    def __init__(self, janela_pai):
        self.janela = tb.Toplevel(janela_pai)
        #tamanho da janela
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        #fechando
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)

        #introdução
        self.janela_nome = tb.Label(self.janela, text= "Seja bem vindo a sua lista de afazeres. Que tal começar fazendo o login?")
        self.janela_nome.pack(padx=20, pady=5)

        #texto login
        self.janela_textologin = tb.Label(self.janela, text="Digite seu usuário")
        self.janela_textologin.pack()

        #campo para digitar o login
        self.janela_login = tb.Entry(self.janela, width=50)
        self.janela_login.pack(padx=30, pady=10)

        #texto senha
        self.janela_textosenha = tb.Label(self.janela, text="Digite sua senha:")
        self.janela_textosenha.pack()

        #campo para digitar a senha
        self.janela_senha = tb.Entry(self.janela, width=50)
        self.janela_senha.pack()
        
        #botão para enviar
        self.janela_botao = tb.Button(self.janela, text="Confimar", command=self.conferir_login)
        self.janela_botao.pack( padx=20, pady=20)

        #botao para cancelar
        self.janela_botao_cancelar = tb.Button(self.janela, text="SAIR", command=self.sair)
        self.janela_botao_cancelar.pack( padx=20, pady=40)

        #mostrar aceitação
        self.aceito_label = tb.Label(self.janela, text="") 
        self.aceito_label.pack(pady=20)

        tb.Button(self.janela, text="Cadastrar", command=self.abrir_cadastro).pack()


    def run(self):
        self.janela.mainloop()

    #abrir tela cadastro
    def abrir_cadastro(self):
        Telacadastro(self.janela_botao)

    #confirmação pra sair
    def sair (self):
        resposta = messagebox.askyesno("Sair?", "Você deseja mesmo sair?")
        if resposta == True:
            exit()

    #def para conferir os dados colocados
    def conferir_login(self):

        login = (self.janela_login.get())
        senha = (self.janela_senha.get())

        conexao = sqlite3.connect("./bddados.sqlite")
        cursor = conexao.cursor()

        cursor.execute("""
                    SELECT usuario, nome FROM usuario WHERE 
                    usuario="?" and senha ="?;""",
                    [login, senha]
                       )

        if login == "g" and senha == "02":
            #messagebox.showinfo("Login aceito!", "Informações corretas inseridas.")
            self.janela.destroy()
            # lista = Telalista()
            # lista.run()
        else:
            messagebox.showerror("Login recusado.", "Tente novamente na próxima!") 

    
      
          
        












if __name__ == "__main__":
    login = Telalogin("casasasasasas")
    login.janela.mainloop()
