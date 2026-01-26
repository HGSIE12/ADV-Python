cat_a = [1, 2, 3, 4, 5]
cat_b = [10, 20, 30]

def calculate_stats(data):
    mean = sum(data) / len(data)
    max_value = max(data)
    return mean, max_value


def menu():
    while True:
        print("1. List1: [1, 2, 3, 4, 5]")
        print("2. List2: [10, 20, 30]")
        print("3. Exit")

        choice = input("\nWhich list would you like to get mean and max? ")

        if choice == "1":
            mean, max_value = calculate_stats(cat_a)
            print("\nThe mean is:", mean)
            print("The max is:", max_value)

        elif choice == "2":
            mean, max_value = calculate_stats(cat_b)
            print("\nThe mean is:", mean)
            print("The max is:", max_value)

        elif choice == "3":
            break

menu()