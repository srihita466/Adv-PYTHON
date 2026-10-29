import numpy as np

def main():
    # 1. Create a one-dimensional array containing numbers from 1 to 10
    arr = np.arange(1, 11)
    print("Original Array:", arr)
    print("-" * 40)
    
    # 2. Perform slicing operations
    sub_slice = arr[2:7]
    every_second = arr[::2]
    print("Slice [2:7]:", sub_slice)
    print("Every second element:", every_second)
    print("-" * 40)
    
    # 3. Compute statistical measures
    total_sum = np.sum(arr)
    mean_val = np.mean(arr)
    max_val = np.max(arr)
    min_val = np.min(arr)
    
    print(f"Sum: {total_sum}")
    print(f"Mean: {mean_val}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")
    print("-" * 40)
    
    # 4. Apply broadcasting to modify the array elements
    # Adds 5 to every element in the array simultaneously without a loop
    broadcasted_arr = arr + 5
    print("Modified Array (arr + 5):", broadcasted_arr)

if __name__ == "__main__":
    main()