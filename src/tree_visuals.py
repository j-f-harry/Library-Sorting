# type: ignore
"""Draws the binary search tree for P's subclasses and highlights the path to a target.

The tree is built entirely from binary_search(): searching for an item returns every
middle it checked, so the last one is the item itself, the one before it is its parent,
and the number of steps tells us how deep it sits in the tree.
"""

import matplotlib.pyplot as plt

from binary_search import binary_search, get_subclasses

CLASS = "P"     # which class's subclasses to search
TARGET = "PH"   # what to search for

items = get_subclasses(CLASS)
_, path = binary_search(items, TARGET)

plt.figure(figsize=(10, 5))
for i, item in enumerate(items):
    _, checked = binary_search(items, item)   
    depth = len(checked) - 1                
    on_path = i in path
    color = "red" if on_path else "gray"

    if len(checked) > 1:                      # every node except the root has a parent
        parent = checked[-2]
        plt.plot([parent, i], [-(depth - 1) - 0.15, -depth + 0.15], color=color,
                 lw=2 if on_path else 1)

    # x = position in the sorted list, y = number of steps to reach it
    plt.text(i, -depth, item, ha="center", va="center", fontsize=12,
             color=color, weight="bold" if on_path else "normal")

plt.title(f"Binary search for {TARGET}: {len(path)} steps among {len(items)} subclasses", pad=20)
plt.axis("off")
plt.show()
