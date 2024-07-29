# module_ListFunction.py

def find_max(lst):
    """the maximum value in the given list."""
    if not lst:
        raise ValueError("The list is empty")
    return max(lst)

def find_min(lst):
    """the minimum value in the given list."""
    if not lst:
        raise ValueError("The list is empty")
    return min(lst)

def calculate_sum(lst):
    """Calculate the sum of all elements in the list."""
    return sum(lst)

def compute_average(lst):
    """Compute the average of the list."""
    if not lst:
        raise ValueError("The list is empty")
    return sum(lst) / len(lst)

def find_median(lst):
    """Determine the median of a list."""
    if not lst:
        raise ValueError("The list is empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
