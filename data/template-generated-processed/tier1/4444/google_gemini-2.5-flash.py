def solve():
    """Index: 4444.
    Returns: the combined population of Port Perry and Lazy Harbor.
    """
    # L1
    wellington_population = 900 # Wellington has a population of 900
    port_perry_multiplier = 7 # seven times as many as the population of Wellington
    port_perry_population = wellington_population * port_perry_multiplier

    # L2
    port_perry_more_than_lazy_harbor = 800 # Port Perry is 800 more than the population of Lazy Harbor
    lazy_harbor_population = port_perry_population - port_perry_more_than_lazy_harbor

    # L3
    combined_population = port_perry_population + lazy_harbor_population

    # FA
    answer = combined_population
    return answer