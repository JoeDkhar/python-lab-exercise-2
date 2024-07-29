def get_dict_input(prompt):
    """Prompt user to enter a dictionary in a specific format."""
    user_input = input(prompt)
    # Convert the input string to a dictionary
    try:
        # Convert the input string to a dictionary
        dictionary = eval(user_input)
        if not isinstance(dictionary, dict):
            raise ValueError("The input is not a dictionary.")
        return dictionary
    except Exception as e:
        print(f"Error: {e}")
        return {}


def merging_Dict(*args):
    """Merges multiple dictionaries into one."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict


def common_keys(*args):
    """Finds common keys in multiple dictionaries."""
    common_keys_set = set(args[0].keys())
    for d in args[1:]:
        common_keys_set &= set(d.keys())
    return common_keys_set


def invert_dict(d):
    """Inverts a dictionary, swapping keys and values."""
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict


def common_items(*args):
    """Finds common key-value pairs across multiple dictionaries."""
    common_items_set = set(args[0].items())
    for d in args[1:]:
        common_items_set &= set(d.items())
    return common_items_set


def main():
    print("Dictionary Operations Demonstration")

    while True:
        print("\nChoose an operation:")
        print("1. Merge Dictionaries")
        print("2. Find Common Keys")
        print("3. Invert Dictionary")
        print("4. Find Common Key-Value Pairs")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num_dicts = int(input("Enter the number of dictionaries to merge: "))
            dicts = [get_dict_input(f"Enter dictionary {i + 1} (e.g., {'{a: 1, b: 2}'}): ") for i in range(num_dicts)]
            merged = merging_Dict(*dicts)
            print("Merged Dictionary:", merged)

        elif choice == '2':
            num_dicts = int(input("Enter the number of dictionaries to find common keys: "))
            dicts = [get_dict_input(f"Enter dictionary {i + 1} (e.g., {'{a: 1, b: 2}'}): ") for i in range(num_dicts)]
            common = common_keys(*dicts)
            print("Common Keys:", common)

        elif choice == '3':
            dictionary = get_dict_input("Enter dictionary to invert (e.g., {'a': 1, 'b': 2}): ")
            inverted = invert_dict(dictionary)
            print("Inverted Dictionary:", inverted)

        elif choice == '4':
            num_dicts = int(input("Enter the number of dictionaries to find common key-value pairs: "))
            dicts = [get_dict_input(f"Enter dictionary {i + 1} (e.g., {'{a: 1, b: 2}'}): ") for i in range(num_dicts)]
            common = common_items(*dicts)
            print("Common Key-Value Pairs:", common)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
