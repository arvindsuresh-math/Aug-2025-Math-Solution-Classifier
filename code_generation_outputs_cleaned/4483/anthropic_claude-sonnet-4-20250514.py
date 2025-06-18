def solve(
    sammys_price_per_record: int = 4, # Sammy will buy all records for 4 dollars each
    bryans_price_interested: int = 6, # Bryan will offer 6 dollars each for the half he's interested in
    bryans_price_not_interested: int = 1, # Bryan will offer 1 dollar each for the remaining half
    total_records: int = 200 # Peggy has 200 records
):
    """Code for Q 4483 from the GSM8K dataset (train).
    Returns the difference in profit between Sammy's deal versus Bryan's deal.
    """
    # Sammy is offering to take the whole collection of 200 records and pay Peggy 4 dollars each for them which would net Peggy 200 * 4=<<200*4=800>>800 dollars for her entire record collection.
    sammys_total_offer = total_records * sammys_price_per_record
    
    # Bryan is willing to buy Peggy's entire record collection but at two different price points, half at one point and half at another. Half of Peggy's record collection is 200/2=<<200/2=100>>100, which means that 100 records will sell for one price and 100 records will sell for another price.
    half_records = total_records / 2
    
    # Bryan is willing to pay more for the half of the record collection that he is interested in so Peggy would net 100 * 6=<<100*6=600>>600 dollars for the first half of her record collection.
    bryans_payment_interested_half = half_records * bryans_price_interested
    
    # For the half of the collection that Bryan is just planning on reselling at a later date, he is willing to offer Peggy 100 *1=<<100*1=100>>100 dollars to take off of her hands.
    bryans_payment_not_interested_half = half_records * bryans_price_not_interested
    
    # In total Bryan is willing to offer Peggy 600+100=<<600+100=700>>700 dollars for her entire record collection.
    bryans_total_offer = bryans_payment_interested_half + bryans_payment_not_interested_half
    
    # If Sammy is offering 800 dollars to buy Peggy's entire record collection and Bryan is offering 700 dollars for Peggy's entire record collection, then Peggy's net profit would be 800-700=<<800-700=100>>100 dollars more by taking Sammy's deal instead of Bryan's deal.
    profit_difference = sammys_total_offer - bryans_total_offer
    
    # The final answer is the difference in profit between the two deals
    return profit_difference