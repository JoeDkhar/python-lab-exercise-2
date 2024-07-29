

def add_element(s, elem):
    """Add an element to a set, ensuring no errors if the element is already present."""
    s.add(elem)

def remove_element(s, elem):
    """Remove an element from a set, ensuring no errors if the element is not present."""
    s.discard(elem)  # discard() does not raise an error if the element is not present

def union_intersection(s1, s2):
    """Return the union and intersection of two sets, handling empty sets correctly."""
    union = s1 | s2
    intersection = s1 & s2
    return union, intersection

def difference(s1, s2):
    """Return the difference S1−S2, handling empty sets correctly."""
    return s1 - s2

def is_subset(s1, s2):
    """Check if set S1 is a subset of set S2, handling empty sets correctly."""
    return s1.issubset(s2)

def set_length(s):
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Compute the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    """Compute the power set of a given set."""
    power_set_list = [[]]
    for elem in s:
        power_set_list.extend([subset + [elem] for subset in power_set_list])
    return [set(subset) for subset in power_set_list]

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    def generate_subsets(s):
        if not s:
            return [[]]
        elem = s.pop()
        subsets = generate_subsets(s)
        return subsets + [subset + [elem] for subset in subsets]

    return [set(subset) for subset in generate_subsets(set(s))]
