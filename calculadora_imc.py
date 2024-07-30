import tkinter as tk
from tkinter import font


def calculate():
    try:
        # Obtém os valores dos campos de entrada e converte para float
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        # Calcula o IMC
        imc = peso / (altura * altura)
        
        # Determina a classificação, a cor do texto e o valor da barra
        if imc < 18.59:
            classificacao = "Abaixo do peso"
            cor_texto = "white"
            barra_valor = 0.1
        elif 18.5 <= imc < 24.99:
            classificacao = "Peso normal"
            cor_texto = "#00FF00"  # Verde claro
            barra_valor = 0.3
        elif 25 <= imc < 29.99:
            classificacao = "Sobrepeso"
            cor_texto = "#FFFF00"  # Amarelo
            barra_valor = 0.5
        elif 30 <= imc < 34.99:
            classificacao = "Obesidade grau 1"
            cor_texto = "#FFA500"  # Laranja
            barra_valor = 0.7
        elif 35 <= imc < 39.99:
            classificacao = "Obesidade grau 2"
            cor_texto = "#FF6347"  # Laranja escuro
            barra_valor = 0.9
        else:
            classificacao = "Obesidade grau 3"
            cor_texto = "#ff0000"  # Vermelho
            barra_valor = 1.0
        
        # Atualiza o texto do resultado com a cor apropriada
        result_label.config(text=f"IMC: {imc:.2f} \n({classificacao})", fg=cor_texto)
        
        # Atualiza a barra de IMC com a mesma cor do texto e exibe a barra
        canvas_barra.delete("all")
        canvas_barra.create_rectangle(0, 0, 200 * barra_valor, 20, fill=cor_texto, outline="")
        canvas_barra.grid(row=4, column=0, columnspan=2, pady=10)
    
    except ValueError:
        # Trata erros de conversão de valor
        result_label.config(text="Por favor, insira valores válidos.", fg="white")
# Cria a janela principal
root = tk.Tk()

# Define o tamanho da fonte
fonte = "Tahoma"
font_size = 14
background_color = "#0c0c0c"

# Define o título da janela; tamanho da janela (largura x altura) e cor de fundo da janela
root.title("Calculadora IMC"); root.geometry("300x300"); root.configure(bg=background_color)

# Cria um Frame principal com a cor de fundo desejada
main_frame = tk.Frame(root, bg=background_color)
main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Cria um Frame para conter o label e o entry dentro do main_frame
frame = tk.Frame(main_frame, bg=background_color)
frame.grid(row=0, column=0)

# Cria um label para o peso dentro do frame
label_altura = tk.Label(frame, text="Altura(m):", bg=background_color, fg="white",font=(fonte, font_size),width=12, anchor="e")
label_altura.grid(row=0, column=0, padx=5, pady=5)

# Cria um campo de entrada para o peso dentro do frame
entry_altura = tk.Entry(frame, font=(fonte, font_size), width=12)
entry_altura.grid(row=0, column=1, padx=5, pady=5)

# Cria um label para o peso dentro do frame
label_peso = tk.Label(frame, text="Peso(kg):", bg=background_color, fg="white",font=(fonte, font_size), width=12, anchor="e")
label_peso.grid(row=1, column=0, padx=5, pady=5)

# Cria um campo de entrada para o peso dentro do frame
entry_peso = tk.Entry(frame, font=(fonte, font_size),width=12)
entry_peso.grid(row=1, column=1, padx=5, pady=5)


# Cria um botão com a cor especificada e o centraliza
button = tk.Button(main_frame, text="Calcular IMC", bg="#669E2E", fg="white", font=("Arial", font_size), width=12, command=calculate)
button.grid(row=2, column=0, pady=20,)

# Configura a expansão do Frame para que o botão fique centralizado
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Cria um Label para exibir o resultado
result_label = tk.Label(main_frame, text="", bg=background_color, fg="white", font=("Arial", font_size))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Cria um canvas para a barra de IMC
canvas_barra = tk.Canvas(main_frame, width=200, height=20, bg="grey", highlightthickness=0)

# Inicia o loop principal da aplicação
root.mainloop()