import matplotlib.pyplot as plt
import numpy as np
import string
import sys

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

def show_graph(yvals):
    plt.plot(yvals)
    f = lambda x, alpha: max(yvals) * 1/(x**alpha)
    x = np.linspace(1, len(yvals))
    for alpha in range(11):
        plt.plot(x,f(x, alpha/10))
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python counter.py <file>")
        sys.exit()
    
    counter = count_symbols(sys.argv[1])
    show_graph(counter)