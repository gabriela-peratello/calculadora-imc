import ttkbootstrap as tb


class Telalista:
    def __init__(self):
        self.janela = tb.Window("Afazeres", themename="vapor")
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)
    





















    def run(self):
        self.janela.mainloop()
if __name__ == "__main__":
    lista = Telalista()
    lista.janela.mainloop()
