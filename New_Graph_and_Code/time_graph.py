import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Graph Traversal
raw_data = {'Prog. Lang': ['0-1 Knapsack', 'OBST'],
        'C++': [0.00144, 0.00116],
        'Java': [0.05145, 0.05935],
        'Python': [0.00906, 0.01615]}
df = pd.DataFrame(raw_data, columns = ['Prog. Lang', 'C++', 'Java', 'Python'])

# Sorting Algorithms
# raw_data = {'Prog. Lang': ['Bubblesort', 'Mergesort'],
#         'C++': [0.00110, 0.00066],
#         'Java': [0.06994, 0.07585],
#         'Python': [0.01608, 0.01651]}
# df = pd.DataFrame(raw_data, columns = ['Prog. Lang', 'C++', 'Java', 'Python'])


pos = list(range(len(df['C++'])))
width = 0.20

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with C++ data,
# in position pos,
plt.bar(pos,
        #using df['C++'] data,
        df['C++'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='blue',
        edgecolor='white',
        # with label the first value in Prog. Lang
        label=df['Prog. Lang'][0])

# Create a bar with Java data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['Java'] data,
        df['Java'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='green',
        edgecolor='white',
        # with label the second value in Prog. Lang
        label=df['Prog. Lang'][1])

# Create a bar with Python data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['Python'] data,
        df['Python'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='red',
        edgecolor='white',
        # with label the third value in Prog. Lang
        label=df['Prog. Lang'][1])

# Set the y axis label
ax.set_ylabel('Execution time (in seconds)')

# Set the chart's title
ax.set_title('Dynamic Programming Algorithms')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['Prog. Lang'])

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['C++'] + df['Java'] + df['Python'])] )

# Adding the legend and showing the plot
plt.legend(['C++', 'Java', 'Python'], loc='upper left')
plt.grid()
# plt.show()
plt.savefig("dp.png")
