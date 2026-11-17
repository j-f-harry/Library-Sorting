# type: ignore
"""Uses the library of congress dataset to see things"""

import pandas as pd                     # for reading, manipulating, and displaying data
import matplotlib.pyplot as plt

# from helpers import get_file_stats

def get_class(id: str) -> str:
    """Returns the first alphanumeric characters"""

    result: str = ""
    for c in id:
        if not (c.isalpha() and c.isupper()):
            break
        result += c

    return result

def get_class_counts(ids: list[str]) -> dict[str, int]:
    """Returns the count of each class"""
    classes: list[str] = list(get_class(id) for id in ids)
    class_dict: dict[str, int] = {}
    for c in set(classes):
        class_dict[c] = classes.count(c)
    class_dict = {key: value for key, value in sorted(class_dict.items()) if len(key) <= 3}

    return class_dict

def get_class_subsets(ids: list[str]) -> dict[str, int]:
    """Returns the count of subsets in each class"""

    classes: list[str] = list(get_class(id) for id in ids)
    class_dict: dict[str, set(str)] = {key: set() for key in classes}
    for c in ids:
        class_dict[get_class(c)].add(c)

    return {key: len(value) for key, value in sorted(class_dict.items(), key=lambda item: item[0]) if len(key) <= 3}


df = pd.read_csv(r"res\small_metadata.csv")

id_list: list[str] = list(df["shelf_id"])



#class_dict = dict(sorted(class_dict.items()))




class_sets: dict[str, int] = get_class_subsets(id_list)
print(class_sets)

class_tokens: list[str] = class_sets.keys()
counts: list[int] = class_sets.items()

plt.bar(range(len(class_sets)), list(class_sets.values()), align='center')
plt.xticks(range(len(class_sets)), list(class_sets.keys()), minor=False)
plt.yscale("log")

plt.show()
