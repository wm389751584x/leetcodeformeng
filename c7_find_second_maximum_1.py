def find_second_maximum(lst):
    # Write your code here
    def merge_sort(lst):
        
        if len(lst) <= 1:
            return lst
        
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                left.insert(i, right[j])
                i += 1
                j += 1
            else:
                i += 1
        
        if j < len(right):
            left.extend(right[j:])
        
        return left

    sorted_list = merge_sort(lst)
    print(sorted_list)
    return sorted_list[-2]

if __name__ == "__main__":
    find_second_maximum([9, 2, 3, 6])