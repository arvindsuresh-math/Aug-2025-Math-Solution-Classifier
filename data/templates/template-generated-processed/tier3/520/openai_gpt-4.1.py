def solve():
    """Index: 520.
    Returns: the number of kinds of rock that make up only one layer in the canyon's strata.
    """
    # L1
    total_layers = 25 # 25 different layers of rock
    limestone_layers = 5 # Five of the layers are limestone
    not_limestone = total_layers - limestone_layers

    # L2
    sandstone_divisor = 2 # Half of the rest are sandstone
    not_limestone_or_sandstone = not_limestone / sandstone_divisor

    # L3
    quartz_layers = 4 # Four of the remaining are quartz
    not_limestone_sandstone_quartz = not_limestone_or_sandstone - quartz_layers

    # L4
    shale_divisor = 2 # Half of the rest are shale
    kinds_one_layer = not_limestone_sandstone_quartz / shale_divisor

    # FA
    answer = kinds_one_layer
    return answer