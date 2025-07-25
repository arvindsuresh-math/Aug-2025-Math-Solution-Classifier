def solve():
    """Index: 2880.
    Returns: the number of people in the salon who are not clients.
    """
    # L1
    total_made = 200.00 # salon made $200.00
    cost_per_client = 20.00 # $20.00 per client
    num_clients = total_made / cost_per_client

    # L2
    total_fingers = 210 # 210 fingers in the salon
    fingers_per_person = 10 # everyone has 10 fingers
    total_people = total_fingers / fingers_per_person

    # L3
    non_clients = total_people - num_clients

    # FA
    answer = non_clients
    return answer