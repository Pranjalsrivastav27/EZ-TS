def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
if __name__ == "__main__":
    try:
        # Input a list of numbers separated by spaces
        input_str = input("Enter numbers separated by spaces: ")
        input_list = [int(x) for x in input_str.split()]

        # Call the quick_sort function to sort the input list
        sorted_list = quick_sort(input_list)

        # Print the sorted list
        print("Sorted array:", sorted_list)
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
