import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import string
import sys

fig = plt.figure()
ax = fig.add_subplot(111)

def count_symbols(file_name):
    counter = {}

    with open(file_name) as file:
        for line in file:
            for symbol in line.strip():
                if symbol not in string.ascii_letters:
                    continue
                if symbol not in counter.keys():
                    counter[symbol] = 0
                counter[symbol] += 1
    return sorted(counter.values(), reverse=True)

def f(c, x, alpha, q):
    return c / ((x + q) ** alpha)

def slider_on_changed(val):
    f_line.set_ydata(f(slider_c.val, x, slider_alpha.val, slider_q.val))
    fig.canvas.draw_idle()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python counter.py <file>")
        sys.exit()
    
    global slider_c
    global slider_alpha
    global slider_q
    global x
    global f_line
    
    fig.subplots_adjust(left=0.25, bottom=0.25)
    
    symbol_counter = count_symbols(sys.argv[1])
    
    c_min = 1
    c_max = symbol_counter[0] * 3
    c_init = symbol_counter[0]

    alpha_min = 0
    alpha_max = 10
    alpha_init = 1

    q_min = - 10
    q_max = 10
    q_init = q_min + (q_max - q_min) / 2
    
    slider_c_ax = plt.axes([0.1, 0.05, 0.8, 0.05])
    slider_c = Slider(slider_c_ax, "c", c_min, c_max, valinit=c_init)
    
    slider_alpha_ax = plt.axes([0.1, 0.10, 0.8, 0.05])
    slider_alpha = Slider(slider_alpha_ax, "alpha", alpha_min, alpha_max, valinit=alpha_init)
    
    slider_q_ax = plt.axes([0.1, 0.15, 0.8, 0.05])
    slider_q = Slider(slider_q_ax, "q", q_min, q_max, valinit=q_init)
    
    symbol_line, = ax.plot(symbol_counter)
    x = np.linspace(1, len(symbol_counter))
    f_line, = ax.plot(x, f(c_init, x, alpha_init, q_init))
    
    slider_c.on_changed(slider_on_changed)
    slider_alpha.on_changed(slider_on_changed)
    slider_q.on_changed(slider_on_changed)
    
    plt.show()
