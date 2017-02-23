import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_bar(result_dict,title):

    labels = [int(x) for x in result_dict.keys()]

    quants = [int(y) for y in result_dict.values()]
    print (labels)
    print(quants)

    #
    # draw_bar(labels, quants)


    fig = plt.figure()
    plt.bar(labels, quants, 0.4, color="green")
    plt.xlabel('Times')
    plt.ylabel('Spent Time')
    plt.title(title)

    plt.savefig(title + ".png")
    plt.close()