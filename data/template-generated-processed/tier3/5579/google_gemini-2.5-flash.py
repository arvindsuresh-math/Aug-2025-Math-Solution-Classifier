from fractions import Fraction

def solve():
    """Index: 5579.
    Returns: the total number of marks Amaya scored in all subjects.
    """
    # L1
    maths_less_fraction = Fraction(1, 10) # scored 1/10 less in Maths
    music_score = 70 # scored 70 in Music
    marks_less_in_maths = maths_less_fraction * music_score

    # L2
    maths_score = music_score - marks_less_in_maths

    # L3
    maths_fewer_than_arts = 20 # scored 20 marks fewer in Maths than she scored in Arts
    arts_score = maths_score + maths_fewer_than_arts

    # L4
    social_studies_more_than_music = 10 # got 10 marks more in Social Studies than she got in Music
    social_studies_score = music_score + social_studies_more_than_music

    # L5
    total_marks = music_score + maths_score + arts_score + social_studies_score

    # FA
    answer = total_marks
    return answer