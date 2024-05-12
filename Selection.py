import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def read_file(filename):
    with open(filename, 'r') as file:
        data = [int(num) for num in file.read().split()]
    return data

def main():
    filename = "selection.txt"
    data = read_file(filename)
    unsorted_data = data.copy()  
    
    start_time = time.time() 
    selection_sort(data)
    end_time = time.time()  
    elapsed_time = end_time - start_time  
    
    print("Sorted array:", data)
    print("Passing time:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
