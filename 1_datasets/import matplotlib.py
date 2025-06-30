import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
nodes = ["Entrepreneur", "Platform", "Activity", "Support/Barrier", "Impact"]
arrows = [(0,1), (1,2), (2,3), (3,4)]

def update(frame):
    ax.clear()
    ax.set_xlim(0, 5); ax.set_ylim(0, 5)
    for i, node in enumerate(nodes):
        ax.text(i+1, 3, node, ha='center')
    if frame > 0:  # Animate arrows sequentially
        for j in range(min(frame, len(arrows))):
            ax.annotate("", xy=(arrows[j][0]+1, 3), xytext=(arrows[j][1]+1, 3),
                        arrowprops=dict(arrowstyle="->"))
    return ax

ani = animation.FuncAnimation(fig, update, frames=5, interval=1000)
ani.save('model_flow.gif', writer='pillow')
