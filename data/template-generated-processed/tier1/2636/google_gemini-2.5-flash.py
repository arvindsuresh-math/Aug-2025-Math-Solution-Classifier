def solve():
    """Index: 2636.
    Returns: the total time for which the five students were late.
    """
    # L1
    charlize_late_minutes = 20 # Charlize was 20 minutes late
    friends_later_than_charlize = 10 # each ten minutes late than she was
    friends_late_minutes = charlize_late_minutes + friends_later_than_charlize

    # L2
    num_classmates = 4 # Four of her classmates
    total_friends_late_minutes = num_classmates * friends_late_minutes

    # L3
    total_all_students_late_minutes = total_friends_late_minutes + charlize_late_minutes

    # FA
    answer = total_all_students_late_minutes
    return answer