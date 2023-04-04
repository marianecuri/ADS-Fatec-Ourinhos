import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define os parâmetros iniciais
preco_init = 139
outros_produtos_init = 139
renda_init = 2424
desloc_oferta_init = 0

def GraficoOferta():

    # Define a função de oferta
    def oferta(quantidade):
        return 304 - 0.16 * quantidade

    # Define a função que calcula a deslocação da oferta
    def desloc_oferta(quantidade, preco, outros_produtos, renda):
        return oferta(quantidade + desloc_oferta_init) - 1 * preco + outros_produtos - 1 * preco + (2/35) * renda

    # Cria a figura e a linha/reta a ser manipulada
    fig, ax = plt.subplots()
    ax.set_xlabel('Quantidade (Unidades)')
    ax.set_ylabel('Preço (R$)')
    ax.set_xlim([0, 2500])
    ax.set_ylim([0, 250])

    # Plotagem da função de oferta
    quantidade = np.linspace(0, 5000, 10000)
    oferta_reta, = ax.plot(quantidade, oferta(quantidade), color='blue', lw=2)

    # Plotagem da função de deslocação da oferta inicial
    desloc_oferta_reta, = ax.plot(quantidade, desloc_oferta(quantidade, preco_init, outros_produtos_init, renda_init), color='black', lw=2)

    # Título do gráfico e ajuste do espaço para os sliders
    plt.title('Gráfico de Oferta')
    fig.subplots_adjust(left=0.25, bottom=0.4)

    # Cria um slider horizontal para controlar o preço do produto
    axPreco = fig.add_axes([0.3, 0.25, 0.5, 0.03])
    slider_preco = Slider(
        ax=axPreco,
        label='Preço do Produto (R$)',
        valmin=0,
        valmax=300,
        valinit=preco_init,
        valstep=0.01,
    )

    # Cria um slider horizontal para controlar o preço de produtos substitutos
    axOutros_produtos = fig.add_axes([0.3, 0.20, 0.5, 0.03])
    slider_outros_produtos = Slider(
        ax=axOutros_produtos,
        label='Preço de Produtos Substitutos (R$)',
        valmin=0,
        valmax=300,
        valinit=outros_produtos_init,
        valstep=0.01,
    )

    # Cria um slider horizontal para controlar a renda do consumidor
    axRenda = fig.add_axes([0.3, 0.15, 0.5, 0.03])
    slider_renda = Slider(
        ax=axRenda,
        label='Renda do Consumidor (R$)',
        valmin=0,
        valmax=50000,
        valinit=renda_init,
        valstep=0.01,
    )

    # Função a ser chamada toda vez que o valor de um slider muda
    def update(val):
        if val == slider_preco.val:
            # Atualiza o ponto vermelho na reta de oferta
            ponto1.set_data([quantidade[np.abs(oferta(quantidade) - slider_preco.val).argmin()]], [slider_preco.val])

            # Atualiza o ponto vermelho na reta de deslocação da oferta
            ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])
                        
        if slider_outros_produtos.val != slider_outros_produtos.valinit or slider_renda.val != slider_renda.valinit:
            # Atualiza a função de deslocação da oferta
            desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, slider_preco.val, slider_outros_produtos.val, slider_renda.val))

            # Atualiza o ponto vermelho na reta de deslocação da oferta
            ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - slider_preco.val).argmin()]], [slider_preco.val])

        fig.canvas.draw_idle()

    # Registra a função de atualização com cada slider
    slider_preco.on_changed(update)
    slider_outros_produtos.on_changed(update)
    slider_renda.on_changed(update)

    # Cria um `matplotlib.widgets.Button` para resetar os sliders aos valores iniciais
    resetax = fig.add_axes([0.85, 0.05, 0.1, 0.04])
    button = Button(resetax, 'Resetar', hovercolor='0.975')

    def reset(event):
        slider_preco.reset()
        slider_outros_produtos.reset()
        slider_renda.reset()
        desloc_oferta_init = 0
        desloc_oferta_reta.set_ydata(desloc_oferta(quantidade, preco_init, outros_produtos_init, renda_init))
        ponto1.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
        ponto2.set_data([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init])
        button.on_clicked(reset)

    # Plotagem do ponto vermelho na reta de deslocação da oferta inicial
    ponto1, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ro')
    ponto2, = ax.plot([desloc_oferta_init + desloc_oferta_reta.get_xdata()[np.abs(desloc_oferta_reta.get_ydata() - preco_init).argmin()]], [preco_init], 'ro')

    # Cria uma legenda para identificar as linhas/retas
    ax.legend((oferta_reta, desloc_oferta_reta), ('Oferta', 'Deslocação da oferta'))

    plt.show()

plt.show()