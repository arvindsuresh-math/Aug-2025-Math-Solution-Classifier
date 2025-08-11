from fractions import Fraction

def solve():
    """Index: 549.
    Returns: the total number of legs of furniture Kenzo has remaining in his company.
    """
    # L1
    damaged_chair_percentage = Fraction(40, 100) # 40% of the chairs are damaged
    total_chairs = 80 # Kenzo has 80 office chairs
    disposed_chairs = damaged_chair_percentage * total_chairs

    # L2
    remaining_chairs = total_chairs - disposed_chairs

    # L3
    legs_per_chair = 5 # five legs each
    remaining_chair_legs = remaining_chairs * legs_per_chair

    # L4
    total_tables = 20 # 20 round tables
    legs_per_table = 3 # three legs each
    table_legs = total_tables * legs_per_table

    # L5
    total_legs = table_legs + remaining_chair_legs

    # FA
    answer = total_legs
    return answer