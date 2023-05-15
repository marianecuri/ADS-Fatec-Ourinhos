import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define os parâmetros iniciais
preco_init = 139
outros_produtos_init = 139
renda_init = 2424
expectativa_init = 50
desloc_demanda_init = 0

# Define a função de demanda
def demanda(quantidade):
    return 304 - 0.16 * quantidade

# Define a função que calcula a deslocação da demanda
def desloc_demanda(quantidade, preco, outros_produtos, renda, expectativa):
    return demanda(quantidade) - (1 * preco) + (1 * outros_produtos) + (0.005 * renda - 112.5) + (3 * expectativa - 50)

# Cria a figura e a linha/reta a ser manipulada
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade (Unidades)')
ax.set_ylabel('Preço (R$)')
ax.set_xlim([0, 2500])
ax.set_ylim([0, 250])

# Plotagem da função de deslocação da demanda inicial
quantidade = np.linspace(0, 2500, 5000)
desloc_demanda_reta, = ax.plot(quantidade, desloc_demanda(quantidade, preco_init, outros_produtos_init, renda_init, expectativa_init), color='black', lw=2)

# Plotagem da função de demanda
demanda_reta, = ax.plot(quantidade, demanda(quantidade), color='blue', lw=2)

# Título do gráfico e ajuste do espaço para os sliders
plt.title('Gráfico de Demanda')
fig.subplots_adjust(left=0.25, bottom=0.4)

# Cria um slider horizontal para controlar o preço do produto
axpreco = fig.add_axes([0.3, 0.25, 0.5, 0.03])
slider_preco = Slider(
    ax=axpreco,
    label='Preço do Produto (R$)',
    valmin=0,
    valmax=300,
    valinit=preco_init,
    valstep=0.01,
)

# Cria um slider horizontal para controlar a renda do consumidor
axrenda = fig.add_axes([0.3, 0.20, 0.5, 0.03])
slider_renda = Slider(
    ax=axrenda,
    label='Renda do Consumidor (R$)',
    valmin=0,
    valmax=50000,
    valinit=renda_init,
    valstep=0.01,
)

# Cria um slider horizontal para controlar o preço de produtos substitutos
axoutros_produtos = fig.add_axes([0.3, 0.15, 0.5, 0.03])
slider_outros_produtos = Slider(
    ax=axoutros_produtos,
    label='Preço de Produtos Substitutos (R$)',
    valmin=0,
    valmax=300,
    valinit=outros_produtos_init,
    valstep=0.01,
)

# Cria um slider horizontal para controlar a expectativa do consumidor
axexpectativa = fig.add_axes([0.3, 0.10, 0.5, 0.03])
slider_expectativa = Slider(
    ax=axexpectativa,
    label='Expectativa do Consumidor (%)',
    valmin=0,
    valmax=100,
    valinit=expectativa_init,
    valstep=0.01,
)

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza o ponto vermelho na reta de demanda
        ponto1.set_data([quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])
        
        # Atualiza o ponto vermelho na reta de deslocação da demanda
        ponto2.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
        
    if slider_outros_produtos.val != slider_outros_produtos.valinit or slider_renda.val != slider_renda.valinit or slider_expectativa.val != slider_expectativa.valinit:
        # Atualiza a função de deslocação da demanda
        desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, slider_preco.val, slider_outros_produtos.val, slider_renda.val, slider_expectativa.val))
	
        # Atualiza o ponto vermelho na reta de deslocação da demanda
        ponto2.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])

    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_outros_produtos.on_changed(update)
slider_renda.on_changed(update)
slider_expectativa.on_changed(update)

# Cria um `matplotlib.widgets.Button` para resetar os sliders aos valores iniciais
axreset = fig.add_axes([0.85, 0.05, 0.1, 0.04])
button = Button(axreset, 'Resetar', hovercolor='0.975')

def reset(event):
    slider_preco.reset()
    slider_outros_produtos.reset()
    slider_renda.reset()
    slider_expectativa.reset()
    desloc_demanda_init = 0
    desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, preco_init, outros_produtos_init, renda_init, expectativa_init))
    ponto1.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto2.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
button.on_clicked(reset)

# Plotagem dos pontos vermelhos nas retas de demanda e se deslocação da demanda inicial
ponto1, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ro')
ponto2, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ro')

# Cria uma legenda para identificar as linhas/retas
ax.legend((demanda_reta, desloc_demanda_reta), ('Demanda', 'Deslocação da Demanda'))

plt.show()