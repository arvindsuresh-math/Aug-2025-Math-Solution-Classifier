def solve():
    """Index: 2684.
    Returns: the total dollars the fair made.
    """
    # L1
    total_ticket_revenue = 2520 # The fair made $2520 from tickets
    ticket_price = 5 # charges $5 for a ticket
    total_attendees = total_ticket_revenue / ticket_price

    # L2
    food_numerator = 2 # Two-thirds of the people
    food_denominator = 3 # Two-thirds of the people
    people_buying_food = total_attendees * food_numerator / food_denominator

    # L3
    food_price = 8 # deep-fried fair food for $8
    revenue_from_food = people_buying_food * food_price

    # L4
    ride_denominator = 4 # one quarter will go on a ride
    people_going_on_ride = total_attendees / ride_denominator

    # L5
    ride_price = 4 # a ride for $4
    revenue_from_rides = people_going_on_ride * ride_price

    # L6
    souvenir_denominator = 8 # one eighth will spend $15 on a souvenir
    people_buying_souvenir = total_attendees / souvenir_denominator

    # L7
    souvenir_price = 15 # $15 on a souvenir
    revenue_from_souvenirs = people_buying_souvenir * souvenir_price

    # L8
    total_revenue = total_ticket_revenue + revenue_from_food + revenue_from_rides + revenue_from_souvenirs

    # FA
    answer = total_revenue
    return answer