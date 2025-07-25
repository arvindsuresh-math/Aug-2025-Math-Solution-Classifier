# Calculate Noah's sales for last month
large_painting_price = 60
small_painting_price = 30
large_paintings_sold_last_month = 8
small_paintings_sold_last_month = 4

# Calculate earnings from large paintings last month
earnings_large_paintings = large_painting_price * large_paintings_sold_last_month

# Calculate earnings from small paintings last month
earnings_small_paintings = small_painting_price * small_paintings_sold_last_month

# Calculate total sales for last month
total_sales_last_month = earnings_large_paintings + earnings_small_paintings

# Calculate sales for this month (twice last month's sales)
sales_this_month = total_sales_last_month * 2

# Print the results in the specified format
print(f'{{"L1": "Noah earned ${large_painting_price}/large painting x {large_paintings_sold_last_month} large paintings = ${earnings_large_paintings}", "L2": "He also earned ${small_painting_price}/small painting x {small_paintings_sold_last_month} small paintings = ${earnings_small_paintings}", "L3": "His total sales last month were ${earnings_large_paintings} + ${earnings_small_paintings} = ${total_sales_last_month}", "L4": "So, his sales this month are ${total_sales_last_month} x 2 = ${sales_this_month}"}}')

def solve_31():
    large_painting_price = 60
    small_painting_price = 30
    large_paintings_sold_last_month = 8
    small_paintings_sold_last_month = 4
    
    earnings_large_paintings = large_painting_price * large_paintings_sold_last_month
    earnings_small_paintings = small_painting_price * small_paintings_sold_last_month
    total_sales_last_month = earnings_large_paintings + earnings_small_paintings
    sales_this_month = total_sales_last_month * 2
    
    return sales_this_month