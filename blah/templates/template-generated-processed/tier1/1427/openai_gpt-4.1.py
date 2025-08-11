def solve():
    """Index: 1427.
    Returns: the total number of remaining animals in the adoption center after the last adoptions.
    """
    # L1
    initial_dogs = 200 # The total number of dogs at an animal rescue center is 200
    incoming_dogs = 100 # 100 dogs at another rescue center are to be moved
    after_incoming = initial_dogs + incoming_dogs

    # L2
    adopted_first = 40 # gives out 40 animals for adoption
    after_first_adoption = after_incoming - adopted_first

    # L3
    adopted_second = 60 # 60 more dogs were adopted
    remaining_dogs = after_first_adoption - adopted_second

    # FA
    answer = remaining_dogs
    return answer