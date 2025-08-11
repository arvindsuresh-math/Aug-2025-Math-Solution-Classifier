def solve():
    """Index: 5887.
    Returns: the total amount of homework Nina is having.
    """
    # L1
    ruby_math_homework = 6 # six math homework
    math_multiplier = 4 # four times more math homework
    nina_more_math_homework = ruby_math_homework * math_multiplier

    # L2
    nina_total_math_homework = nina_more_math_homework + ruby_math_homework

    # L3
    ruby_reading_homework = 2 # two reading homework
    reading_multiplier = 8 # eight times more reading homework
    nina_more_reading_homework = reading_multiplier * ruby_reading_homework

    # L4
    nina_total_reading_homework = nina_more_reading_homework + ruby_reading_homework

    # L5
    nina_total_homework_altogether = nina_total_reading_homework + nina_total_math_homework

    # FA
    answer = nina_total_homework_altogether
    return answer