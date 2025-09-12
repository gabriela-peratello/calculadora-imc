import ttkbootstrap as tb
import tkinter.messagebox
class Janela_principal:
    def __init__(self):
        # CRIANDO A JANELA
        self.janela = tb.Window(title="Calculadora IMC", themename="darkly")  # Usando tb.Window
        # DEFININDO TAMANHO DA JANELA
        self.janela.geometry("800x600")
        self.janela.resizable(False, False)

        # INTRODUÇÃO 
        self.janela_nome = tb.Label(self.janela, text="O IMC (Índice de massa corporal) é um cálculo que avalia se o seu peso está saudável.")
        self.janela_nome.pack(padx=20, pady=5)

        # SUBTEXTO PESO
        self.janela_subtexto01 = tb.Label(self.janela, text="Digite seu peso (em kg):")
        self.janela_subtexto01.pack()

        # CAMPO PARA DIGITAR O PESO
        self.janela_peso = tb.Entry(self.janela, width=50)
        self.janela_peso.pack(padx=30, pady=10)

        # SUBTEXTO ALTURA
        self.janela_subtexto02 = tb.Label(self.janela, text="Digite sua altura (em metros):")
        self.janela_subtexto02.pack()

        # CAMPO PARA DIGITAR A ALTURA
        self.janela_altura = tb.Entry(self.janela, width=50)
        self.janela_altura.pack()

        # BOTÃO PARA ENVIAR
        self.janela_botao = tb.Button(self.janela, text="Calcular IMC", command=self.calcular_imc)
        self.janela_botao.pack(padx=20, pady=20)

        # LABEL PARA EXIBIR O RESULTADO
        self.resultado_label = tb.Label(self.janela, text="")
        self.resultado_label.pack(pady=20)

    def calcular_imc(self):
        try:
            # Pegando os valores inseridos
            peso = float(self.janela_peso.get())
            altura = float(self.janela_altura.get())

        
            # CALCULANDO O IMC
            imc = peso / (altura ** 2)

            # CALCULO
            if imc < 18.5:
                resultado = "(Abaixo do peso)"
            elif 18.5 <= imc < 24.9:
                resultado = "(Peso normal)"
            elif 25 <= imc < 29.9:
                resultado = "(Sobrepeso)"
            else:
                resultado = "(Obesidade)"
            # MOSTRANDO RESULTADO
            self.resultado_label.config(text=f"O seu IMC é {imc:.2f}. Você está na categoria {resultado}")
            
        except ValueError or ZeroDivisionError:
            tkinter.messagebox.showerror(title="ERRO")



       

    def run(self):
        self.janela.mainloop()

# Instanciando a classe e rodando
if __name__ == "__main__":
    app = Janela_principal()
    app.run()
