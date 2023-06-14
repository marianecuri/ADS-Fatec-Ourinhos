import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons

# Define os parâmetros iniciais
preco_init = 139
insumos_init = 139
desloc_oferta_init = 0

# Define a função de oferta
def oferta(quantidade):
    return 36 + 0.1 * quantidade

# Define a função que calcula a deslocação da oferta
def desloc_oferta(quantidade, preco, insumos):
    desloc_val = oferta(quantidade) - (1 * preco) + (1 * insumos)
    desloc_val = np.where(desloc_val < 16, np.nan, desloc_val)
    return desloc_val

def desloc_oferta2(quantidade, preco, insumos):
    return oferta(quantidade) - (1 * preco) + (1 * insumos)

# Cria a figura e a linha/reta a ser manipulada
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade (Unidades)')
ax.set_ylabel('Preço (R$)')
ax.set_xlim([0, 1800])
ax.set_ylim([0, 300])
ax.set_xticks(np.arange(0, 1800, 100))
ax.set_yticks(np.arange(0, 300, 25))

# Plotagem da função de deslocação da oferta inicial
quantidade = np.linspace(100, 2730, 5000)
desloc_oferta_reta, = ax.plot(quantidade, desloc_oferta(quantidade, preco_init, insumos_init), color='orange', lw=2)
desloc_oferta_ponto, = ax.plot(quantidade, desloc_oferta2(quantidade, preco_init, insumos_init), color='orange', lw=2)
desloc_oferta_ponto.set_visible(False)

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
    valmin=46,
    valmax=216,
    valinit=preco_init,
    valstep=0.01,
    color='sandybrown'
)

# Cria um slider horizontal para controlar o preço dos insumos
axinsumos = fig.add_axes([0.25, 0.20, 0.5, 0.03])
slider_insumos = Slider(
    ax=axinsumos,
    label='Preço dos Insumos Produtivos (R$)',
    valmin=46,
    valmax=216,
    valinit=insumos_init,
    valstep=0.01,
    color='sandybrown'
)

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza o ponto na reta de oferta
        ponto1.set_data([quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])

    if slider_insumos.val != slider_insumos.valinit:
        # Atualiza a função de deslocação da oferta
        desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, 139, slider_insumos.val))
        desloc_oferta_ponto.set_ydata(desloc_oferta2(quantidade, 139, slider_insumos.val))

    # Atualiza o ponto na reta de deslocação da oferta
    ponto2.set_data([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
        
    # Atualiza os stemplots verticais
    stem_vertical1.set_xdata([quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]] * 2)
    stem_vertical1.set_ydata([0, slider_preco.val])
        
    stem_vertical2.set_xdata([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]] * 2)
    stem_vertical2.set_ydata([0, slider_preco.val])
        
    # Atualiza os stemplots horizontais
    stem_horizontal1.set_xdata([0, quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]])
    stem_horizontal1.set_ydata([slider_preco.val] * 2)

    stem_horizontal2.set_xdata([0, desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]])
    stem_horizontal2.set_ydata([slider_preco.val] * 2)

    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_insumos.on_changed(update)

# Cria um botão para resetar os sliders aos valores iniciais
axreset = fig.add_axes([0.8, 0.25, 0.1, 0.04])
button = Button(axreset, 'Resetar', color='navajowhite', hovercolor='sandybrown')

def reset(event):
    slider_preco.reset()
    slider_insumos.reset()
    
    desloc_oferta_init = 0
    desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, preco_init, insumos_init))
    desloc_oferta_ponto.set_ydata(desloc_oferta2(quantidade, preco_init, insumos_init))
    
    ponto1.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto2.set_data([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - preco_init).argmin()]], [preco_init])
    
    stem_vertical1.set_xdata([quantidade[np.abs(oferta(quantidade) - preco_init).argmin()]] * 2)
    stem_vertical1.set_ydata([0, preco_init])
    stem_vertical2.set_xdata([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]] * 2)
    stem_vertical2.set_ydata([0, slider_preco.val])
    
    stem_horizontal1.set_xdata([0, quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]])
    stem_horizontal1.set_ydata([slider_preco.val] * 2)
    stem_horizontal2.set_xdata([0, desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]])
    stem_horizontal2.set_ydata([slider_preco.val] * 2)
    
button.on_clicked(reset)

# Cria os stemplots
stem_vertical1, = ax.plot([quantidade[np.abs(oferta(quantidade) - preco_init).argmin()]] * 2, [0, preco_init], '--', color='grey')
stem_vertical2, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]] * 2, [0, preco_init], '--', color='grey')
stem_horizontal1, = ax.plot([0, quantidade[np.abs(oferta(quantidade) - preco_init).argmin()]], [preco_init] * 2, '--', color='grey')
stem_horizontal2, = ax.plot([0, desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init] * 2, '--', color='grey')

# Plotagem dos pontos nas retas de oferta e de deslocação da oferta inicial
ponto2, = ax.plot([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - preco_init).argmin()]], [preco_init], 'yo', markersize=7)
ponto1, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=7)

# Cria um checkbox para controlar a visibilidade do stem_vertical1 e do stem_horizontal1
ax_check_vertical_horizontal = plt.axes([0.1, 0.9, 0.1, 0.05], frameon=False)
check_vertical_horizontal = CheckButtons(ax_check_vertical_horizontal, ['Mostrar/ocultar linha auxiliar - Oferta'], [True])
check_vertical_horizontal.labels[0].set_fontsize(10)
check_vertical_horizontal.labels[0].set_bbox(None)

# Função para atualizar a visibilidade do stem_vertical1 e do stem_horizontal1
def update_visibility_vertical_horizontal(label):
    if check_vertical_horizontal.get_status()[0]:
        stem_vertical1.set_visible(True)
        stem_horizontal1.set_visible(True)
    else:
        stem_vertical1.set_visible(False)
        stem_horizontal1.set_visible(False)
    fig.canvas.draw_idle()

check_vertical_horizontal.on_clicked(update_visibility_vertical_horizontal)

# Cria um checkbox para controlar a visibilidade do stem_vertical2 e do stem_horizontal2
ax_check_vertical_horizontal2 = plt.axes([0.1, 0.875, 0.1, 0.05], frameon=False)
check_vertical_horizontal2 = CheckButtons(ax_check_vertical_horizontal2, ['Mostrar/ocultar linha auxiliar - Deslocação da Oferta'], [True])
check_vertical_horizontal2.labels[0].set_fontsize(10)
check_vertical_horizontal2.labels[0].set_bbox(None)

# Função para atualizar a visibilidade do stem_vertical2 e do stem_horizontal2
def update_visibility_vertical_horizontal2(label):
    if check_vertical_horizontal2.get_status()[0]:
        stem_vertical2.set_visible(True)
        stem_horizontal2.set_visible(True)
    else:
        stem_vertical2.set_visible(False)
        stem_horizontal2.set_visible(False)
    fig.canvas.draw_idle()

check_vertical_horizontal2.on_clicked(update_visibility_vertical_horizontal2)

# Cria uma legenda para identificar as linhas/retas
ax.legend((oferta_reta, desloc_oferta_reta, ponto2), ('Oferta', 'Deslocação da Oferta', 'Preço x Quantidade'))

plt.show()