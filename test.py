nums = [1,0,1,2]

def merge(arr, L, M, R):
    left = arr[L:M+1]
    right = arr[M+1:R+1]
    i, j, k = L, 0, 0

    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            arr[i] = left[j]
            j += 1
        if right[k] < left[j]:
            arr[i] = right[k]
            k += 1
        i += 1
    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1
    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1
    
    return arr


def merge_sort(arr, l, r):
    if l == r:
        return arr

    m = (l + r) // 2
    print(m)
    merge_sort(arr, l, m)
    merge_sort(arr, m+1, r)
    # print(merge(arr, l, m, r))


merge_sort(nums, 0, len(nums))