def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    try:
        # Input a list of numbers separated by spaces
        input_str = input("Enter numbers separated by spaces: ")
        input_list = [int(x) for x in input_str.split()]

        # Call the selection_sort function to sort the input list
        selection_sort(input_list)

        # Print the sorted list
        print("Sorted array:", input_list)
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
