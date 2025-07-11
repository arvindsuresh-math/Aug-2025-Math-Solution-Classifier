def solve():
    """Index: 353.
    Returns: the amount of money Sally’s Woodworking LLC will reimburse Remy.
    """
    # L1
    cost_per_piece = 134 # the cost of a piece of furniture is $134
    num_pieces = 150 # 150 pieces of furniture
    correct_total_cost = cost_per_piece * num_pieces

    # L2
    amount_paid = 20700 # Remy paid $20,700
    reimbursement = amount_paid - correct_total_cost

    # FA
    answer = reimbursement
    return answer