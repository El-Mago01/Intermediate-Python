def sum_of_digits(num):
    sum = 0
    for digit in str(num):
      sum += int(digit)
    return sum

def subtract_digits(num):
    sub = 0
    for digit in str(num):
        sub -= int(digit)

    return sub

def main():
    print("Welcome to masterlib library! Enjoy your usage!")

if __name__ == "__main__":
    main()
