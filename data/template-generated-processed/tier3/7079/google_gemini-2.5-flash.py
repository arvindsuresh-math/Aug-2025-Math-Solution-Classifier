def solve():
    """Index: 7079.
    Returns: the number of colored pencils each container can hold after redistribution.
    """
    # L1
    initial_pencils = 150 # 150 colored pencils
    num_containers = 5 # 5 containers
    pencils_per_container_initial = initial_pencils / num_containers

    # L2
    added_pencils = 30 # 30 more pencils
    total_pencils = initial_pencils + added_pencils

    # L3
    pencils_per_container_final = total_pencils / num_containers

    # FA
    answer = pencils_per_container_final
    return answer