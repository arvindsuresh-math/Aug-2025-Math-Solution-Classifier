def solve():
    """Index: 2880.
    Returns: the number of people in the salon who are not clients.
    """
    # L1
    total_revenue = 200 # The salon made $200.00
    price_per_client = 20 # They charge $20.00 per client
    num_clients = total_revenue / price_per_client

    # L2
    total_fingers = 210 # There are 210 fingers in the salon
    fingers_per_person = 10 # Everyone has 10 fingers
    total_people = total_fingers / fingers_per_person

    # L3
    num_non_clients = total_people - num_clients

    # FA
    answer = num_non_clients
    return answer