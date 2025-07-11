def solve():
    """Index: 799.
    Returns: the total number of legs in the room.
    """
    # L1
    num_tables_4_legs = 4 # 4 tables
    num_sofas_4_legs = 1 # 1 sofa
    num_chairs_4_legs = 2 # 2 chairs
    pieces_4_legs = num_tables_4_legs + num_sofas_4_legs + num_chairs_4_legs

    # L2
    legs_per_piece_4_legs = 4 # 4 legs each
    total_legs_4_legs_furniture = pieces_4_legs * legs_per_piece_4_legs

    # L3
    num_tables_3_legs = 3 # 3 tables
    legs_per_table_3_legs = 3 # 3 legs each
    total_legs_3_legs_tables = num_tables_3_legs * legs_per_table_3_legs

    # L4
    legs_table_1_leg = 1 # 1 table with 1 leg
    legs_rocking_chair = 2 # 1 rocking chair with 2 legs
    total_legs_in_room = total_legs_4_legs_furniture + total_legs_3_legs_tables + legs_table_1_leg + legs_rocking_chair

    # FA
    answer = total_legs_in_room
    return answer