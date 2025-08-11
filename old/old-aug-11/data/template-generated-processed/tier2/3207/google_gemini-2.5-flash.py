def solve():
    """Index: 3207.
    Returns: the total liters of milk Josephine sold.
    """
    # L1
    liters_per_container_1 = 2 # two liters each
    num_containers_1 = 3 # three containers
    total_liters_container_1 = liters_per_container_1 * num_containers_1

    # L2
    liters_per_container_2 = 0.75 # 0.75 liters each
    num_containers_2 = 2 # two containers
    total_liters_container_2 = liters_per_container_2 * num_containers_2

    # L3
    liters_per_container_3 = 0.5 # 0.5 liters each
    num_containers_3 = 5 # five containers
    total_liters_container_3 = liters_per_container_3 * num_containers_3

    # L4
    total_milk_sold = total_liters_container_1 + total_liters_container_2 + total_liters_container_3

    # FA
    answer = total_milk_sold
    return answer