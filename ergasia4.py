n1 = input("Enter first number(zero-nine):")
n2 = input("Enter second number(zero-nine):")
praxh = input("Enter an action between the two numbers(plus,minus,times,divided):")


def zero():
  a = 0
  return a
def one():
  a = 1
  return a
def two():
  a = 2
  return a
def three():
  a = 3
  return a
def four():
  a = 4
  return a
def five():
  a = 5
  return a
def six():
  a = 6
  return a
def seven():
  a = 7
  return a
def eight():
  a = 8
  return a
def nine():
  a = 9
  return a

def plus(a,b):
  c = a + b
  return c
def minus(a,b):
  c = a - b
  return c
def times(a,b):
  c = a * b
  return c
def divided(a,b):
  if b!= 0:
    c = a // b
  else:
    c = "oxi me to mhden"
  return c

if n1 == "zero":
  a = zero()
elif n1 == "one":
  a = one()
elif n1 == "two":
  a = two()
elif n1 == "three":
  a = three()
elif n1 == "four":
  a = four()
elif n1 == "five":
  a = five()
elif n1 == "six":
  a = six()
elif n1 == "seven":
  a = seven()
elif n1  == "eight":
  a = eight()
elif n1 == "nine":
  a = nine()


if n2 == "zero":
  b = zero()
elif n2 == "one":
  b = one()
elif n2 == "two":
  b = two()
elif n2 == "three":
  b = three()
elif n2 == "four":
  b = four()
elif n2 == "five":
  b = five()
elif n2 == "six":
  b = six()
elif n2 == "seven":
  b = seven()
elif n2 == "eight":
  b = eight()
elif n2 == "nine":
  b = nine()

if praxh ==  "plus":
  c = plus(a,b)
elif praxh == "minus":
  c = minus(a,b)
elif praxh  == "times":
  c = times(a,b)
elif praxh == "divided":
  c= divided(a,b)

print (c)
