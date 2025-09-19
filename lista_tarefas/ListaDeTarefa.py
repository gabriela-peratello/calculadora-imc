import ttkbootstrap as tb
from tkinter import messagebox


class Telalogin:
    def __init__(self):
        self.janela = tb.Window (title="Lista de Afazeres", themename="darkly")
        #tamanho da janela
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

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
        self.janela_botao_cancelar = tb.Button(self.janela, text="SAIR", command=self.janela.destroy)
        self.janela_botao_cancelar.pack( padx=20, pady=40)

        #mostrar aceitação
        self.aceito_label = tb.Label(self.janela, text="")
        self.aceito_label.pack(pady=20)

    def conferir_login(self):

        login = (self.janela_login.get())
        senha = (self.janela_senha.get())


        if login == "gabriela" and senha == "gabi2008":
            messagebox.showinfo("Login aceito!", "Informações corretas inseridas.")
        else:
            messagebox.showerror("Login recusado.", "Tente novamente na próxima!") 
      
          
        










    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    login = Telalogin()
    login.janela.mainloop()