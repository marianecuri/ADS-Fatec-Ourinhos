import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define os parâmetros iniciais
preco_init = 139
insumos_init = 139
desloc_oferta_init = 0

# Define a função de oferta
def oferta(quantidade):
    return 36 + 0.1 * quantidade

# Define a função que calcula a deslocação da oferta
def desloc_oferta(quantidade, preco, insumos):
    return oferta(quantidade) - (1 * preco) + (1 * insumos)

# Cria a figura e a linha/reta a ser manipulada
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade (Unidades)')
ax.set_ylabel('Preço (R$)')
ax.set_xlim([0, 2500])
ax.set_ylim([0, 250])

# Plotagem da função de deslocação da oferta inicial
quantidade = np.linspace(0, 2500, 5000)
desloc_oferta_reta, = ax.plot(quantidade, desloc_oferta(quantidade, preco_init, insumos_init), color='orange', lw=2)

# Plotagem da função de oferta
oferta_reta, = ax.plot(quantidade, oferta(quantidade), color='black', lw=2)

# Título do gráfico e ajuste do espaço para os sliders
plt.title('Gráfico da Curva de Oferta', y=1.05, fontsize=16, weight='bold')
fig.subplots_adjust(left=0.1, bottom=0.4)

# Cria um slider horizontal para controlar o preço do produto
axpreco = fig.add_axes([0.25, 0.25, 0.5, 0.03])
slider_preco = Slider(
    ax=axpreco,
    label='Preço do Produto (R$)',
    valmin=0,
    valmax=300,
    valinit=preco_init,
    valstep=0.01,
    color = 'sandybrown'
)

# Cria um slider horizontal para controlar o preço dos insumos
axinsumos = fig.add_axes([0.25, 0.20, 0.5, 0.03])
slider_insumos = Slider(
    ax=axinsumos,
    label='Preço dos Insumos Produtivos (R$)',
    valmin=0,
    valmax=300,
    valinit=insumos_init,
    valstep=0.01,
    color = 'sandybrown'
)

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza o ponto na reta de oferta
        ponto1.set_data([quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])
        
        # Atualiza o ponto na reta de deslocação da oferta
        ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
        
    if slider_insumos.val != slider_insumos.valinit:
        # Atualiza a função de deslocação da oferta
        desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, 139, slider_insumos.val))
	
        # Atualiza o ponto na reta de deslocação da oferta
        ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])

    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_insumos.on_changed(update)

# Cria um botão para resetar os sliders aos valores iniciais
axreset = fig.add_axes([0.8, 0.25, 0.1, 0.04])
button = Button(axreset, 'Resetar', color = 'navajowhite', hovercolor='sandybrown')

def reset(event):
    slider_preco.reset()
    slider_insumos.reset()
    desloc_oferta_init = 0
    desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, preco_init, insumos_init))
    ponto1.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
button.on_clicked(reset)

# Plotagem dos pontos nas retas de oferta e de deslocação da oferta inicial
ponto2, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'yo', markersize=6)
ponto1, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=6)

# Cria uma legenda para identificar as linhas/retas
ax.legend((oferta_reta, desloc_oferta_reta, ponto2), ('Oferta', 'Deslocação da Oferta','Preço x Quantidade'))

plt.show()