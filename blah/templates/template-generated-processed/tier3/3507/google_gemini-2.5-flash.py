from fractions import Fraction

def solve():
    """Index: 3507.
    Returns: Ella's new salary.
    """
    # L1
    spent_on_games = 100 # spent $100
    percentage_on_games = Fraction(40, 100) # 40% of the money
    last_year_salary = spent_on_games / percentage_on_games

    # L2
    raise_percentage = Fraction(110, 100) # 10% raise (100% + 10% = 110%)
    new_salary = last_year_salary * raise_percentage

    # FA
    answer = new_salary
    return answer