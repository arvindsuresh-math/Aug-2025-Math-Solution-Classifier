def solve():
    """Index: 1898.
    Returns: the total time it will take to cook all the hushpuppies in minutes.
    """
    # L1
    hushpuppies_per_guest = 5 # each guest will eat 5 hushpuppies
    num_guests = 20 # he is having 20 guests
    total_hushpuppies_needed = hushpuppies_per_guest * num_guests

    # L2
    hushpuppies_per_batch = 10 # He can cook 10 hushpuppies
    num_batches = total_hushpuppies_needed / hushpuppies_per_batch

    # L3
    minutes_per_batch = 8 # 8 minutes
    total_cooking_time_minutes = minutes_per_batch * num_batches

    # FA
    answer = total_cooking_time_minutes
    return answer