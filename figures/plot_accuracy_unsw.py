from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=18)
machines = ['SVM', 'Embeddings', 'Wide & Deep', 'AC-GAN']
accuracy = [81.2564, 86.9079, 81.4434, 76.9251]
width = 0.4
ind = np.arange(len(machines))

fig, ax = plt.subplots()
rects = ax.bar(ind + width / 2, accuracy, width, color='b')
ax.set_ylabel('Accuracy(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(machines)
ax.set_xlim([-0.5, len(machines)])
ax.set_ylim([72, 89])
plt.grid()


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
                '%.2f' % height, ha='center', va='bottom')

autolabel(rects)
plt.tight_layout()
# plt.savefig('comp_accuracy_unsw.pdf', fmt='pdf')
plt.show()
