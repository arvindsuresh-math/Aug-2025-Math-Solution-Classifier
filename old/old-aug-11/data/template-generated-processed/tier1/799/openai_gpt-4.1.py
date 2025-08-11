def solve():
    """Index: 799.
    Returns: the total number of legs in the room.
    """
    # L1
    num_tables_4legs = 4 # 4 tables
    num_sofa_4legs = 1 # 1 sofa
    num_chairs_4legs = 2 # 2 chairs
    total_4leg_furniture = num_tables_4legs + num_sofa_4legs + num_chairs_4legs

    # L2
    legs_per_4leg_furniture = 4 # have 4 legs each
    legs_4leg_furniture = total_4leg_furniture * legs_per_4leg_furniture

    # L3
    num_tables_3legs = 3 # 3 tables with 3 legs each
    legs_per_3leg_table = 3 # 3 legs each
    legs_3leg_tables = num_tables_3legs * legs_per_3leg_table

    # L4
    legs_1leg_table = 1 # 1 table with 1 leg
    legs_rocking_chair = 2 # 1 rocking chair with 2 legs
    total_legs = legs_4leg_furniture + legs_3leg_tables + legs_1leg_table + legs_rocking_chair

    # FA
    answer = total_legs
    return answer