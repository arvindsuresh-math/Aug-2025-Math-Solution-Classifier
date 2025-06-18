def solve(
        total_records: int = 200,  # Peggy has 200 records
        sammy_price_per_record: int = 4,  # Sammy offers $4 per record
        bryan_high_price_per_record: int = 6,  # Bryan offers $6 for half the records
        bryan_low_price_per_record: int = 1  # Bryan offers $1 for the other half
    ):
    """Code for Q 4483 from the GSM8K dataset (train).
    Returns the difference in profit between Sammy's and Bryan's offers.
    """
    # Sammy is offering to take the whole collection of 200 records and pay Peggy 4 dollars each for them which would net Peggy 200 * 4=<<200*4=800>>800 dollars for her entire record collection.
    sammy_total_offer = total_records * sammy_price_per_record

    # Half of Peggy's record collection is 200/2=<<200/2=100>>100, which means that 100 records will sell for one price and 100 records will sell for another price.
    half_records = total_records // 2

    # Bryan is willing to pay more for the half of the record collection that he is interested in so Peggy would net 100 * 6=<<100*6=600>>600 dollars for the first half of her record collection.
    bryan_high_price_offer = half_records * bryan_high_price_per_record

    # For the half of the collection that Bryan is just planning on reselling at a later date, he is willing to offer Peggy 100 *1=<<100*1=100>>100 dollars to take off of her hands.
    bryan_low_price_offer = half_records * bryan_low_price_per_record

    # In total Bryan is willing to offer Peggy 600+100=<<600+100=700>>700 dollars for her entire record collection.
    bryan_total_offer = bryan_high_price_offer + bryan_low_price_offer

    # If Sammy is offering 800 dollars to buy Peggy's entire record collection and Bryan is offering 700 dollars for Peggy's entire record collection, then Peggy's net profit would be 800-700=<<800-700=100>>100 dollars more by taking Sammy's deal instead of Bryan's deal.
    profit_difference = sammy_total_offer - bryan_total_offer

    # The final answer is the difference in profit between Sammy and Bryan's offers
    return profit_difference