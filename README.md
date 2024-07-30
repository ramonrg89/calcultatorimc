Calculadora de IMC
Este é um projeto simples de uma calculadora de Índice de Massa Corporal (IMC) desenvolvida em Python usando a biblioteca Tkinter para criar uma interface gráfica. A calculadora recebe o peso e a altura do usuário, calcula o IMC e fornece uma classificação com base no resultado. Além disso, exibe uma barra colorida para representar visualmente a categoria do IMC.

Funcionalidades
Cálculo do IMC: Calcula o IMC com base no peso e altura inseridos.
Classificação do IMC: Exibe a classificação do IMC com cores diferentes para representar as categorias:
Abaixo do peso
Peso normal
Sobrepeso
Obesidade grau 1
Obesidade grau 2
Obesidade grau 3
Barra de IMC: Mostra uma barra colorida que reflete a categoria do IMC.
Como usar
Instale o Python: Certifique-se de que o Python está instalado no seu sistema. Você pode baixá-lo aqui.

Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/calculadora-imc.git
Navegue até o diretório do projeto:

bash
Copiar código
cd calculadora-imc
Execute o script:

bash
Copiar código
python calculadora_imc.py
Use a calculadora:

Insira a altura em metros e o peso em quilogramas nos campos apropriados.
Clique no botão "Calcular IMC".
Veja o resultado e a barra de IMC atualizarem com base na sua entrada.
Código
O código utiliza o Tkinter para criar a interface gráfica, com os seguintes componentes principais:

Labels e campos de entrada para peso e altura.
Um botão para calcular o IMC.
Um Label para mostrar o resultado do IMC.
Um Canvas para mostrar a barra colorida representando a categoria do IMC.
Exemplo de Código
Aqui está um exemplo do código principal:

python
Copiar código

import tkinter as tk
from tkinter import font

def calculate():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura * altura)
        
        if imc < 18.59:
            classificacao = "Abaixo do peso"
            cor_texto = "white"
            barra_valor = 0.1
        elif 18.5 <= imc < 24.99:
            classificacao = "Peso normal"
            cor_texto = "#00FF00"
            barra_valor = 0.3
        elif 25 <= imc < 29.99:
            classificacao = "Sobrepeso"
            cor_texto = "#FFFF00"
            barra_valor = 0.5
        elif 30 <= imc < 34.99:
            classificacao = "Obesidade grau 1"
            cor_texto = "#FFA500"
            barra_valor = 0.7
        elif 35 <= imc < 39.99:
            classificacao = "Obesidade grau 2"
            cor_texto = "#FF6347"
            barra_valor = 0.9
        else:
            classificacao = "Obesidade grau 3"
            cor_texto = "#ff0000"
            barra_valor = 1.0
        
        result_label.config(text=f"IMC: {imc:.2f} \n({classificacao})", fg=cor_texto)
        canvas_barra.delete("all")
        canvas_barra.create_rectangle(0, 0, 200 * barra_valor, 20, fill=cor_texto, outline="")
        canvas_barra.grid(row=4, column=0, columnspan=2, pady=10)
    except ValueError:
        result_label.config(text="Por favor, insira valores válidos.", fg="white")

root = tk.Tk()
fonte = "Tahoma"
font_size = 14
background_color = "#0c0c0c"
root.title("Calculadora IMC")
root.geometry("300x300")
root.configure(bg=background_color)
main_frame = tk.Frame(root, bg=background_color)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame = tk.Frame(main_frame, bg=background_color)
frame.grid(row=0, column=0)
label_altura = tk.Label(frame, text="Altura(m):", bg=background_color, fg="white", font=(fonte, font_size), width=12, anchor="e")
label_altura.grid(row=0, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame, font=(fonte, font_size), width=12)
entry_altura.grid(row=0, column=1, padx=5, pady=5)
label_peso = tk.Label(frame, text="Peso(kg):", bg=background_color, fg="white", font=(fonte, font_size), width=12, anchor="e")
label_peso.grid(row=1, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame, font=(fonte, font_size), width=12)
entry_peso.grid(row=1, column=1, padx=5, pady=5)
button = tk.Button(main_frame, text="Calcular IMC", bg="#669E2E", fg="white", font=("Arial", font_size), width=12, command=calculate)
button.grid(row=2, column=0, pady=20)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
result_label = tk.Label(main_frame, text="", bg=background_color, fg="white", font=("Arial", font_size))
result_label.grid(row=3, column=0, columnspan=2, pady=10)
canvas_barra = tk.Canvas(main_frame, width=200, height=20, bg="grey", highlightthickness=0)
root.mainloop()



## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
