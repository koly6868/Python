import json
import StringModule
import NumericAlgoritmhs as NA
import Analizator

with open("configuration.json", "r") as read_file:
    data = json.load(read_file)

# code
print("Hello")
print(max(2, 4))
a = input("please\n")
answ = NA.SimpleMultiplaers(int(a))
print(answ)