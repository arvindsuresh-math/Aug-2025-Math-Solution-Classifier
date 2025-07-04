# -------------------------------------------- #
# Correct examples of code with eval trace
# -------------------------------------------- #

def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""

    #: L1
    clips_sold_in_may = clips_sold_in_april * fraction_of_april_sales # eval: 24.0 = 48 * 0.5

    #: L2
    total_clips_sold = clips_sold_in_april + clips_sold_in_may # eval: 72.0 = 48 + 24.0

    #: FA
    answer = total_clips_sold
    return answer # eval: return 72.0

def solve(
    hourly_wage: int = 12, # Weng earns $12 an hour
    minutes_worked: int = 50 # she just did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned.
    """

    #: L1
    wage_per_minute = hourly_wage / 60 # eval: 0.2 = 12 / 60

    #: L2
    total_earned = wage_per_minute * minutes_worked # eval: 10.0 = 0.2 * 50

    #: FA
    answer = total_earned
    return answer # eval: return 10.0

def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = wallet_cost * betty_savings_fraction # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3
    money_still_needed = wallet_cost - betty_savings - grandparents_contribution - parents_contribution # eval: 5.0 = 100 - 50.0 - 30 - 15

    #: FA
    answer = money_still_needed
    return answer # eval: return 5.0

def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = pages_read_yesterday + pages_read_today # eval: 36 = 12 + 24

    #: L3
    remaining_pages = total_pages - total_pages_read # eval: 84 = 120 - 36

    #: L4
    pages_to_read_tomorrow = remaining_pages / 2 # eval: 42.0 = 84 / 2

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 42.0

def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,  # to 2 different friends
    times_per_week: int = 2,  # twice a week
    weeks_per_year: int = 52  # in a year
):
    """Index: 4.
    Returns: the total number of pages James writes in a year."""

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week # eval: 6 = 3 * 2

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends # eval: 12 = 6 * 2

    #: L3
    total_pages_per_year = total_pages_per_week * weeks_per_year # eval: 624 = 12 * 52

    #: FA
    answer = total_pages_per_year
    return answer # eval: return 624

# -------------------------------------------- #
# Incorrect-operation code with eval trace
# -------------------------------------------- #

def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""

    #: L1
    clips_sold_in_may = clips_sold_in_april + fraction_of_april_sales # eval: 48.5 = 48 + 0.5

    #: L2
    total_clips_sold = clips_sold_in_april + clips_sold_in_may # eval: 96.5 = 48 + 48.5

    #: FA
    answer = total_clips_sold
    return answer # eval: return 96.5

def solve(
    hourly_rate: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # She did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for her babysitting work.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2
    earnings = rate_per_minute + minutes_worked # eval: 50.2 = 0.2 + 50

    #: FA
    answer = earnings
    return answer # eval: return 50.2

def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = wallet_cost * betty_savings_fraction # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3
    money_still_needed = wallet_cost + betty_savings - grandparents_contribution - parents_contribution # eval: 105.0 = 100 + 50.0 - 30 - 15

    #: FA
    answer = money_still_needed
    return answer # eval: return 105.0

def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = pages_read_yesterday - pages_read_today # eval: -12 = 12 - 24

    #: L3
    remaining_pages = total_pages - total_pages_read # eval: 132 = 120 - -12

    #: L4
    pages_to_read_tomorrow = remaining_pages / 2 # eval: 66.0 = 132 / 2

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 66.0

def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,  # to 2 different friends
    times_per_week: int = 2,  # twice a week
    weeks_per_year: int = 52  # in a year
):
    """Index: 4.
    Returns: the total number of pages James writes in a year."""

    #: L1
    pages_per_friend_per_week = pages_per_letter - times_per_week # eval: 1 = 3 - 2

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends # eval: 2 = 1 * 2

    #: L3
    total_pages_per_year = total_pages_per_week * weeks_per_year # eval: 104 = 2 * 52

    #: FA
    answer = total_pages_per_year
    return answer # eval: return 104

# -------------------------------------------- #
# Skipped-step code with eval trace
# -------------------------------------------- #

def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""

    #: L1
    clips_sold_in_may = clips_sold_in_april * fraction_of_april_sales # eval: 24.0 = 48 * 0.5

    #: L2

    #: FA
    answer = fraction_of_april_sales
    return answer # eval: return 0.5

def solve(
    hourly_rate: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # She did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for her babysitting work.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2

    #: FA
    answer = minutes_worked
    return answer # eval: return 50

def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = wallet_cost * betty_savings_fraction # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3

    #: FA
    answer = wallet_cost
    return answer # eval: return 100

def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = pages_read_yesterday + pages_read_today # eval: 36 = 12 + 24

    #: L3
    remaining_pages = total_pages - total_pages_read # eval: 84 = 120 - 36

    #: L4

    #: FA
    answer = total_pages
    return answer # eval: return 120

def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,  # to 2 different friends
    times_per_week: int = 2,  # twice a week
    weeks_per_year: int = 52  # in a year
):
    """Index: 4.
    Returns: the total number of pages James writes in a year."""

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week # eval: 6 = 3 * 2

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends # eval: 12 = 6 * 2

    #: L3

    #: FA
    answer = pages_per_letter
    return answer # eval: return 3

# -------------------------------------------- #
# Computational-error code with eval trace
# -------------------------------------------- #

def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""

    #: L1
    clips_sold_in_may = clips_sold_in_april * fraction_of_april_sales # eval: 24.0 = 48 * 0.5

    #: L2
    total_clips_sold = 82.0 # eval: 82.0 = 82.0

    #: FA
    answer = total_clips_sold
    return answer # eval: return 82.0

def solve(
    hourly_rate: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # She did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for her babysitting work.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2
    earnings = 11.0 # eval: 11.0 = 11.0

    #: FA
    answer = earnings
    return answer # eval: return 11.0

def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = 60.0 # eval: 60.0 = 60.0

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3
    money_still_needed = wallet_cost - betty_savings - grandparents_contribution - parents_contribution # eval: -5.0 = 100 - 60.0 - 30 - 15

    #: FA
    answer = money_still_needed
    return answer # eval: return -5.0

def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = 37 # eval: 37 = 37

    #: L3
    remaining_pages = total_pages - total_pages_read # eval: 83 = 120 - 37

    #: L4
    pages_to_read_tomorrow = remaining_pages / 2 # eval: 41.5 = 83 / 2

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 41.5

def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,  # to 2 different friends
    times_per_week: int = 2,  # twice a week
    weeks_per_year: int = 52  # in a year
):
    """Index: 4.
    Returns: the total number of pages James writes in a year."""

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week # eval: 6 = 3 * 2

    #: L2
    total_pages_per_week = 13 # eval: 13 = 13

    #: L3
    total_pages_per_year = total_pages_per_week * weeks_per_year # eval: 676 = 13 * 52

    #: FA
    answer = total_pages_per_year
    return answer # eval: return 676

# -------------------------------------------- #
# Incorrect-operand code with eval trace
# -------------------------------------------- #

def solve(
    clips_sold_in_april: int = 48,  # Natalia sold clips to 48 of her friends in April
    fraction_of_april_sales: float = 1/2  # she sold half as many clips in May
):
    """Index: 0.
    Returns: the total number of clips Natalia sold in April and May."""

    #: L1
    clips_sold_in_may = clips_sold_in_april * fraction_of_april_sales # eval: 24.0 = 48 * 0.5

    #: L2
    total_clips_sold = fraction_of_april_sales + clips_sold_in_may # eval: 24.5 = 0.5 + 24.0

    #: FA
    answer = total_clips_sold
    return answer # eval: return 24.5

def solve(
    hourly_rate: int = 12,  # Weng earns $12 an hour
    minutes_worked: int = 50  # She did 50 minutes of babysitting
):
    """Index: 1.
    Returns: the amount Weng earned for her babysitting work.
    """

    #: L1
    rate_per_minute = hourly_rate / 60 # eval: 0.2 = 12 / 60

    #: L2
    earnings = minutes_worked * minutes_worked # eval: 2500 = 50 * 50

    #: FA
    answer = earnings
    return answer # eval: return 2500

def solve(
    wallet_cost: int = 100,  # wallet costs $100
    betty_savings_fraction: float = 1/2,  # Betty has only half of the money she needs
    parents_contribution: int = 15,  # her parents decided to give her $15
    grandparents_multiplier: int = 2  # her grandparents gave twice as much as her parents
):
    """Index: 2.
    Returns: the amount of money Betty still needs to buy the wallet.
    """

    #: L1
    betty_savings = wallet_cost * betty_savings_fraction # eval: 50.0 = 100 * 0.5

    #: L2
    grandparents_contribution = parents_contribution * grandparents_multiplier # eval: 30 = 15 * 2

    #: L3
    money_still_needed = wallet_cost - betty_savings - grandparents_contribution - wallet_cost # eval: -80.0 = 100 - 50.0 - 30 - 100

    #: FA
    answer = money_still_needed
    return answer # eval: return -80.0

def solve(
        total_pages: int = 120,  # Julie is reading a 120-page book
        pages_read_yesterday: int = 12,  # Yesterday, she was able to read 12 pages
        pages_multiplier: int = 2  # today, she read twice as many pages as yesterday
    ):
    """Index: 3.
    Returns: the number of pages Julie should read tomorrow.
    """

    #: L1
    pages_read_today = pages_read_yesterday * pages_multiplier # eval: 24 = 12 * 2

    #: L2
    total_pages_read = pages_read_yesterday + pages_read_today # eval: 36 = 12 + 24

    #: L3
    remaining_pages = total_pages_read - total_pages_read # eval: 0 = 36 - 36

    #: L4
    pages_to_read_tomorrow = remaining_pages / 2 # eval: 0.0 = 0 / 2

    #: FA
    answer = pages_to_read_tomorrow
    return answer # eval: return 0.0

def solve(
    pages_per_letter: int = 3,  # James writes a 3-page letter
    num_friends: int = 2,  # to 2 different friends
    times_per_week: int = 2,  # twice a week
    weeks_per_year: int = 52  # in a year
):
    """Index: 4.
    Returns: the total number of pages James writes in a year."""

    #: L1
    pages_per_friend_per_week = pages_per_letter * times_per_week # eval: 6 = 3 * 2

    #: L2
    total_pages_per_week = pages_per_friend_per_week * num_friends # eval: 12 = 6 * 2

    #: L3
    total_pages_per_year = total_pages_per_week * total_pages_per_week # eval: 144 = 12 * 12

    #: FA
    answer = total_pages_per_year
    return answer # eval: return 144
