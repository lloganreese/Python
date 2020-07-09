import sys

inputs = sys.argv
inputs.pop(0)



for index, number in enumerate(inputs, start=0):
    if (int(number) % 3 == 0) and (int(number) % 5 == 0):
        print('fizzbuzz')
    elif int(number) % 5 == 0:
        print('buzz')
    elif int(number) % 3 == 0:
        print('fizz')
    else:
        print(number)
