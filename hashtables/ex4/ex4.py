def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = []

    for e in a:
        # absolute value e
        if abs(e) not in dict:
            dict[abs(e)] = 0
        else:
            result.append(abs(e))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
