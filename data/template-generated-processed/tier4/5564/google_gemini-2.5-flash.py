def solve():
    """Index: 5564.
    Returns: the amount of money the school raised for the playground after administration fees.
    """
    # L1
    mrs_johnson_raised = 2300 # Mrs. Johnson’s class raised $2300
    sutton_johnson_divisor = 2 # twice the amount that Mrs. Sutton’s class raised
    mrs_sutton_raised = mrs_johnson_raised / sutton_johnson_divisor

    # L2
    rollin_sutton_multiplier = 8 # Mrs. Sutton’s class raised 8 times less than Miss Rollin’s class
    miss_rollin_raised = mrs_sutton_raised * rollin_sutton_multiplier

    # L3
    rollin_total_multiplier = 3 # Miss Rollin’s class raised a third of the total amount raised by the school
    total_raised_before_fees = miss_rollin_raised * rollin_total_multiplier

    # L4
    admin_fee_percent_num = 2 # 2% will be deducted for administration fees
    percent_divisor = 100 # WK
    admin_fee_decimal = admin_fee_percent_num / percent_divisor

    # L5
    administration_fees = total_raised_before_fees * admin_fee_decimal

    # L6
    final_amount_raised = total_raised_before_fees - administration_fees

    # FA
    answer = final_amount_raised
    return answer