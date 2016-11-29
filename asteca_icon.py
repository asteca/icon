
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

cmd_xy = []
with open('stars.DAT', 'r') as f:
    for line in f:
        if not line.startswith('#'):
            l = line.split()
            cmd_xy.append([float(l[1]), float(l[0])])

fig = plt.figure(figsize=(25, 25))
ax = fig.add_subplot(111, aspect='auto')
ax.set_axis_off()
plt.scatter(zip(*cmd_xy)[0], zip(*cmd_xy)[1], c='grey', s=300,
            edgecolor='none')
e = Ellipse(xy=(0.77, 19.3), width=4.5, height=9, angle=0., lw=45, fc='None',
            edgecolor='k')
ax.add_artist(e)
plt.xlim(-3., 6)
plt.ylim(28, 10)
plt.savefig('asteca_icon.png', dpi=300, bbox_inches='tight')
