# 버블정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 예시 사용
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("정렬된 배열:", numbers)


# 삽입정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 예시 사용
numbers = [64, 25, 12, 22, 11]
insertion_sort(numbers)
print("정렬된 배열:", numbers)


#선택정렬
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 예시 사용
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("정렬된 배열:", numbers)

#퀵정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 예시 사용
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("정렬된 배열:", sorted_numbers)

#병합정렬
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 분할 단계
        merge_sort(left_half)
        merge_sort(right_half)

        # 합병 단계
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 예시 사용
numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numbers)
print("정렬된 배열:", numbers)