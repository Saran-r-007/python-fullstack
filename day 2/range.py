
value = list(range(10))
print(value)

#range -> single value -> range(stop) ex: 10 -> 0 to 9
value2 = list(range(10))
print(value2) # 0 to 9

#range -> two values -> range(start, stop) ex: 10, 20 -> 10 to 19
value3 = list(range(10, 20))
print(value3) # 10 to 19

#postive step -> range(start, stop, step) ex: 10, 20, 2 -> 10 to 18 with step of 2
value4 = list(range(10, 20, 2)) #start which must be less than stop, step must be positive
print(value4) # 10, 12, 14, 16, 18

#negative step -> range(start, stop, step) ex: 20, 10, -2 -> 20 to 12 with step of -2
value5 = list(range(20, 10, -2))
print(value5) # 20, 18, 16, 14, 12

value6 = list(range(20, 100, -2))
print(value6)