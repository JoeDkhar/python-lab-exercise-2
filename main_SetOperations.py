import module_SetOperations as mso


def get_set_input(prompt):
    """Get a set input from the user."""
    user_input = input(prompt)
    return set(map(int, user_input.split(',')))


def main():
    print("Set Operations Demonstration")

    # Get user input for sets
    set1 = get_set_input("Enter elements for Set1 (comma-separated): ")
    set2 = get_set_input("Enter elements for Set2 (comma-separated): ")

    while True:
        print("\nChoose an operation:")
        print("1. Add element to Set1")
        print("2. Remove element from Set1")
        print("3. Union and Intersection of Set1 and Set2")
        print("4. Difference of Set1 - Set2")
        print("5. Check if Set1 is a subset of Set2")
        print("6. Length of Set1 (without len)")
        print("7. Symmetric Difference of Set1 and Set2")
        print("8. Power Set of Set1")
        print("9. Unique Subsets of Set1")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            element = int(input("Enter element to add to Set1: "))
            print("Set1 before adding element:", set1)
            mso.add_element(set1, element)
            print("Set1 after adding element:", set1)

        elif choice == '2':
            element = int(input("Enter element to remove from Set1: "))
            print("Set1 before removing element:", set1)
            mso.remove_element(set1, element)
            print("Set1 after removing element:", set1)

        elif choice == '3':
            union, intersection = mso.union_intersection(set1, set2)
            print("Union of Set1 and Set2:", union)
            print("Intersection of Set1 and Set2:", intersection)

        elif choice == '4':
            print("Difference of Set1 - Set2:", mso.difference(set1, set2))

        elif choice == '5':
            print("Is Set1 a subset of Set2?", mso.is_subset(set1, set2))

        elif choice == '6':
            print("Length of Set1 (without len):", mso.set_length(set1))

        elif choice == '7':
            print("Symmetric difference of Set1 and Set2:", mso.symmetric_difference(set1, set2))

        elif choice == '8':
            print("Power set of Set1:", mso.power_set(set1))

        elif choice == '9':
            print("Unique subsets of Set1:", mso.unique_subsets(set1))

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
