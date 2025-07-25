def solve():
    """Index: 4634.
    Returns: the total number of pennies donated to charity.
    """
    # L1
    cassandra_pennies = 5000 # Cassandra collected 5000 pennies
    james_fewer_pennies = 276 # James collected 276 fewer pennies
    james_pennies = cassandra_pennies - james_fewer_pennies

    # L2
    total_pennies = cassandra_pennies + james_pennies

    # FA
    answer = total_pennies
    return answer