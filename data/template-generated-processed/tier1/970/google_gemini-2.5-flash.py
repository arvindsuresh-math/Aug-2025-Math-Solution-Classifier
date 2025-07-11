def solve():
    """Index: 970.
    Returns: the number of pieces of mail Johann needs to deliver.
    """
    # L1
    friend_mail_per_person = 41 # each deliver 41 pieces of mail
    num_friends = 2 # two friends
    total_friend_mail = friend_mail_per_person * num_friends

    # L2
    total_mail_to_deliver = 180 # deliver 180 pieces of certified mail
    johann_mail = total_mail_to_deliver - total_friend_mail

    # FA
    answer = johann_mail
    return answer