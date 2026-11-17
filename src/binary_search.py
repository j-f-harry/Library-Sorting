# type: ignore
"""Binary search over sorted Library of Congress subclasses (e.g. PA, PB, ..., PZ)."""

import re

import pandas as pd


def get_subclasses(letter: str) -> list[str]:
    """Returns the sorted, unique subclasses of one class, e.g. 'P' -> ['PA', 'PB', ..., 'PZ']."""
    ids = pd.read_csv("res/small_metadata.csv", usecols=["shelf_id"])["shelf_id"].dropna()
    found = {m[0] for s in ids if (m := re.match(r"[A-Z]{2}", s)) and m[0][0] == letter}
    return sorted(found)


def binary_search(items: list[str], target: str) -> tuple[int, list[int]]:
    """Returns (index of target or -1, every middle index checked along the way)."""
    low, high = 0, len(items) - 1
    checked = []
    while low <= high:
        mid = (low + high) // 2
        checked.append(mid)
        if items[mid] == target:
            return mid, checked
        if items[mid] < target:
            low = mid + 1    
        else:
            high = mid - 1   
    return -1, checked


if __name__ == "__main__":
    subclasses = get_subclasses("P")
    target = "PE"
    index, checked = binary_search(subclasses, target)

    print("Sorted list:", subclasses)
    for step, mid in enumerate(checked, 1):
        print(f"Step {step}: check {subclasses[mid]}")
    print(f"Found {target} at index {index} in {len(checked)} steps "
          f"(a linear search would take {index + 1})")
