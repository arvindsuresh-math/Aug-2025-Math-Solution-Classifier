def solve():
    """Index: 3505.
    Returns: the total number of students who prefer dogs over cats.
    """
    # L1
    total_students = 30 # Of the 30 students in her class
    dogs_video_games_percent_decimal = 0.5 # 50% chose dogs and video games
    dogs_video_games_percent_num = 50 # 50% chose dogs and video games
    percent_factor = 0.01 # WK
    students_dogs_video_games = total_students * dogs_video_games_percent_decimal

    # L2
    dogs_movies_percent_num = 10 # 10% chose dogs and movies
    dogs_movies_percent_decimal = 0.1 # 10% chose dogs and movies
    students_dogs_movies = total_students * dogs_movies_percent_decimal

    # L3
    total_students_prefer_dogs = students_dogs_video_games + students_dogs_movies

    # FA
    answer = total_students_prefer_dogs
    return answer