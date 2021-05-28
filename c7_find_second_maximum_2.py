def find_second_maximum(lst):
    first_max = float("-inf")
    second_max = float("-inf")

    for num in lst:
        if num > first_max:
            first_max = num

    for num in lst:
        if num != first_max and num > second_max:
            second_max = num

    return second_max


if __name__ == "__main__":
    print(find_second_maximum([9, 2, 3, 6]))
