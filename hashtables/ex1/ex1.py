def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = ()
    # loop each weight
    for w in sorted(weights):
        # add to dict
        if w not in dict:
            dict[w] = limit - w
        # check the value if exists in dict
        if dict[w] in dict:
            # check if the two elements are the same
            if (dict[w] == limit-dict[w]):
                idx_l = weights.index(dict[w])
                idx_h = weights.index(dict[w], idx_l+1)
                result = (idx_h, idx_l)
                return result
            # find their index in weights
            else:
                result = (weights.index(limit-dict[w]), weights.index(dict[w]))
                return result
    # if no match
    return None


t = get_indices_of_item_weights([4, 4], 2, 8)
print(t)
