def solve():
    """Index: 415.
    Returns: the dog's full adult weight in pounds.
    """
    # L1
    weight_7wks = 6 # At 7 weeks old, the puppy weighed 6 pounds
    double = 2 # doubled in weight
    weight_9wks = weight_7wks * double

    # L2
    weight_3mo = weight_9wks * double

    # L3
    weight_5mo = weight_3mo * double

    # L4
    added_final = 30 # adding another 30 pounds
    final_weight = weight_5mo + added_final

    # FA
    answer = final_weight
    return answer