```python
def solve(
    total_milk_gallons: int = 16, # Bill milked his cow and got 16 gallons of milk
    fraction_for_sour_cream: float = 1/4, # He turned 1/4 into sour cream
    fraction_for_butter: float = 1/4, # 1/4 into butter
    milk_per_gallon_butter: int = 4, # It takes 4 gallons of milk to make one gallon of butter
    milk_per_gallon_sour_cream: int = 2, # and 2 gallons of milk to make 1 gallon of sour cream
    price_butter_per_gallon: int = 5, # If Bill sells butter for $5/gallon
    price_sour_cream_per_gallon: int = 6, # sour cream for $6/gallon
    price_whole_milk_per_gallon: int = 3 # and whole milk for $3/gallon
):
    """Index: 5464.
    Returns: the total amount of money Bill makes.
    """
    #: L1
    milk_used_for_sour_cream = total_