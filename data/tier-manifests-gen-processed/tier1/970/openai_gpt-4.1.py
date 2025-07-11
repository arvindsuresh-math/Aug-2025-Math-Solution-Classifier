def solve():
    """Index: 970.
    Returns: the number of pieces of mail Johann needs to deliver.
    """
    # L1
    friends_each_deliver = 41 # friends each deliver 41 pieces of mail
    num_friends = 2 # Johann and two friends
    friends_total = friends_each_deliver * num_friends

    # L2
    total_mail = 180 # deliver 180 pieces of certified mail
    johann_mail = total_mail - friends_total

    # FA
    answer = johann_mail
    return answer