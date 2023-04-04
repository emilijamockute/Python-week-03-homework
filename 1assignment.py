def sum_of_digits():
    num = input("Input value: ")
    sum = 0

    for i in num:
        sum = sum + int(i)

    print("Output result:", sum)

    # Function call


sum_of_digits()