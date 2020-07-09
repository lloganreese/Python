import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

for index, name in enumerate(order_of_succession, start=0):
    string_to_print = f"{index + 1}. {name}"
    print(string_to_print)
