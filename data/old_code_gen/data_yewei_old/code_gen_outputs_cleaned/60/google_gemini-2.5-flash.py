def solve_60():
    # Number of games per daughter
    games_per_daughter = 8
    # Duration of each game in hours
    game_duration_hours = 2
    # Practice hours for every game
    practice_hours_per_game = 4
    # Number of daughters
    num_daughters = 2

    # Calculate hours spent watching one daughter play games
    hours_playing_one_daughter = games_per_daughter * game_duration_hours

    # Calculate total hours spent watching both daughters play games
    total_hours_playing = hours_playing_one_daughter * num_daughters

    # Calculate hours spent watching one daughter practice
    hours_practicing_one_daughter = games_per_daughter * practice_hours_per_game

    # Calculate total hours spent watching both daughters practice
    total_hours_practicing = hours_practicing_one_daughter * num_daughters

    # Calculate the grand total hours Jerry will spend at the field
    total_hours_at_field = total_hours_playing + total_hours_practicing

    return total_hours_at_field

# Execute the function to get the answer
answer = solve_60()