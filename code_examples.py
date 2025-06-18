examples_indices = []

examples_indices.append(310)
def Q_310(
        num_employees: int = 6, # Janet hires six employees
        num_warehouse_workers: int = 4, # four of them are warehouse workers
        num_managers: int = 2, # the other two are managers
        hourly_wage_warehouse: int = 15, # warehouse workers make $15/hour
        hourly_wage_manager: int = 20, # managers make $20/hour
        fica_tax_rate: float = 0.1, # FICA tax rate is 10%
        days_per_month: int = 25, # each worker works 25 days a month
        hours_per_day: int = 8 # each worker works 8 hours a day
    ):
    """Code for Q 310 from the GSM8K dataset (train).
    Returns the monthly total wage bill, including FICA taxes.
    """
    # First figure out how many hours each worker works per month by multiplying the number of days they work by the number of hours a day they work: 25 days * 8 hours/day = <<25*8=200>>200 hours
    hours_per_month = days_per_month * hours_per_day
    assert hours_per_month == 200

    # Then calculate how much one warehouse worker makes per month by multiplying their hourly rate by the number of hours they work: 200 hours * $15/hour = $<<200*15=3000>>3000
    monthly_wage_warehouse = hourly_wage_warehouse * hours_per_month
    assert monthly_wage_warehouse == 3000

    # Then multiply that number by 4 to find out how much all the warehouse workers make: $3000/worker * 4 workers = $<<3000*4=12000>>12,000
    total_wage_warehouse = monthly_wage_warehouse * num_warehouse_workers
    assert total_wage_warehouse == 12000

    # Now multiply the hours each manager works (also 200) by their hourly wage to find out how much one manager makes per month: 200 hours * $20/hour = $<<200*20=4000>>4,000
    monthly_wage_manager = hourly_wage_manager * hours_per_month
    assert monthly_wage_manager == 4000

    # Now multiply one manager's wages by the number of managers (2) to find their total wage amount: $4,000/manager * 2 managers = $<<4000*2=8000>>8,000
    total_wage_manager = monthly_wage_manager * num_managers
    assert total_wage_manager == 8000

    # Now add the wages for the managers and the workers to find the total cost of the wages: $8,000 + $12,000 = $<<8000+12000=20000>>20,000
    total_wages = total_wage_warehouse + total_wage_manager
    assert total_wages == 20000

    # Now multiply the total wage bill by 10% to find how much the FICA taxes are: $20,000 * .1 = $<<20000*.1=2000>>2,000
    fica_taxes = total_wages * fica_tax_rate
    assert fica_taxes == 2000

    # Now add the total wage bill to the total tax amount to find the grand total: $20,000 + $2,000 = $<<20000+2000=22000>>22,000
    grand_total = total_wages + fica_taxes
    assert grand_total == 22000

    # The final answer is the grand total
    return grand_total

examples_indices.append(3822)
def Q_3822(
        fraction_needed_to_win: float = 3/4,  # Alec needs three-quarters of the class to vote for him
        fraction_voting_for_him: float = 1/2,  # Half of the class has already said they will vote for him
        students_thinking_about_it: int = 5,  # Number of students thinking about voting for him
        total_students: int = 60  # Total number of students in Alec's class
):    
    """Code for Q 3822 from the GSM8K dataset (train).
    Returns the number of votes by which Alec is short of his goal.
    """
    # To calculate Alec's goal number of votes, we need to know that 60 students / 4 = <<60/4=15>>15 students is equal to one-quarter of the class students.
    students_per_quarter = total_students / 4
    assert students_per_quarter == 15

    # Alec's goal is therefore 15 students * 3 quarters = <<15*3=45>>45 votes.
    votes_needed = students_per_quarter * 3
    assert votes_needed == 45

    # Half of the class said they will vote for him, so there are already 60 students / 2 = <<60/2=30>>30 votes.
    votes_for_him = total_students * fraction_voting_for_him
    assert votes_for_him == 30

    # Another 5 students are thinking about voting for him which leaves a total so far of 30 + 5 = <<30+5=35>>35 votes.
    votes_so_far = votes_for_him + students_thinking_about_it
    assert votes_so_far == 35

    # This means there are 60 students - 35 voting for Alec = <<60-35=25>>25 students not voting for Alec.
    students_not_voting_for_him = total_students - votes_so_far
    assert students_not_voting_for_him == 25
    
    # A fifth of these say they will vote for him, so this is a further 25 students / 5 = <<25/5=5>>5 votes.
    new_votes = students_not_voting_for_him / 5
    assert new_votes == 5

    # Alec is therefore receiving a total of 35 + 5 = <<35+5=40>>40 votes.
    total_votes_for_him = votes_so_far + new_votes
    assert total_votes_for_him == 40

    # So he has missed his goal by 45 goal votes - 40 actual votes = <<45-40=5>>5 votes.
    votes_short_of_goal = votes_needed - total_votes_for_him
    assert votes_short_of_goal == 5

    # The final answer is the number of students Alec is short of his goal
    return votes_short_of_goal

examples_indices.append(2345)
def Q_2345(
        peppers_per_very_spicy: int = 3,  # Peppers needed for very spicy curries
        peppers_per_spicy: int = 2,  # Peppers needed for spicy curries
        peppers_per_mild: int = 1,  # Peppers needed for mild curries
        previous_very_spicy_curries: int = 30, # Number of very spicy curries previously made
        previous_spicy_curries: int = 30, # Number of spicy curries previously made
        previous_mild_curries: int = 10, # Number of mild curries previously made
        spicy_curries_now: int = 15, # Number of spicy curries now
        mild_curries_now: int = 90 # Number of mild curries now
):
    """Code for Q 2345 from the GSM8K dataset (train).
    Returns how many fewer peppers the curry house buys now compared to before."""
    # The curry house previously bought 3 peppers per very spicy curry * 30 very spicy curries = <<3*30=90>>90 peppers for very spicy curries.
    previous_peppers_for_very_spicy = peppers_per_very_spicy * previous_very_spicy_curries
    assert previous_peppers_for_very_spicy == 90

    # They also bought 2 peppers per spicy curry * 30 spicy curries = <<2*30=60>>60 peppers for spicy curries.
    previous_peppers_for_spicy = peppers_per_spicy * previous_spicy_curries
    assert previous_peppers_for_spicy == 60

    # They also bought 1 pepper per mild curry * 10 mild curries = <<1*10=10>>10 peppers for mild curries.
    previous_peppers_for_mild = peppers_per_mild * previous_mild_curries
    assert previous_peppers_for_mild == 10

    # So they were previously buying 90 + 60 + 10 = <<90+60+10=160>>160 peppers.
    previous_total_peppers = (previous_peppers_for_very_spicy + 
                            previous_peppers_for_spicy + 
                            previous_peppers_for_mild)
    assert previous_total_peppers == 160
    
    # They now buy 2 peppers per spicy curry * 15 spicy curries = <<2*15=30>>30 peppers for spicy curries.
    new_peppers_for_spicy = peppers_per_spicy * spicy_curries_now
    assert new_peppers_for_spicy == 30

    #They also now buy 1 pepper per mild curry * 90 mild curries = <<1*90=90>>90 peppers for mild curries.
    new_peppers_for_mild = peppers_per_mild * mild_curries_now
    assert new_peppers_for_mild == 90

    #So they now buy 30 + 90 = <<30+90=120>>120 peppers.
    new_total_peppers = new_peppers_for_spicy + new_peppers_for_mild
    assert new_total_peppers == 120

    #This is a difference of 160 peppers bought originally - 120 peppers bought now = <<160-120=40>>40 peppers.
    fewer_peppers = previous_total_peppers - new_total_peppers
    assert fewer_peppers == 40

    # The final answer is the number of fewer peppers bought
    return fewer_peppers

examples_indices.append(1202)
def Q_1202(
    rent_apt1: int = 800, # Rent for apt 1
    utilities_apt1: int = 260, # Utilities for apt 1
    miles_apt1: int = 31, # Miles driven per day for apt 1
    rent_apt2: int = 900, # Rent for apt 2
    utilities_apt2: int = 200, # Utilities for apt 2
    miles_apt2: int = 21, # Miles driven per day for apt 2
    cost_per_mile: float = 0.58, # Cost per mile in dollars
    work_days_per_month: int = 20 # Work days per month
):
    """Code for Q 1202 from the GSM8K dataset (train).
    Returns the difference in total costs between the two apartments."""
    
    # The mileage cost for the first apartment will be 31*20*0.58 = $<<31*20*0.58=359.60>>359.60
    mileage_cost_apt1 = miles_apt1 * cost_per_mile * work_days_per_month
    assert mileage_cost_apt1 == 359.60

    # This makes the total monthly cost of the first apartment 359.60 + 800 + 260 = $<<359.60+800+260=1419.60>>1419.60
    total_cost_apt1 = rent_apt1 + utilities_apt1 + mileage_cost_apt1
    assert total_cost_apt1 == 1419.60

    # Similarly, the mileage cost for the second apartment will be 21*20*0.58 = $<<21*20*0.58=243.60>>243.60
    mileage_cost_apt2 = miles_apt2 * cost_per_mile * work_days_per_month
    assert mileage_cost_apt2 == 243.60

    # Thus, the total monthly cost of the second apartment is 243.60 + 900 + 200 = <<243.60+900+200=1343.60>>1343.60
    total_cost_apt2 = rent_apt2 + utilities_apt2 + mileage_cost_apt2
    assert total_cost_apt2 == 1343.60

    # Therefore, the difference in total monthly costs is 1419.60 - 1343.60 = $<<1419.60-1343.60=76>>76
    cost_difference = total_cost_apt1 - total_cost_apt2
    assert cost_difference == 76

    # The final answer is the cost difference
    return cost_difference

examples_indices.append(7371)
def Q_7371(
    baseline_avg_score: int = 75, # Karen wants an average score of 75
    bonus_if_avg_above_baseline = 500, # Karen gets a $500 bonus if their average score is above 75
    extra_bonus_per_point = 10, # Karen gets an extra $10 for every point above 75
    tests_graded_so_far = 8, # So far, Karen has graded 8 tests
    avg_so_far = 70, # The average score so far is 70
    max_score_per_student = 150, # each student can have a maximum score of 150
    desired_bonus = 600 # Karen wants to earn a $600 bonus
):
    """Code for Q 7371 from the GSM8K dataset (train).
    Returns the combined score needed in the last two tests to ensure that Karen earns a $600 bonus."""
    # First subtract $500 from Karen's goal bonus amount to find how much she makes from the extra $10/point bonus: $600 - $500 = $<<600-500=100>>100
    extra_bonus_needed = desired_bonus - bonus_if_avg_above_baseline
    assert extra_bonus_needed == 100

    # Then divide the extra bonus by the extra rate: $100 / $10/point = <<100/10=10>>10 points
    extra_points_needed = extra_bonus_needed / extra_bonus_per_point
    assert extra_points_needed == 10

    # Then add the 10 extra points to the baseline 75 point goal to find the students' average test score: 10 points + 75 points = <<10+75=85>>85 points
    target_avg_score = baseline_avg_score + extra_points_needed
    assert target_avg_score == 85

    # Then added the 8 graded tests to the 2 ungraded tests to find the total number of tests: 2 tests + 8 tests = <<2+8=10>>10 tests
    total_tests = tests_graded_so_far + 2
    assert total_tests == 10

    # Then multiply the 85 point average by the number of tests to find the total number of points the students need to earn: 85 points/test * 10 tests = 850 points
    total_points_needed = target_avg_score * total_tests
    assert total_points_needed == 850

    # Then multiply the current average by the current number of graded tests to find how many points have been earned so far: 70 points/test * 8 tests = <<70*8=560>>560 points
    points_earned_so_far = avg_so_far * tests_graded_so_far
    assert points_earned_so_far == 560

    # Then subtract the number of points earned from the number of points needed to find the combine score the last two tests need: 850 points - 560 points = <<850-560=290>>290 points
    points_needed_last_two_tests = total_points_needed - points_earned_so_far
    assert points_needed_last_two_tests == 290

    # The final answer is the combined score needed in the last two tests
    return points_needed_last_two_tests

