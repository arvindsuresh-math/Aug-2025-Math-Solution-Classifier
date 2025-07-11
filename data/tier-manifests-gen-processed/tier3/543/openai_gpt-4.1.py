def solve():
    """Index: 543.
    Returns: the total amount of money the class was able to gather together.
    """
    # L1
    full_amount = 50 # $50 each to finance a big science project
    half_divisor = 2 # paid half
    half_amount = full_amount / half_divisor

    # L2
    num_half_payers = 4 # 4 students, who paid half
    total_half_payers = num_half_payers * half_amount

    # L3
    total_students = 25 # 25 students
    num_full_payers = total_students - num_half_payers

    # L4
    total_full_payers = num_full_payers * full_amount

    # L5
    total_gathered = total_half_payers + total_full_payers

    # FA
    answer = total_gathered
    return answer