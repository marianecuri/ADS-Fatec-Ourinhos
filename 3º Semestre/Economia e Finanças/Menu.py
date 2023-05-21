import subprocess
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

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
axBtn1 = plt.axes([0.25, 0.50, 0.5, 0.1])
btn1 = Button(axBtn1, 'Gráfico da Curva de Oferta', color='navajowhite', hovercolor='sandybrown')
btn1.on_clicked(botao_oferta)

# Criando e dando função ao botão de demanda
axBtn2 = plt.axes([0.25, 0.35, 0.5, 0.1])
btn2 = Button(axBtn2, 'Gráfico da Curva de Demanda', color='lightsteelblue', hovercolor='cornflowerblue')
btn2.on_clicked(botao_demanda)

# Criando e dando função ao botão de equilíbrio de mercado
axBtn3 = plt.axes([0.25, 0.20, 0.5, 0.1])
btn3 = Button(axBtn3, 'Gráfico de Equilíbrio de Mercado', color='aquamarine', hovercolor='mediumaquamarine')
btn3.on_clicked(botao_mercado)

# Adicionando título e texto
plt.title('Menu', y=5, fontsize=20, weight='bold')
texto1 = plt.text(0.5, 7.25, 'Economia e Finanças', ha='center', va='center', fontsize=16, weight='bold')
texto2 = plt.text(0.5, 6.75, 'Princípios de Funcionamento de Mercado', ha='center', va='center', fontsize=12)
texto3 = plt.text(0.5, 6.25, 'Representação gráfica das forças de oferta e demanda', ha='center', va='center', fontsize=12)
texto4 = plt.text(0.5, 4.5, 'Selecione uma opção para visualizar o gráfico correspondente:', ha='center', va='center', fontsize=12)

plt.show()