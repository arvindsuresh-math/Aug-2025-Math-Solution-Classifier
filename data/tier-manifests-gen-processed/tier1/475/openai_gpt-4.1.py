def solve():
    """Index: 475.
    Returns: the number of apples Layla picked.
    """
    # L1
    average_apples = 30 # averaged 30 apples picked
    num_people = 3 # the three
    total_apples = average_apples * num_people

    # L2
    maggie_apples = 40 # Maggie picked 40 apples
    kelsey_apples = 28 # Kelsey picked 28 apples
    accounted_apples = maggie_apples + kelsey_apples

    # L3
    layla_apples = total_apples - accounted_apples

    # FA
    answer = layla_apples
    return answer