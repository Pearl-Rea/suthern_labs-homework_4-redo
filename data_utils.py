#Author:Pearl

"""Utility modules for calculating averages an d formatting South Africsan Rand."""

def calculate_average(number1, number2, number3, number4, number5):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
         numbers_list: A list of numeric values number1, number2, number3, number4, number5.

    
    Returns:
        float: The arithmetic mean.
        """
    return (number1 + number2 + number3 + number4 + number5)/ 5

def format_currency(amount):
    """
    format an amount of South African Rand.

    Args:
         amount: The numeric  amount to format .

    Returns:
             A formatted currency string, for example R150.50.
             """

    rounded_amount = round(amount, 2)
    results = "R" + str(rounded_amount)
    return results

       
