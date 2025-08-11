def solve():
    """Index: 6323.
    Returns: the total number of jellybeans in the jar.
    """
    # L1
    initial_jellybeans = 90 # 90 jellybeans in a jar
    samantha_took = 24 # Samantha snuck 24 jellybeans
    jellybeans_after_samantha = initial_jellybeans - samantha_took

    # L2
    shelby_ate = 12 # Shelby ate 12 jellybeans
    jellybeans_after_shelby = jellybeans_after_samantha - shelby_ate

    # L3
    total_taken_out = samantha_took + shelby_ate

    # L4
    refill_divisor = 2 # half as much as Samantha and Shelby took out
    refilled_amount = total_taken_out / refill_divisor

    # L5
    final_jellybeans = jellybeans_after_shelby + refilled_amount

    # FA
    answer = final_jellybeans
    return answer