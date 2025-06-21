def solve(
        keys_sticky: int = 15,  # Tina counts 15 keys that are sticky
        time_per_key: int = 3,  # it takes 3 minutes to clean one key
        keys_cleaned: int = 1,  # Tina has already cleaned one key
        homework_time: int = 10  # her assignment will take 10 minutes to complete
):
    """Index: 636.
    Returns: the total minutes needed to clean remaining keys and finish homework.
    """
    #: L1
    remaining_keys = keys_sticky - keys_cleaned
    time_to_clean_keys = remaining_keys * time_per_key

    #: L2
    total_time = time_to_clean_keys + homework_time

    answer = total_time  # FINAL ANSWER
    return answer