def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)
    return sorted_arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Example usage:
if __name__ == "__main__":
    try:
        # Input a list of numbers separated by spaces
        input_str = input("Enter numbers separated by spaces: ")
        input_list = [int(x) for x in input_str.split()]

        # Call the merge_sort function to sort the input list
        sorted_list = merge_sort(input_list)

        # Print the sorted list
        print("Sorted array:", sorted_list)
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")