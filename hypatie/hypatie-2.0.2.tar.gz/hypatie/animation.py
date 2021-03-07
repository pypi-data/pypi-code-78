import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D, proj3d

def play(bodies, names, colors, sizes, path=True, legend=True, interval=20):
    """
    Plays animation from positions.
    
    Arguments
    ---------
    bodies : list
        targer bodies returned from Vector or Observer classes
    names : list
        name of bodies
    colors : list
        color of bodies
    sizes : list
        size of bodies
    path : bool
        whether or not draw the trajectory path of bodies; default True.
    legend : bool
        legend of the plot; default True.
    interval : int
        time interval between sequences, greater means slower. default 20.

    Returns
    -------
    matplotlib.animation.FuncAnimation object
    """
    
    for b in bodies:
        if len(b.time)!=len(bodies[0].time):
            raise Exception('Number of steps are not equal for all bodies!')

    dates = bodies[0].time

    minxs = min([vec.x.min() for vec in bodies])
    minys = min([vec.y.min() for vec in bodies])
    minzs = min([vec.z.min() for vec in bodies])
    maxxs = max([vec.x.max() for vec in bodies])
    maxys = max([vec.y.max() for vec in bodies])
    maxzs = max([vec.z.max() for vec in bodies])

    fig = plt.figure(figsize=plt.figaspect(0.5)*1.2)
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)
    ax.tick_params(axis='z', labelsize=8)

    txt = ax.text(minxs, maxys, maxzs, '')

    lines = []

    alpha = 0.2 if path else 0

    for i in range(len(bodies)):
        ax.plot(bodies[i].x, bodies[i].y, bodies[i].z, colors[i], alpha=alpha)
        lines.append(ax.plot(bodies[i].x[0:2], bodies[i].y[0:2], bodies[i].z[0:2],
                             color=colors[i], marker='o', markersize=sizes[i],
                             label=names[i])[0])

    def init():
        for line in lines:
            line.set_xdata(np.array([]))
            line.set_ydata(np.array([]))
            line.set_3d_properties(np.array([]))
        return lines

    def animate(i):
        for j,line in enumerate(lines):
            line.set_xdata(bodies[j].x[i])
            line.set_ydata(bodies[j].y[i])
            line.set_3d_properties(bodies[j].z[i])
        txt.set_text(dates[i].isoformat().replace('T', ' '))
        return lines + [txt]

    plt.locator_params(axis='x', nbins=7)
    plt.locator_params(axis='y', nbins=7)
    plt.locator_params(axis='z', nbins=7)

    if legend:
        plt.legend(loc='upper left')
    plt.grid(True)

    anim = FuncAnimation(fig, animate, init_func=init,
                         frames=len(dates), interval=interval,
                         blit=True, repeat=True)
    return anim
