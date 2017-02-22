import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_bar(result_dict,title):

    labels = result_dict.keys()

    quants = result_dict.values()
    #
    # draw_bar(labels, quants)


    fig = plt.figure()
    plt.bar(labels, quants, 0.4, color="green")
    plt.xlabel('spen time')
    plt.ylabel('Times')
    plt.title(title)

    plt.savefig(title + ".png")
    plt.close()