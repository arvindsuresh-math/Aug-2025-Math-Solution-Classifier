from fractions import Fraction

def solve():
    """Index: 939.
    Returns: the number of students who do not play either game.
    """
    # L1
    total_students = 20 # 20 students in the class
    basketball_denominator = 2 # Half of them play basketball
    basketball_players = total_students / basketball_denominator

    # L2
    volleyball_fraction = Fraction(2, 5) # Two-fifths play volleyball
    volleyball_players = total_students * volleyball_fraction

    # L3
    both_games_fraction = Fraction(1, 10) # one-tenth play both basketball and volleyball
    both_players = total_students * both_games_fraction

    # L4
    sum_of_individual_sport_counts = basketball_players + volleyball_players

    # L5
    students_playing_at_least_one_game = sum_of_individual_sport_counts - both_players

    # L6
    students_not_playing_either_game = total_students - students_playing_at_least_one_game

    # FA
    answer = students_not_playing_either_game
    return answer