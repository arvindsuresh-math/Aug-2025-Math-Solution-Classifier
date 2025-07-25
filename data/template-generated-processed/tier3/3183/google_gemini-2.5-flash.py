def solve():
    """Index: 3183.
    Returns: the percentage of students who take music.
    """
    # L1
    total_students = 400 # There are 400 students
    dance_students = 120 # 120 students take dance as their elective
    art_students = 200 # 200 students take art as their elective
    music_students = total_students - dance_students - art_students

    # L2
    percentage_multiplier = 100 # WK
    percentage_music_students = (music_students / total_students) * percentage_multiplier

    # FA
    answer = percentage_music_students
    return answer