def solve():
    """Index: 912.
    Returns: the total money made from the strawberries.
    """
    # L1
    betty_strawberries = 16 # Betty picked 16 strawberries
    more_than_betty = 20 # Matthew picked 20 more strawberries than Betty
    matthew_strawberries = betty_strawberries + more_than_betty

    # L2
    natalie_divisor = 2 # twice as many as Natalie
    natalie_strawberries = matthew_strawberries / natalie_divisor

    # L3
    total_strawberries = betty_strawberries + matthew_strawberries + natalie_strawberries

    # L4
    strawberries_per_jar = 7 # One jar of jam used 7 strawberries
    num_jars = total_strawberries / strawberries_per_jar

    # L5
    price_per_jar = 4 # they sold each jar at $4
    total_money_made = num_jars * price_per_jar

    # FA
    answer = total_money_made
    return answer