import ttkbootstrap as tb
from tkinter import Listbox
from tkinter import messagebox
import sqlite3

class Telacadastro:
    def __init__(self):
        self.janela = tb.Window("Cadastro", themename="morph")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        self.janela_nome = tb.Label(self.janela, text="Não tem um cadastro? Faça agora!")
        self.janela_nome.pack(padx=20, pady=5)

        #texto digite seu usuário
        self.janela_crieusuario = tb.Label(self.janela, text="Digite um nome de usário:")
        self.janela_crieusuario.pack()

        #campo para digitar
        self.janela_usuario = tb.Entry(self.janela, width=50)
        self.janela_usuario.pack(padx=30, pady=10)

        #texto digitar senha
        self.janela_digite_senha = tb.Label(self.janela, text="Crie uma senha forte!")
        self.janela_digite_senha.pack()

        #campo para digitar a senha
        self.janela_senha = tb.Entry(self.janela, width=50)
        self.janela_senha.pack()

         #botão para enviar
        self.janela_botao = tb.Button(self.janela, text="Confimar")
        self.janela_botao.pack( padx=20, pady=20)

       

       












if __name__ == "__main__":
    login = Telacadastro()
    login.janela.mainloop()
