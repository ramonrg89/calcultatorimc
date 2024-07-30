<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Calculadora de IMC</h1>
<p>Este é um projeto simples de uma calculadora de Índice de Massa Corporal (IMC) desenvolvida em Python usando a biblioteca Tkinter para criar uma interface gráfica. A calculadora recebe o peso e a altura do usuário, calcula o IMC e fornece uma classificação com base no resultado. Além disso, exibe uma barra colorida para representar visualmente a categoria do IMC.</p>

<h2>Funcionalidades</h2>
<ul>
    <li><strong>Cálculo do IMC:</strong> Calcula o IMC com base no peso e altura inseridos.</li>
    <li><strong>Classificação do IMC:</strong> Exibe a classificação do IMC com cores diferentes para representar as categorias:
        <ul>
            <li><span style="color:white;">Abaixo do peso</span></li>
            <li><span style="color:#00FF00;">Peso normal</span></li>
            <li><span style="color:#FFFF00;">Sobrepeso</span></li>
            <li><span style="color:#FFA500;">Obesidade grau 1</span></li>
            <li><span style="color:#FF6347;">Obesidade grau 2</span></li>
            <li><span style="color:#ff0000;">Obesidade grau 3</span></li>
        </ul>
    </li>
    <li><strong>Barra de IMC:</strong> Mostra uma barra colorida que reflete a categoria do IMC.</li>
</ul>

<h2>Como usar</h2>
<ol>
    <li><strong>Instale o Python:</strong> Certifique-se de que o Python está instalado no seu sistema. Você pode baixá-lo <a href="https://www.python.org/downloads/" target="_blank">aqui</a>.</li>
    <li><strong>Clone o repositório:</strong>
        <pre><code>git clone https://github.com/seu-usuario/calculadora-imc.git</code></pre>
    </li>
    <li><strong>Navegue até o diretório do projeto:</strong>
        <pre><code>cd calculadora-imc</code></pre>
    </li>
    <li><strong>Execute o script:</strong>
        <pre><code>python calculadora_imc.py</code></pre>
    </li>
    <li><strong>Use a calculadora:</strong> 
        <ul>
            <li>Insira a altura em metros e o peso em quilogramas nos campos apropriados.</li>
            <li>Clique no botão "Calcular IMC".</li>
            <li>Veja o resultado e a barra de IMC atualizarem com base na sua entrada.</li>
        </ul>
    </li>
</ol>

<h2>Código</h2>
<p>O código utiliza o Tkinter para criar a interface gráfica, com os seguintes componentes principais:</p>
<ul>
    <li>Labels e campos de entrada para peso e altura.</li>
    <li>Um botão para calcular o IMC.</li>
    <li>Um Label para mostrar o resultado do IMC.</li>
    <li>Um Canvas para mostrar a barra colorida representando a categoria do IMC.</li>
</ul>

<h2>Exemplo de Código</h2>
<p>Aqui está um exemplo do código principal:</p>
<pre class="code-example">
<code>import tkinter as tk
from tkinter import font
		
	def calculate():
		try:
			peso = float(entry_peso.get())
			altura = float(entry_altura.get())
			imc = peso / (altura * altura)
			
			if imc &lt; 18.59:
				classificacao = "Abaixo do peso"
				cor_texto = "white"
				barra_valor = 0.1
			elif 18.5 &lt;= imc &lt; 24.99:
				classificacao = "Peso normal"
				cor_texto = "#00FF00"
				barra_valor = 0.3
			elif 25 &lt;= imc &lt; 29.99:
				classificacao = "Sobrepeso"
				cor_texto = "#FFFF00"
				barra_valor = 0.5
			elif 30 &lt;= imc &lt; 34.99:
				classificacao = "Obesidade grau 1"
				cor_texto = "#FFA500"
				barra_valor = 0.7
			elif 35 &lt;= imc &lt; 39.99:
				classificacao = "Obesidade grau 2"
				cor_texto = "#FF6347"
				barra_valor = 0.9
			else:
				classificacao = "Obesidade grau 3"
				cor_texto = "#ff0000"
				barra_valor = 1.0
			
			result_label.config(text=f"IMC: {imc:.2f} \\n({classificacao})", fg=cor_texto)
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
</code></pre>

<h2>Licença</h2>
<p>Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.</p>

</body>
</html>
