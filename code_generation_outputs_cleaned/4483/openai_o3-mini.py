def solve(
    sammy_price: int = 4,  # Sammy says that he will buy all of them for 4 dollars each
    records: int = 200,  # Peggy has 200 records
    bryan_interested_price: int = 6,  # Bryan will offer 6 dollars each for the half he is interested in
    bryan_not_interested_price: int = 1  # Bryan will offer 1 dollar each for the half he is not interested in
):
    """Code for Q 4483 from the GSM8K dataset (train).
    Returns the difference in profit between Sammy's deal and Bryan's deal.
    """
    # Sammy's deal: 200 records * 4 dollars = <<200*4=800>>800 dollars
    total_sammy = records * sammy_price

    # Determine half of the records: 200/2 = <<200/2=100>>100 records for each price in Bryan's deal
    half_records = records // 2

    # For the half Bryan is interested in: 100 records * 6 dollars = <<100*6=600>>600 dollars
    bryan_first_half = half_records * bryan_interested_price

    # For the half Bryan is not interested in: 100 records * 1 dollar = <<100*1=100>>100 dollars
    bryan_second_half = half_records * bryan_not_interested_price

    # Total offered by Bryan: 600 + 100 = <<600+100=700>>700 dollars
    total_bryan = bryan_first_half + bryan_second_half

    # The difference in profit: Sammy's 800 dollars - Bryan's 700 dollars = <<800-700=100>>100 dollars more with Sammy's deal
    profit_difference = total_sammy - total_bryan

    # The final answer is the profit difference between Sammy's deal and Bryan's deal
    return profit_difference