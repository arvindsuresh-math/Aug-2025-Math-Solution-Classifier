def solve():
    """Index: 1518.
    Returns: the number of non-vegan cupcakes that also contain gluten.
    """
    # L1
    total_cupcakes = 80 # A mum ordered 80 cupcakes
    gluten_free_divisor = 2 # Half of them are gluten-free
    gluten_free_cupcakes = total_cupcakes / gluten_free_divisor

    # L2
    total_vegan_cupcakes = 24 # 24 vegan cupcakes
    vegan_gluten_free_divisor = 2 # half of them are also gluten-free
    vegan_gluten_free_cupcakes = total_vegan_cupcakes / vegan_gluten_free_divisor

    # L3
    non_vegan_cupcakes_with_gluten = gluten_free_cupcakes - vegan_gluten_free_cupcakes

    # FA
    answer = non_vegan_cupcakes_with_gluten
    return answer