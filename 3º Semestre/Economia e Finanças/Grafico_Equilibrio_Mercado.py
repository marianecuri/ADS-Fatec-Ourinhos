import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Define initial parameters
init_price = 0
init_comp_price = 0
init_demand_shift = 0

# Define demand function
def demand(quantity):
    return 200 - 0.4 * quantity

# Define function to calculate shifted demand
def shifted_demand(quantity, price, comp_price):
    return demand(quantity + init_demand_shift) - 0.2 * price + 0.1 * comp_price

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
ax.set_xlabel('Quantidade')
ax.set_ylabel('Preço')
ax.set_xlim([0, 500])
ax.set_ylim([0, 500])

# Plot demand function
quantity = np.linspace(0, 500, 1000)
demand_line, = ax.plot(quantity, demand(quantity), color='blue', lw=2)

# Plot initial shifted demand function
shifted_demand_line, = ax.plot(quantity, shifted_demand(quantity, init_price, init_comp_price), color='black', lw=2)

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.4)

# Make a horizontal slider to control the product price.
axprice = fig.add_axes([0.3, 0.25, 0.5, 0.03])
price_slider = Slider(
    ax=axprice,
    label='Preço do Produto',
    valmin=0,
    valmax=500,
    valinit=init_price,
)

# Make a horizontal slider to control the competing product price.
axcomp_price = fig.add_axes([0.3, 0.15, 0.5, 0.03])
comp_price_slider = Slider(
    ax=axcomp_price,
    label='Preço de Produtos Concorrentes',
    valmin=0,
    valmax=500,
    valinit=init_comp_price,
)

# The function to be called anytime a slider's value changes
def update(val):
    # Update shifted demand function and plot
    shifted_demand_line.set_ydata(shifted_demand(quantity, price_slider.val, comp_price_slider.val))
    # Update red point on shifted demand line
    point.set_data([init_demand_shift + shifted_demand_line.get_xdata()[np.abs(shifted_demand_line.get_ydata() - price_slider.val).argmin()], price_slider.val])
    fig.canvas.draw_idle()

# register the update function with each slider
price_slider.on_changed(update)
comp_price_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    price_slider.reset()
    comp_price_slider.reset()
button.on_clicked(reset)

# Plot red point on initial shifted demand line
point, = ax.plot([init_demand_shift + shifted_demand_line.get_xdata()[np.abs(shifted_demand_line.get_ydata() - init_price).argmin()]], [init_price], 'ro')

plt.show()
