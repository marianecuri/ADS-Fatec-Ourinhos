import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons

# Define os parâmetros iniciais
preco_init = 139
renda_init = 2424
outros_produtos_init = 139
expectativa_init = 50
insumos_init = 139
desloc_oferta_init = 0
desloc_demanda_init = 0

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

# Plotagem da função de deslocação da oferta inicial
quantidade = np.linspace(100, 1800, 5000)
desloc_oferta_reta, = ax.plot(quantidade, desloc_oferta(quantidade, preco_init, insumos_init), color='orange', lw=2)
desloc_oferta_ponto, = ax.plot(quantidade, desloc_oferta2(quantidade, preco_init, insumos_init), color='orange', lw=2)
desloc_oferta_ponto.set_visible(False)

# Plotagem da função de oferta
oferta_reta, = ax.plot(quantidade, oferta(quantidade), color='black', lw=2)

# Plotagem da função de deslocação da demanda inicial
quantidade = np.linspace(100, 1800, 5000)
desloc_demanda_reta, = ax.plot(quantidade, desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init), color='blue', lw=2)

# Plotagem da função de demanda
demanda_reta, = ax.plot(quantidade, demanda(quantidade), color='black', lw=2)
desloc_demanda_ponto, = ax.plot(quantidade, desloc_demanda2(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init), color='blue', lw=2)
desloc_demanda_ponto.set_visible(False)

# Título do gráfico e ajuste do espaço para os sliders
plt.title('Gráfico de Equilíbrio de Mercado', y=1.05, fontsize=16, weight='bold')
fig.subplots_adjust(left=0.1, bottom=0.4)

# Cria um slider horizontal para controlar o preço do produto
axpreco = fig.add_axes([0.25, 0.25, 0.5, 0.03])
slider_preco = Slider(
    ax=axpreco,
    label='Preço do Produto (R$)',
    valmin=46,
    valmax=288,
    valinit=preco_init,
    valstep=0.01,
    color = 'mediumaquamarine'
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
    valmin=46,
    valmax=288,
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

# Cria um slider horizontal para controlar o preço dos insumos
axinsumos = fig.add_axes([0.25, 0.05, 0.5, 0.03])
slider_insumos = Slider(
    ax=axinsumos,
    label='Preço dos Insumos Produtivos (R$)',
    valmin=16,
    valmax=288,
    valinit=insumos_init,
    valstep=0.01,
    color = 'sandybrown'
)

# Função que encontra o ponto de equilíbrio entre as retas de oferta e demanda
def encontrar_equilibrio():
    quantidade = np.linspace(100, 1800, 5000)
    desloc_oferta_val = desloc_oferta2(quantidade, 139, slider_insumos.val)
    desloc_demanda_val = desloc_demanda2(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val)
    equilibrio_index = np.argmin(np.abs(desloc_oferta_val - desloc_demanda_val))
    return quantidade[equilibrio_index], desloc_oferta_val[equilibrio_index]
equilibrio_x, equilibrio_y = encontrar_equilibrio()

# Função a ser chamada toda vez que o valor de um slider muda
def update(val):
    if val == slider_preco.val:
        # Atualiza os pontos na reta de oferta e demanda
        ponto_oferta1.set_data([quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])

        ponto_demanda1.set_data([quantidade[np.abs(demanda(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])
        
    if slider_renda.val != slider_renda.valinit or slider_outros_produtos.val != slider_outros_produtos.valinit or slider_expectativa.val != slider_expectativa.valinit or slider_insumos.val != slider_insumos.valinit:
        # Atualiza a função de deslocação da oferta e demanda
        desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, 139, slider_insumos.val))
        desloc_oferta_ponto.set_ydata(desloc_oferta2(quantidade, 139, slider_insumos.val))

        desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val))
        desloc_demanda_ponto.set_ydata(desloc_demanda2(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val))
	
    # Atualiza o ponto na reta de deslocação da oferta e demanda
    ponto_oferta2.set_data([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])

    # Ajusta a visibilidade do ponto_oferta2
    ponto_oferta2.set_visible(ponto_oferta2.get_ydata()[0] >= 16)

    ponto_demanda2.set_data([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
    
    # Atualiza o ponto de equilíbrio
    equilibrio_x, equilibrio_y = encontrar_equilibrio()
    ponto_equilibrio2.set_data([equilibrio_x], [equilibrio_y])
    
    # Atualiza os stemplots verticais
    stem_vertical2.set_xdata([equilibrio_x] * 2)
    stem_vertical2.set_ydata([0, equilibrio_y])
    
    # Atualiza os stemplots horizontais
    stem_horizontal2.set_xdata([0, equilibrio_x])
    stem_horizontal2.set_ydata([equilibrio_y] * 2)
    
    fig.canvas.draw_idle()

# Registra a função de atualização com cada slider
slider_preco.on_changed(update)
slider_renda.on_changed(update)
slider_outros_produtos.on_changed(update)
slider_expectativa.on_changed(update)
slider_insumos.on_changed(update)

# Cria um botão para resetar os sliders aos valores iniciais
axreset = fig.add_axes([0.8, 0.25, 0.1, 0.04])
button = Button(axreset, 'Resetar', color = 'aquamarine', hovercolor='mediumaquamarine')

def reset(event):
    slider_preco.reset()
    slider_renda.reset()
    slider_outros_produtos.reset()
    slider_expectativa.reset()
    slider_insumos.reset()

    desloc_oferta_init = 0
    desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, preco_init, insumos_init))
    desloc_oferta_ponto.set_ydata(desloc_oferta2(quantidade, preco_init, insumos_init))
    desloc_demanda_init = 0
    desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init))
    desloc_demanda_ponto.set_ydata(desloc_demanda2(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init))

    ponto_oferta1.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto_oferta2.set_data([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - preco_init).argmin()]], [preco_init])

    ponto_demanda1.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto_demanda2.set_data([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - preco_init).argmin()]], [preco_init])
    
    stem_vertical2.set_xdata([equilibrio_x] * 2)
    stem_vertical2.set_ydata([0, equilibrio_y])
    
    stem_horizontal2.set_xdata([0, equilibrio_x])
    stem_horizontal2.set_ydata([equilibrio_y] * 2)

button.on_clicked(reset)

# Cria os stemplots
stem_vertical1, = ax.plot([equilibrio_x] * 2, [0, equilibrio_y], '--', color='grey')
stem_vertical2, = ax.plot([equilibrio_x] * 2, [0, equilibrio_y], '--', color='grey')
stem_horizontal1, = ax.plot([0, equilibrio_x], [equilibrio_y] * 2, '--', color='grey')
stem_horizontal2, = ax.plot([0, equilibrio_x], [equilibrio_y] * 2, '--', color='grey')

# Plotagem dos pontos de equilíbrio e dos pontos nas retas de oferta/demanda e de deslocação da oferta/demanda
ponto_oferta2, = ax.plot([desloc_oferta_init + desloc_oferta_ponto.get_xdata()[np.abs(desloc_oferta_ponto.get_ydata() - preco_init).argmin()]], [preco_init], 'yo', markersize=5)
ponto_demanda2, = ax.plot([desloc_demanda_init + desloc_demanda_ponto.get_xdata()[np.abs(desloc_demanda_ponto.get_ydata() - preco_init).argmin()]], [preco_init], 'bo', markersize=5)

ponto_oferta1, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=5)
ponto_demanda1, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=5)

equilibrio_x, equilibrio_y = encontrar_equilibrio()
ponto_equilibrio2, = ax.plot([equilibrio_x], [equilibrio_y], 'ro', markersize=8)
ponto_equilibrio1, = ax.plot([equilibrio_x], [equilibrio_y], 'ro', markersize=8)

# Cria um checkbox para controlar a visibilidade dos pontos de desequilíbrio
ax_check_desequilibrio = plt.axes([0.1, 0.925, 0.1, 0.05], frameon=False)
check_desequilibrio = CheckButtons(ax_check_desequilibrio, ['Mostrar/ocultar Pontos de Desequilíbrio'], [True])
check_desequilibrio.labels[0].set_fontsize(10)
check_desequilibrio.labels[0].set_bbox(None)

# Função para atualizar a visibilidade dos pontos de desequilíbrio
def update_visibility_desequilibrio(label):
    if check_desequilibrio.get_status()[0]:
        ponto_oferta1.set_visible(True)
        ponto_oferta2.set_visible(True)
        ponto_demanda1.set_visible(True)
        ponto_demanda2.set_visible(True)
    else:
        ponto_oferta1.set_visible(False)
        ponto_oferta2.set_visible(False)
        ponto_demanda1.set_visible(False)
        ponto_demanda2.set_visible(False)
    fig.canvas.draw_idle()

check_desequilibrio.on_clicked(update_visibility_desequilibrio)

# Cria um checkbox para controlar a visibilidade do stem_vertical1 e do stem_horizontal1
ax_check_vertical_horizontal = plt.axes([0.1, 0.9, 0.1, 0.05], frameon=False)
check_vertical_horizontal = CheckButtons(ax_check_vertical_horizontal, ['Mostrar/ocultar linha auxiliar - Equilíbrio'], [True])
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
check_vertical_horizontal2 = CheckButtons(ax_check_vertical_horizontal2, ['Mostrar/ocultar linha auxiliar - Deslocação do Equilíbrio'], [True])
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
ax.legend((oferta_reta, demanda_reta, desloc_oferta_reta, desloc_demanda_reta, ponto_oferta2, ponto_demanda2, ponto_equilibrio2), ('Oferta', 'Demanda', 'Deslocação da Oferta', 'Deslocação da Demanda', 'Preço x Quantidade Ofertada', 'Preço x Quantidade Demandada', 'Ponto de Equilíbrio'))

plt.show()