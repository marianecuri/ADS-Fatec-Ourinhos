import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import subprocess

# Função para executar o programa de oferta
def botao_oferta(event):
    subprocess.run(["python", "Economia e Finanças\Grafico_Oferta.py"])

# Função para executar o programa de demanda
def botao_demanda(event):
    subprocess.run(["python", "Economia e Finanças\Grafico_Demanda.py"])

# Função para executar o programa de equilíbrio de mercado
def botao_mercado(event):
    subprocess.run(["python", "Economia e Finanças\Grafico_Equilibrio_Mercado.py"])

# Criando e dando função ao botão de oferta
axBotao1 = plt.axes([0.25, 0.70, 0.5, 0.1])
botao1 = Button(axBotao1, 'Gráfico da Curva de Oferta')
botao1.color = 'palegoldenrod'
botao1.hovercolor = 'sandybrown'
botao1.on_clicked(botao_oferta)

# Criando e dando função ao botão de demanda
axBotao2 = plt.axes([0.25, 0.55, 0.5, 0.1])
botao2 = Button(axBotao2, 'Gráfico da Curva de Demanda')
botao2.color = 'powderblue'
botao2.hovercolor = 'steelblue'
botao2.on_clicked(botao_demanda)

# Criando e dando função ao botão de equilíbrio de mercado
axBotao3 = plt.axes([0.25, 0.40, 0.5, 0.1])
botao3 = Button(axBotao3, 'Gráfico de Equilíbrio de Mercado')
botao3.color = 'palegreen'
botao3.hovercolor = 'mediumseagreen'
botao3.on_clicked(botao_mercado)

# Adicionando título
plt.title('Menu', y=5, fontsize=18)

# Adicionando texto
texto = plt.text(0.5, 4.5, 'Selecione uma opção para visualizar o gráfico:', ha='center', va='center')

plt.show()