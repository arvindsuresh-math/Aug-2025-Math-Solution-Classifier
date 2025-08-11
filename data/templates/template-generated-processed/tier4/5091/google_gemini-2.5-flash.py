def solve():
    """Index: 5091.
    Returns: the total number of cans of frosting Paul will need.
    """
    # L1
    cans_per_layer_cake = 1 # 1 can of frosting to frost a layer cake
    num_layer_cakes = 3 # 3 layer cakes
    frosting_for_layer_cakes = cans_per_layer_cake * num_layer_cakes

    # L2
    num_cupcake_dozens = 6 # 6 dozen cupcakes
    num_single_cakes = 12 # 12 single cakes
    num_brownie_pans = 18 # 18 pans of brownies
    total_other_orders = num_cupcake_dozens + num_single_cakes + num_brownie_pans

    # L3
    frosting_per_other_order = 0.5 # a half can of frosting for a single cake, or a single pan of brownies, or a dozen cupcakes
    frosting_for_other_items = total_other_orders * frosting_per_other_order

    # L4
    total_frosting_cans = frosting_for_layer_cakes + frosting_for_other_items

    # FA
    answer = total_frosting_cans
    return answer