def solve():
    """Index: 4517.
    Returns: the total cost of the fruit basket.
    """
    # L1
    num_bananas = 4 # 4 bananas
    cost_per_banana = 1 # One banana costs $1
    cost_bananas = num_bananas * cost_per_banana

    # L2
    num_apples = 3 # 3 apples
    cost_per_apple = 2 # An apple costs $2
    cost_apples = num_apples * cost_per_apple

    # L3
    num_strawberries = 24 # 24 strawberries
    strawberries_per_unit = 12 # 12 strawberries cost $4
    cost_per_unit_strawberries = 4 # 12 strawberries cost $4
    cost_strawberries = (num_strawberries / strawberries_per_unit) * cost_per_unit_strawberries

    # L4
    num_avocados = 2 # 2 avocados
    cost_per_avocado = 3 # An avocado costs $3
    cost_avocados = num_avocados * cost_per_avocado

    # L5
    half_bunch_grapes_cost = 2 # half a bunch of grapes costs $2
    multiplier_for_full_bunch = 2 # WK
    cost_grapes = multiplier_for_full_bunch * half_bunch_grapes_cost

    # L6
    total_cost = cost_bananas + cost_apples + cost_strawberries + cost_avocados + cost_grapes

    # FA
    answer = total_cost
    return answer