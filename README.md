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

<h2>Licença</h2>
<p>Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.</p>

</body>
</html>
