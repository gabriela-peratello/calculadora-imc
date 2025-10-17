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

        #texto digite seu nome
        self.janela_nome = tb.Label(self.janela, text="Digite seu nome completo:")
        self.janela_nome.pack()

        #campo para digitar o nome
        self.janela_digitar_nome = tb.Entry(self.janela, width=50)
        self.janela_digitar_nome.pack(padx=30, pady=10)

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
        self.janela_botao = tb.Button(self.janela, text="Cadastrar", command=self.inserir_usuario)
        self.janela_botao.pack( padx=20, pady=20)

        self.tabela_usuario()

    def tabela_usuario(self):
        #conecatndo banco de dados
        conexao = sqlite3.connect("./bddados.sqlite")
        #criar cursor
        cursor = conexao.cursor()
        #executar comando
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (
                        nome VARCHAR(80),
                        usuario VARCHAR (20) PRIMARY KEY,
                        senha VARCHAR(20));
                        """)
        #comito a transição
        conexao.commit()
        #encerrar a conexão
        conexao.close()

    def inserir_usuario(self):
        #criar conexao
        conexao = sqlite3.connect("./bddados.sqlite")
        #criar cursor
        cursor = conexao.cursor()

        nome = self.janela_digitar_nome.get()
        usuario = self.janela_crieusuario.get()
        senha = self.janela_digite_senha.get()



        #criar cursor
        cursor.execute("""INSERT INTO usuario
                        (nome,
                        usuario,
                        senha)
                    VALUES
                        (?,
                        ?,
                        ?);
                        """,
                        (nome, usuario, senha)
                        )
        #comitar
        conexao.commit()
        conexao.close()

        
    

       




def run(self):
    self.cadastro.mainloop()

if __name__ == "__main__":
    login = Telacadastro()
    login.janela.mainloop()
