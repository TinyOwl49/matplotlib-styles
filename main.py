import matplotlib.pyplot as plt

style_list = plt.style.available

for style in style_list:
    plt.style.use(style)

    fig, ax = plt.subplots()
    ax.plot([1,2], [6,3])
    ax.plot([1,2], [4,5])
    ax.plot([1,2], [3,4])
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    ax.set_title(style+" style")
    ax.legend(["1", "2", "3"], title="Legend")
    plt.show()
    fig.savefig("images/"+style+".png")
