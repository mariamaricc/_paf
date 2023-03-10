import matplotlib.pyplot as plt
import numpy as np


def pravac(x1,y1,x2,y2):
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k*x1
    print("y = {}x + {}".format(k,l))

    fig = plt.figure()
    ax = plt.axes()
    plt.plot((x1,x2),(y1,y2), 'o-r')

    ax.set(xlabel='x', ylabel='y',
       title='Pravac')
    ax.grid()

    prikaz = input("1.prikazi na ekranu ili 2. spremi kao pdf: ")
    if prikaz == "1":
        plt.show()
    elif prikaz == "2":
        spremanje = input("pod kojim imenom zelite spremiti file? ")
        fig.savefig("{}.pdf".format(spremanje))

pravac(x1 = 1, y1 = 2, x2 = 5, y2 = 4)