import ttkbootstrap as tb
from tkinter import Listbox


class Telalista:
    def __init__(self):
        self.janela = tb.Window("Afazeres", themename="superhero")
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

        botao_excluir = tb.Button(frame_botao, text="Excluir")
        botao_excluir.pack(side="left")

        feito = tb.Button(frame_botao, text="Concluido")
        feito.pack(side="right", padx=20)

    def adicionar_tarefa(self):
        #pegando o texto da caixa de texto
        tarefa = self.add_tarefa.get()
        #inserindo tarefa na lista
        self.lista.insert(tb.END, tarefa)






















    def run(self):
        self.janela.mainloop()
if __name__ == "__main__":
    lista = Telalista()
    lista.janela.mainloop()
