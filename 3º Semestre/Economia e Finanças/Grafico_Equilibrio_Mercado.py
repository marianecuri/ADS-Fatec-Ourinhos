import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define os parâmetros iniciais
preco_init = 4
outros_produtos_init = 4
desloc_demanda_init = 0

# Define a função de demanda
def demanda(quantidade):
    return 8 - (1/75) * quantidade

# Define a função que calcula a deslocação da demanda
def desloc_demanda(quantidade, preco, outros_produtos):
    return demanda(quantidade + desloc_demanda_init) - 1 * preco + 1 * outros_produtos

# Cria a figura e a linha/reta a ser manipulada
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade')
ax.set_ylabel('Preço')
ax.set_xlim([0, 800])
ax.set_ylim([0, 10])

# Plotagem da função de demanda
quantidade = np.linspace(0, 1000, 2000)
demanda_reta, = ax.plot(quantidade, demanda(quantidade), color='blue', lw=2)

# Plotagem da função de deslocação da demanda inicial
desloc_demanda_reta, = ax.plot(quantidade, desloc_demanda(quantidade, preco_init, outros_produtos_init), color='black', lw=2)

# Ajuste do espaço para os sliders
fig.subplots_adjust(left=0.25, bottom=0.4)

# Cria um slider horizontal para controlar o preço do produto
axpreco = fig.add_axes([0.3, 0.25, 0.5, 0.03])
slider_preco = Slider(
    ax=axpreco,
    label='Preço do Produto',
    valmin=0,
    valmax=8,
    valinit=preco_init,
    valstep=0.01,
)

# Cria um slider horizontal para controlar o preço de produtos substitutos
axoutros_produtos = fig.add_axes([0.3, 0.15, 0.5, 0.03])
slider_outros_produtos = Slider(
    ax=axoutros_produtos,
    label='Preço de Produtos Substitutos',
    valmin=0,
    valmax=8,
    valinit=outros_produtos_init,
    valstep=0.01,
)

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza o ponto vermelho na reta de demanda
        point.set_data([quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])
    else:
        # Atualiza a função de deslocação da demanda
        desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, slider_preco.val, slider_outros_produtos.val))
        # Atualiza o ponto vermelho na reta de deslocação da demanda
        point.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_outros_produtos.on_changed(update)

# Cria um `matplotlib.widgets.Button` para resetar os sliders aos valores iniciais
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    slider_preco.reset()
    slider_outros_produtos.reset()
    desloc_demanda_init = 0
    desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, preco_init, outros_produtos_init))
    point.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
button.on_clicked(reset)

# Plotagem do ponto vermelho na reta de deslocação da demanda inicial
point, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ro')

# Cria uma legenda para identificar as linhas/retas
ax.legend((demanda_reta, desloc_demanda_reta), ('Demanda', 'Deslocação da Demanda'))

plt.show()