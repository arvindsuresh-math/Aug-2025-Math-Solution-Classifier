def solve():
    """Index: 1594.
    Returns: the number of oranges remaining after Michaela and Cassandra have eaten their fill.
    """
    # L1
    michaela_oranges = 20 # Michaela needs 20 oranges
    cassandra_multiplier = 2 # twice as many oranges
    cassandra_oranges = cassandra_multiplier * michaela_oranges

    # L2
    total_eaten = michaela_oranges + cassandra_oranges

    # L3
    oranges_picked = 90 # picked 90 oranges from the farm today
    oranges_remaining = oranges_picked - total_eaten

    # FA
    answer = oranges_remaining
    return answer