def calculate(text_input):
    print("Welcome to our calculator")
    if text_input[1] == "+":
        return int(text_input[0])+int(text_input[-1])

if __name__ == "__main__":
    calculation = input("What do you want to calculate?")
    answer = calculate(calculation)
    print(f"The result is {answer}")