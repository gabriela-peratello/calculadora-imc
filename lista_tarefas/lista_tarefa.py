import ttkbootstrap as tb
from tkinter import Listbox
from tkinter import messagebox
import sqlite3


class Telalista:
    def __init__(self):
        self.janela = tb.Window("Afazeres", themename="morph")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        tb.Label(self.janela, text="Lista de afazeres").pack()

        frame_add = tb.Frame(self.janela)
        frame_add.pack(fill="x", padx=20)

        self.add_tarefa = tb.Entry(frame_add)
        self.add_tarefa.pack(side="left", fill="x", expand=True)    

        tb.Button (frame_add, text="Adicionar", command=self.adicionar_tarefa).pack(side="right")

        self.lista = Listbox(self.janela, height=10)
        self.lista.pack(padx=20, pady=20, fill="both", expand=True)

        frame_botao = tb.Frame(self.janela)
        frame_botao.pack(side="bottom")

        botao_excluir = tb.Button(frame_botao, text="Excluir", command=self.excluir_itens)
        botao_excluir.pack(side="left")

        feito = tb.Button(frame_botao, text="Concluido", command=self.concluir)
        feito.pack(side="right", padx=20)

        #criando e conectando ao banco de dados
        conexao = sqlite3.connect("lista_tarefas/bddados.sqlite")
        #criando o cursor que comanda o banco de dados
        cursor = conexao.cursor()
        #criando tabela
        sql_tabela = """
                        CREATE TABLE IF NOT EXISTS tarefas (
                        codigo integer primary key autoincrement, 
                        desc_tarefa varchar(200));
                    """
        cursor.execute(sql_tabela)
        #comitei as alterações
        conexao.commit()
        #fechei as conexões
        cursor.close()
        conexao.close()

        #atualizar a lista
        conexao = sqlite3.connect("lista_tarefas/bddados.sqlite")
        cursor = conexao.cursor()

        selecionar_tarefas=""" SELECT codigo, desc_tarefa FROM tarefas
                            """
        cursor.execute(selecionar_tarefas)

        tarefas_lista = cursor.fetchall()

        cursor.close()
        conexao.close()

        #inserindo os itens na listbox
        for linha in tarefas_lista:
            self.lista.insert("end", linha[1])

    def adicionar_tarefa(self):
        #pegando o texto da caixa de texto
        tarefa = self.add_tarefa.get()
        #inserindo tarefa na lista
        self.lista.insert(tb.END, tarefa)

        conexao = sqlite3.connect("lista_tarefas/bddados.sqlite")
        cursor = conexao.cursor()
        #sql do insert
        sql_insert = """
                    INSERT INTO tarefa (desc_tarefa)
                    VALUES (?)
                        """
        cursor.execute(sql_insert,[tarefa])

        conexao.commit()
        cursor.close()
        conexao.close()
        
    
    def excluir_itens (self):
        selecionando = self.lista.curselection()

        if selecionando:
            self.lista.delete(selecionando)
        else:
            messagebox.showerror(message="Selecione algo para excluir!")
    
    def concluir(self):
        concluido = self.lista.curselection()


        if concluido:
            item = self.lista.get(concluido)

            novo_item = item + " [Feito]"

            self.lista.delete(concluido)
            self.lista.insert(concluido, novo_item)
        else:
             messagebox.showerror(message="Selecione algo para concluir!")
    
    def run(self):
        self.janela.mainloop()
if __name__ == "__main__":
    lista = Telalista()
    lista.janela.mainloop()
