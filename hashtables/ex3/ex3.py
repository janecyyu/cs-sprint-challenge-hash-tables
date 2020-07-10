def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    length = len(arrays)
    print(length)
    result = []
    # loop every array
    for arr in arrays:
        # loop each element in arr, add to dict if not exists
        for e in arr:
            if e not in dict:
                dict[e] = 0
            else:
                dict[e] += 1
    # check our dict and see if any value equals length
    for k, v in dict.items():
        if v == length-1:
            result.append(k)
    return result


if __name__ == "__main__":
    # arrays = []

    # arrays.append([1, 2, 3])
    # arrays.append([3, 4, 5, 2])
    # arrays.append([1, 2, 3])

    # print(intersection(arrays))
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
