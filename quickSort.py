""" Implement quick sort in Python
    Input: a list
    Output: a sorted list"""


def quickSort(array):
    less = []
    equal = []
    great = []

    if len(array) > 1:
        pivit = array[0]
        for x in array:
            if x < pivit:
                less.append(x)
            elif x == pivit:
                equal.append(x)
            else:
                great.append(x)

        return quickSort(less) + equal + quickSort(great)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quickSort(test))
