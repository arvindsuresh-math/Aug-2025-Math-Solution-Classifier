def solve():
    """Index: 5568.
    Returns: the number of chocolate and vanilla cupcakes Mary should make.
    """
    # L1
    cherry_cupcakes = 36 # 36 cherry cupcakes
    berry_cupcakes = 48 # 48 berry cupcakes
    current_cupcakes = cherry_cupcakes + berry_cupcakes

    # L2
    total_needed_cupcakes = 144 # 144 cupcakes for her party
    additional_cupcakes_needed = total_needed_cupcakes - current_cupcakes

    # L3
    number_of_flavors_to_split = 2 # chocolate and vanilla cupcakes
    cupcakes_per_flavor = additional_cupcakes_needed / number_of_flavors_to_split

    # FA
    answer = cupcakes_per_flavor
    return answer