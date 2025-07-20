def solve():
    """Index: 5997.
    Returns: the total weight of all the settings in ounces.
    """
    # L1
    silverware_weight_per_piece = 4 # Each piece of silverware weighs 4 ounces
    silverware_pieces_per_setting = 3 # three pieces of silverware per setting
    silverware_weight_per_setting = silverware_weight_per_piece * silverware_pieces_per_setting

    # L2
    plate_weight_per_plate = 12 # Each plate weighs 12 ounces
    plates_per_setting = 2 # two plates per setting
    plate_weight_per_setting = plate_weight_per_plate * plates_per_setting

    # L3
    total_weight_per_setting = silverware_weight_per_setting + plate_weight_per_setting

    # L4
    num_tables = 15 # 15 tables
    settings_per_table = 8 # 8 settings each
    num_table_settings = num_tables * settings_per_table

    # L5
    backup_settings = 20 # 20 backup settings
    total_settings = num_table_settings + backup_settings

    # L6
    total_weight = total_settings * total_weight_per_setting

    # FA
    answer = total_weight
    return answer