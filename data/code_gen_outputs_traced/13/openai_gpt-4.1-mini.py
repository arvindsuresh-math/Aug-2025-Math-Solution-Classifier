def solve(
    cheddar_cost: int = 10,  # 2 pounds of cheddar cheese for $10
    cheddar_pounds: int = 2,  # 2 pounds of cheddar cheese
    cream_cheese_pound: int = 1,  # a pound of cream cheese
    cold_cuts_pack: int = 1  # a pack of cold cuts
):
    """Index: 13.
    Returns: the total amount Jasper spends on the ingredients.
    """
    #: L1
    cream_cheese_cost = cheddar_cost / 2 # eval: 5.0 = 10 / 2
    #: L2
    cold_cuts_cost = cheddar_cost * 2 # eval: 20 = 10 * 2
    #: L3
    total_spent = cheddar_cost + cream_cheese_cost + cold_cuts_cost # eval: 35.0 = 10 + 5.0 + 20
    answer = total_spent  # FINAL ANSWER # eval: 35.0 = 35.0  # FINAL ANSWER
    return answer # eval: return 35.0