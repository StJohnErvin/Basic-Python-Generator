#using generator
def fib(number):
    a = 0
    b = 1
    for i in range(number):
      yield a
      temp = a
      a = b
      b = temp + b

for x in fib(20):
  print(x)


# def fib2(number):
#     a = 0
#     b = 1
#     result = []
#     for i in range(number):
#       result.append(a)
#       temp = a
#       a = b
#       b = temp + b
#     return result

# print(fib2(100))

    
