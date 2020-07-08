import sys

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])

sum = first_number + second_number

if sum <= 0:
    print("You have chosen the path of destitution.")
elif 1 <= sum <= 100:
    print("You have chosen the path of plenty.")
else:
    print("You have chosen the path of excess.")
