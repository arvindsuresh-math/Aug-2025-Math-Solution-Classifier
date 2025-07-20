def solve():
    """Index: 5395.
    Returns: the total pounds of pasta Dale needs to buy.
    """
    # L1
    reunion_people = 35 # Dale's family reunion will have 35 people
    serves_people = 7 # serves 7 people
    batch_multiplier = reunion_people / serves_people

    # L2
    original_pasta_pounds = 2 # calls for 2 pounds of pasta
    total_pasta_needed = original_pasta_pounds * batch_multiplier

    # FA
    answer = total_pasta_needed
    return answer