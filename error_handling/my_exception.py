class NegativeValueError(Exception):
    pass

class TooSmallTransaction(Exception):
    pass
while True:
    try:
        transaction = float(input("Enter value for transaction: "))
        
        if transaction <= 0:
            raise NegativeValueError
        elif transaction < 30:
            raise TooSmallTransaction
        
        break
        
    except NegativeValueError:
        print("Cannot transfer negative amount of money!")
    except TooSmallTransaction:
        print("At least 30 leva must be transfered!")

        
print(f"Successful transaction of {transaction:.2f} leva.")