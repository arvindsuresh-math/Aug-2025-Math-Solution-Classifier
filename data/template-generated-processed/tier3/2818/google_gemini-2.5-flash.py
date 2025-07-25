def solve():
    """Index: 2818.
    Returns: the total marks Teresa scored in all subjects.
    """
    # L1
    science_marks = 70 # 70 marks in science
    music_marks = 80 # 80 in music
    science_and_music_total = science_marks + music_marks

    # L2
    social_studies_marks = 85 # 85 in social studies
    total_after_social_studies = science_and_music_total + social_studies_marks

    # L3
    physics_fraction_numerator = 1 # half as many marks
    physics_fraction_denominator = 2 # half as many marks
    physics_marks = (physics_fraction_numerator / physics_fraction_denominator) * music_marks

    # L4
    final_total_marks = total_after_social_studies + physics_marks

    # FA
    answer = final_total_marks
    return answer