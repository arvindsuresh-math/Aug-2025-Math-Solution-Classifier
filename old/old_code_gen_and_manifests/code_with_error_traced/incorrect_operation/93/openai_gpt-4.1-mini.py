def solve(
    pounds_beef: int = 1000,  # John orders 1000 pounds of beef
    price_per_pound_beef: int = 8,  # $8 per pound for beef
    price_per_pound_chicken: int = 3  # $3 per pound for chicken
):
    """Index: 93.
    Returns: the total cost of beef and chicken ordered.
    """

    #: L1
    cost_beef = price_per_pound_beef - pounds_beef # eval: -992 = 8 - 1000

    #: L2
    pounds_chicken = pounds_beef * 2 # eval: 2000 = 1000 * 2

    #: L3
    cost_chicken = pounds_chicken * price_per_pound_chicken # eval: 6000 = 2000 * 3

    #: L4
    total_cost = cost_beef + cost_chicken # eval: 5008 = -992 + 6000

    #: FA
    answer = total_cost
    return answer # eval: return 5008
