#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    route = []

    for t in tickets:
        if t.source not in dict:
            dict[t.source] = t.destination
            # find the first destination, add it to route
            if t.source == "NONE":
                route.append(t.destination)

    cur = route[0]
    while cur is not "NONE":
        route.append(dict[cur])
        cur = dict[cur]
    return route
