def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    # loop each weight
    print(sorted(weights))
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
                idx_l = min(weights.index(
                    limit-dict[w]), weights.index(dict[w]))
                idx_h = max(weights.index(
                    limit-dict[w]), weights.index(dict[w]))
                result = (idx_h, idx_l)
                return result
    # if no match
    return None
