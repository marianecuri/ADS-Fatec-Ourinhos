import Grafico_Oferta
import Grafico_Demanda
import Grafico_Equilibrio_Mercado
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Criando e dando função ao botão de oferta
axBotao1 = plt.axes([0.25, .8, 0.5, 0.1])
botao1 = Button(axBotao1, 'Grafico de Oferta')

def botao_oferta(event):
    Grafico_Oferta
botao1.on_clicked(botao_oferta)

# Criando e dando função ao botão de demanda
axBotao2 = plt.axes([0.25, .65, 0.5, 0.1])
botao2 = Button(axBotao2, 'Grafico de Demanda')

def botao_demanda(event):
    Grafico_Demanda
botao2.on_clicked(botao_demanda)

# Criando e dando função ao botão de equilíbrio de mercado
axBotao3 = plt.axes([0.25, .5, 0.5, 0.1])
botao3 = Button(axBotao3, 'Grafico de Equilíbrio de Mercado')

def botao_mercado(event):
    Grafico_Equilibrio_Mercado
botao3.on_clicked(botao_mercado)

plt.show()