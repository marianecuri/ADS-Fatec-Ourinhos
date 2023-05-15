import Oferta
import Demanda
import Mercado
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Criando e dando função ao botão de oferta
axBotao1 = plt.axes([0.25, .8, 0.5, 0.1])
botao1 = Button(axBotao1, 'Grafico de Oferta')

def botao_oferta(event):
    Oferta
botao1.on_clicked(botao_oferta)

# Criando e dando função ao botão de demanda
axBotao2 = plt.axes([0.25, .65, 0.5, 0.1])
botao2 = Button(axBotao2, 'Grafico de Demanda')

def botao_demanda(event):
    Demanda
botao2.on_clicked(botao_demanda)

# Criando e dando função ao botão de equilíbrio de mercado
axBotao3 = plt.axes([0.25, .5, 0.5, 0.1])
botao3 = Button(axBotao3, 'Grafico de Equilíbrio de Mercado')

def botao_mercado(event):
    Mercado
botao3.on_clicked(botao_mercado)

plt.show()