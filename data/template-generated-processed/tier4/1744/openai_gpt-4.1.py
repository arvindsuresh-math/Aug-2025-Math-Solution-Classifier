def solve():
    """Index: 1744.
    Returns: the total amount the farmer got from selling all potatoes and carrots.
    """
    # L1
    potatoes_harvested = 250 # 250 potatoes
    potatoes_per_bundle = 25 # bundled in twenty-five's
    potato_bundles = potatoes_harvested / potatoes_per_bundle

    # L2
    potato_bundle_price = 1.90 # sold each bundle for $1.90
    potato_total = potato_bundle_price * potato_bundles

    # L3
    carrots_harvested = 320 # 320 carrots
    carrots_per_bundle = 20 # bundled in twenty's
    carrot_bundles = carrots_harvested / carrots_per_bundle

    # L4
    carrot_bundle_price = 2 # sold each bundle for $2
    carrot_total = carrot_bundle_price * carrot_bundles

    # L5
    answer = potato_total + carrot_total
    return answer