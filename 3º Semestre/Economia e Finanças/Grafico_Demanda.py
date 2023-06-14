import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons

# Define os parâmetros iniciais
preco_init = 139
renda_init = 2424
outros_produtos_init = 139
expectativa_init = 50
desloc_demanda_init = 0

# Define a função de demanda
def demanda(quantidade):
    return 304 - 0.16 * quantidade

# Define a função que calcula a deslocação da demanda
def desloc_demanda(quantidade, preco, renda, outros_produtos, expectativa):
    desloc_val = demanda(quantidade) - (1 * preco) + (0.005 * renda - 112) + (1 * outros_produtos) + (3 * expectativa - 50)
    desloc_val = np.where(desloc_val < 16, np.nan, desloc_val)
    return desloc_val
    
def desloc_demanda2(quantidade, preco, renda, outros_produtos, expectativa):
    return demanda(quantidade) - (1 * preco) + (0.005 * renda - 112) + (1 * outros_produtos) + (3 * expectativa - 50)

# Cria a figura e a linha/reta a ser manipulada
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade (Unidades)')
ax.set_ylabel('Preço (R$)')
ax.set_xlim([0, 1800])
ax.set_ylim([0, 300])
ax.set_xticks(np.arange(0, 1800, 100))
ax.set_yticks(np.arange(0, 300, 25))

# Plotagem da função de deslocação da demanda inicial
quantidade = np.linspace(100, 1800, 5000)
preco = np.linspace(15, 315, 5000)
desloc_demanda_reta, = ax.plot(quantidade, desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init), color='blue', lw=2)
desloc_demanda_ponto, = ax.plot(quantidade, desloc_demanda2(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init), color='blue', lw=2)
desloc_demanda_ponto.set_visible(False)

# Plotagem da função de demanda
demanda_reta, = ax.plot(quantidade, demanda(quantidade), color='black', lw=2)

# Título do gráfico e ajuste do espaço para os sliders
plt.title('Gráfico da Curva de Demanda', y=1.05, fontsize=16, weight='bold')
fig.subplots_adjust(left=0.1, bottom=0.4)

# Cria um slider horizontal para controlar o preço do produto
axpreco = fig.add_axes([0.25, 0.25, 0.5, 0.03])
slider_preco = Slider(
    ax=axpreco,
    label='Preço do Produto (R$)',
    valmin=16,
    valmax=288,
    valinit=preco_init,
    valstep=0.01,
    color = 'cornflowerblue'
)

# Cria um slider horizontal para controlar a renda do consumidor
axrenda = fig.add_axes([0.25, 0.20, 0.5, 0.03])
slider_renda = Slider(
    ax=axrenda,
    label='Renda do Consumidor (R$)',
    valmin=100,
    valmax=50000,
    valinit=renda_init,
    valstep=0.01,
    color = 'cornflowerblue'
)

# Cria um slider horizontal para controlar o preço de produtos substitutos
axoutros_produtos = fig.add_axes([0.25, 0.15, 0.5, 0.03])
slider_outros_produtos = Slider(
    ax=axoutros_produtos,
    label='Preço de Produtos Substitutos (R$)',
    valmin=16,
    valmax=260,
    valinit=outros_produtos_init,
    valstep=0.01,
    color = 'cornflowerblue'
)

# Cria um slider horizontal para controlar a expectativa do consumidor
axexpectativa = fig.add_axes([0.25, 0.10, 0.5, 0.03])
slider_expectativa = Slider(
    ax=axexpectativa,
    label='Expectativa do Consumidor (%)',
    valmin=0,
    valmax=100,
    valinit=expectativa_init,
    valstep=0.01,
    color = 'cornflowerblue'
)

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza o ponto na reta de demanda
        ponto1.set_data([quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])
        
    if slider_renda.val != slider_renda.valinit or slider_outros_produtos.val != slider_outros_produtos.valinit or slider_expectativa.val != slider_expectativa.valinit:
        # Atualiza a função de deslocação da demanda
        desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val))
        desloc_demanda_ponto.set_ydata(desloc_demanda2(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val))
	
    # Atualiza o ponto na reta de deslocação da demanda
    ponto2.set_data([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
    
    # Atualiza os stemplots verticais
    stem_vertical1.set_xdata([quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]] * 2)
    stem_vertical1.set_ydata([0, slider_preco.val])
        
    stem_vertical2.set_xdata([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]] * 2)
    stem_vertical2.set_ydata([0, slider_preco.val])
        
    # Atualiza os stemplots horizontais
    stem_horizontal1.set_xdata([0, quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]])
    stem_horizontal1.set_ydata([slider_preco.val] * 2)

    stem_horizontal2.set_xdata([0, desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]])
    stem_horizontal2.set_ydata([slider_preco.val] * 2)
    
    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_renda.on_changed(update)
slider_outros_produtos.on_changed(update)
slider_expectativa.on_changed(update)

# Cria um botão para resetar os sliders aos valores iniciais
axreset = fig.add_axes([0.8, 0.25, 0.1, 0.04])
button = Button(axreset, 'Resetar', color = 'lightsteelblue', hovercolor='cornflowerblue')

def reset(event):
    slider_preco.reset()
    slider_renda.reset()
    slider_outros_produtos.reset()
    slider_expectativa.reset()
    
    desloc_demanda_init = 0
    desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init))
    desloc_demanda_ponto.set_ydata(desloc_demanda2(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init))
    
    ponto1.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto2.set_data([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - preco_init).argmin()]], [preco_init])
    
    stem_vertical1.set_xdata([quantidade[np.abs(demanda(quantidade) - preco_init).argmin()]] * 2)
    stem_vertical1.set_ydata([0, preco_init])
    stem_vertical2.set_xdata([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]] * 2)
    stem_vertical2.set_ydata([0, slider_preco.val])
    
    stem_horizontal1.set_xdata([0, quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]])
    stem_horizontal1.set_ydata([slider_preco.val] * 2)
    stem_horizontal2.set_xdata([0, desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]])
    stem_horizontal2.set_ydata([slider_preco.val] * 2)
    
button.on_clicked(reset)

# Cria os stemplots
stem_vertical1, = ax.plot([quantidade[np.abs(demanda(quantidade) - preco_init).argmin()]] * 2, [0, preco_init], '--', color='grey')
stem_vertical2, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]] * 2, [0, preco_init], '--', color='grey')
stem_horizontal1, = ax.plot([0, quantidade[np.abs(demanda(quantidade) - preco_init).argmin()]], [preco_init] * 2, '--', color='grey')
stem_horizontal2, = ax.plot([0, desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init] * 2, '--', color='grey')

# Plotagem dos pontos nas retas de demanda e de deslocação da demanda inicial
ponto2, = ax.plot([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - preco_init).argmin()]], [preco_init], 'bo', markersize=7)
ponto1, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=7)

# Cria um checkbox para controlar a visibilidade do stem_vertical1 e do stem_horizontal1
ax_check_vertical_horizontal = plt.axes([0.1, 0.9, 0.1, 0.05], frameon=False)
check_vertical_horizontal = CheckButtons(ax_check_vertical_horizontal, ['Mostrar/ocultar linha auxiliar - Demanda'], [True])
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
check_vertical_horizontal2 = CheckButtons(ax_check_vertical_horizontal2, ['Mostrar/ocultar linha auxiliar - Deslocação da Demanda'], [True])
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
ax.legend((demanda_reta, desloc_demanda_reta, ponto2), ('Demanda', 'Deslocação da Demanda', 'Preço x Quantidade'))

plt.show()