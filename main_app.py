#Author:Pearl

import random
import datetime
import data_utils


def main():

    amount1 = random.randint(50,500)
    amount2 = random.randint(50,500)
    amount3 = random.randint(50,500)
    amount4 = random.randint(50,500)
    amount5 = random.randint(50,500)
     
    today = datetime.date.today()

    average = data_utils.calculate_average(amount1, amount2, amount3, amount4, amount5)

    formatted_currency = data_utils.format_currency(average)
    
    print("SOUTHERN LABS TRANSACTION SUMMARY")
    print("Date:", today)
    print("Transaction 1:", amount1)
    print("Transaction 2:", amount2)
    print("Transaction 3:", amount3)
    print("Transaction 4:", amount4)
    print("Transaction 5:", amount5)
    print("Transaction Average:", average)
    print("Average transaction:",formatted_currency)

if __name__ == "__main__":
    main() 

