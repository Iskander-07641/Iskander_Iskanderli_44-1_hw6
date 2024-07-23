
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            print(f"Элемент найден: {target} на позиции {middle}")
            return
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    print("Элемент не найден")

def get_numbers_from_user():
    numbers = input("Введите числа, разделенные пробелами: ")
    return list(map(float, numbers.split()))

def get_search_element():
    return float(input("Введите элемент для поиска: "))

if __name__ == "__main__":
    unsorted_list = get_numbers_from_user()
    sorted_list = bubble_sort(unsorted_list)  # Используйте bubble_sort или selection_sort
    print(f"Отсортированный список: {sorted_list}")
    search_element = get_search_element()
    binary_search(sorted_list, search_element)
