import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

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
    return oferta(quantidade) - (1 * preco) + (1 * insumos)

# Define a função de demanda
def demanda(quantidade):
    return 304 - 0.16 * quantidade

# Define a função que calcula a deslocação da demanda
def desloc_demanda(quantidade, preco, renda, outros_produtos, expectativa):
    return demanda(quantidade) - (1 * preco) + (0.005 * renda - 112) + (1 * outros_produtos) + (3 * expectativa - 50)

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

# Plotagem da função de deslocação da demanda inicial
quantidade = np.linspace(0, 2500, 5000)
desloc_demanda_reta, = ax.plot(quantidade, desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init), color='blue', lw=2)

# Plotagem da função de demanda
demanda_reta, = ax.plot(quantidade, demanda(quantidade), color='black', lw=2)

# Título do gráfico e ajuste do espaço para os sliders
plt.title('Gráfico de Equilíbrio de Mercado', y=1.05, fontsize=16, weight='bold')
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
    color = 'mediumaquamarine'
)

# Cria um slider horizontal para controlar a renda do consumidor
axrenda = fig.add_axes([0.25, 0.20, 0.5, 0.03])
slider_renda = Slider(
    ax=axrenda,
    label='Renda do Consumidor (R$)',
    valmin=0,
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
    valmin=0,
    valmax=300,
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
    valmin=0,
    valmax=300,
    valinit=insumos_init,
    valstep=0.01,
    color = 'sandybrown'
)

# Função que encontra o ponto de equilíbrio entre as retas de oferta e demanda
def encontrar_equilibrio():
    quantidade = np.linspace(0, 2500, 5000)
    desloc_oferta_val = desloc_oferta(quantidade, 139, slider_insumos.val)
    desloc_demanda_val = desloc_demanda(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val)
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

        desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, 139, slider_renda.val, slider_outros_produtos.val, slider_expectativa.val))
	
    # Atualiza o ponto na reta de deslocação da oferta e demanda
    ponto_oferta2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])

    ponto_demanda2.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
    
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
    desloc_demanda_init = 0
    desloc_demanda_reta.set_ydata(desloc_demanda(quantidade, preco_init, renda_init, outros_produtos_init, expectativa_init))

    ponto_oferta1.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto_oferta2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])

    ponto_demanda1.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    ponto_demanda2.set_data([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init])
    
    stem_vertical2.set_xdata([equilibrio_x] * 2)
    stem_vertical2.set_ydata([0, equilibrio_y])
    
    stem_horizontal2.set_xdata([0, equilibrio_x])
    stem_horizontal2.set_ydata([equilibrio_y] * 2)

button.on_clicked(reset)

# Cria os stemplots
stem_vertical1, = ax.plot([equilibrio_x] * 2, [0, equilibrio_y], 'k--', color='grey')
stem_vertical2, = ax.plot([equilibrio_x] * 2, [0, equilibrio_y], 'k--', color='grey')
stem_horizontal1, = ax.plot([0, equilibrio_x], [equilibrio_y] * 2, 'k--', color='grey')
stem_horizontal2, = ax.plot([0, equilibrio_x], [equilibrio_y] * 2, 'k--', color='grey')

# Plotagem dos pontos de equilíbrio e dos pontos nas retas de oferta/demanda e de deslocação da oferta/demanda
ponto_oferta2, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'yo', markersize=5)
ponto_demanda2, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'bo', markersize=5)

ponto_oferta1, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=5)
ponto_demanda1, = ax.plot([desloc_demanda_init + desloc_demanda_reta.get_xdata()[np.abs(desloc_demanda_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ko', markersize=5)

equilibrio_x, equilibrio_y = encontrar_equilibrio()
ponto_equilibrio2, = ax.plot([equilibrio_x], [equilibrio_y], 'ro', markersize=7)
ponto_equilibrio1, = ax.plot([equilibrio_x], [equilibrio_y], 'ro', markersize=7)

# Cria uma legenda para identificar as linhas/retas
ax.legend((oferta_reta, demanda_reta, desloc_oferta_reta, desloc_demanda_reta, ponto_oferta2, ponto_demanda2, ponto_equilibrio2), ('Oferta', 'Demanda', 'Deslocação da Oferta', 'Deslocação da Demanda', 'Preço x Quantidade Ofertada', 'Preço x Quantidade Demandada', 'Ponto de Equilíbrio'))

plt.show()