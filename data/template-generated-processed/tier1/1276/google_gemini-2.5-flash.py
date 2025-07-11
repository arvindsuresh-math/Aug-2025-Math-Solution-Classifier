def solve():
    """Index: 1276.
    Returns: Kaylin's age.
    """
    # L1
    freyja_age = 10 # Freyja is ten years old
    eli_older_than_freyja = 9 # nine years older than Freyja
    eli_age = freyja_age + eli_older_than_freyja

    # L2
    multiplier_for_sarah = 2 # twice as old as Eli
    sarah_age = multiplier_for_sarah * eli_age

    # L3
    kaylin_younger_than_sarah = 5 # five years younger than Sarah
    kaylin_age = sarah_age - kaylin_younger_than_sarah

    # FA
    answer = kaylin_age
    return answer