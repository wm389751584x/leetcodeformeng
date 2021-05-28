def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for num in lst:
        product.append(left)
        left *= num
    # get product startnig from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right *= lst[i]

    return product


if __name__ == "__main__":
    find_product([4,2,1,5,0])
