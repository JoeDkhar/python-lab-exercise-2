

import module_ListFunction as mlf


def demonstrate_functions():
    # Example lists
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = [7, 8, 9, 10, 11, 12, 13]
    list3 = [10, 20, 30, 40, 50, 60]

    # Demonstrate find_max
    print("Max of list1:", mlf.find_max(list1))

    # Demonstrate find_min
    print("Min of list2:", mlf.find_min(list2))

    # Demonstrate calculate_sum
    print("Sum of list3:", mlf.calculate_sum(list3))

    # Demonstrate compute_average
    print("Average of list1:", mlf.compute_average(list1))

    # Demonstrate find_median
    print("Median of list1:", mlf.find_median(list1))
    print("Median of list2:", mlf.find_median(list2))
    print("Median of list3:", mlf.find_median(list3))


# Run the demonstration
if __name__ == "__main__":
    demonstrate_functions()
