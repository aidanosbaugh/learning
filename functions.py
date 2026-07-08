
## Function that prompts user for name and greets them
def greet():
    name = input("Hello, what is your name?")
    print("Hello", name)

## Function that calculates simple interest
def interest():
    capital = float(input("What is the starting amount?"))
    return_rate = float(input("What is the annual return rate?"))
    term = int(input("How many years?"))

    new_amount = capital * (1 + return_rate/100)**term
    accrued_amount = new_amount - capital

    print("New total is:", new_amount)
    print("Accrued interest is:", accrued_amount)

## Function that converts percents to decimals

def conversion():
    percent = float(input("What is the percent?"))
    decimal = percent / 100

    print(percent, "%", "is the same as", decimal)
