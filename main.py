import json
import StringModule
from NumericAlgoritmhs import max, Fibonachi
import Analizator

with open("configuration.json", "r") as read_file :
    data = json.load(read_file)

#code
print("Hello")
print(max(2,4))

nums = Fibonachi(1000)
print(Analizator.linarFunct(nums))

if data["isDebug"] :
    input("Press Enter")