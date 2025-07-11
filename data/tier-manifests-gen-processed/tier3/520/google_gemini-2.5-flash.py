def solve():
    """Index: 520.
    Returns: the number of kinds of rock that make up only one layer.
    """
    # L1
    total_layers = 25 # 25 different layers of rock
    limestone_layers = 5 # Five of the layers are limestone
    non_limestone_layers = total_layers - limestone_layers

    # L2
    half_divisor = 2 # Half of the rest are sandstone
    non_limestone_sandstone_layers = non_limestone_layers / half_divisor

    # L3
    quartz_layers = 4 # Four of the remaining are quartz
    non_limestone_sandstone_quartz_layers = non_limestone_sandstone_layers - quartz_layers

    # L4
    shale_half_divisor = 2 # Half of the rest are shale
    single_layer_rocks = non_limestone_sandstone_quartz_layers / shale_half_divisor

    # FA
    answer = single_layer_rocks
    return answer