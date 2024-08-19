import pandas as pd

def mark_distribution(m1,m2,m3):
  if m1 in range(0,101) and m2 in range(0,101) and m3 in range(0,101):
    tot = (m1+m2+m3)/3
    if tot >= 75 and tot <= 100:
      return "First Division with distinction"
    elif tot >=60  and tot<=74:
      return "First Division"
    elif tot >=50 and tot <=59:
      return "Second Division"
    elif tot >=40 and tot <=49:
      return "Third Division"
    else:
      return "Fail"

test_cases = []
x = [0,1,50,99,100]
for i in x:
  if [i,50,50] not in test_cases:
   test_cases.append([i,50,50])
for i in x:
  if [50,i,50] not in test_cases:
    test_cases.append([50,i,50])
for i in x:
  if [50,50,i] not in test_cases:
    test_cases.append([50,50,i])
len(test_cases)

test_cases

res = []
for i in range(len(test_cases)):
    t = i + 1
    m1 = test_cases[i][0]
    m2 = test_cases[i][1]
    m3 = test_cases[i][2]
    distribution = mark_distribution(m1, m2, m3)
    res.append([t,m1,m2,m3,distribution])
df = pd.DataFrame(data=res,columns=['Test Cases','Mark1','Mark2','Mark3','Output'])

expected_output = ["Fail","Fail","Second Division","First Division","First Division","Fail","Fail","First Division","First Division","Fail","Fail","First Division","First Division"]
df['Expected Output'] = expected_output
df['Test Case'] = (df["Output"] == df["Expected Output"]).replace({True: "Pass", False: "Fail"})
df

df.to_csv("mark.csv")

"""# Classification of a triangle"""

99 == (90+9)

def triangle(a,b,c):
  if a in range(1,101) and b in range(1,101) and c in range(1,101):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
      return ["Invalid triangle","Pass"]
    elif((c**2 == (a**2 + b**2)) or (a**2 == (b**2 + c**2)) or (b**2 == (a**2 + c**2))):
      return ["Right angled triangle","Pass"]
    elif((c**2 > (a**2 + b**2)) or (a**2 > (b**2 + c**2)) or (b**2 > (a**2 + c**2))):
      return ["Obtuse triangle","Pass"]
    else:
      return ["Acute triangle","Pass"]
  else:
    return ["Invalid triabgle","Fail"]

test_cases = []
x = [1,2,50,99,100]
for i in x:
  if [i,50,50] not in test_cases:
   test_cases.append([i,50,50])
for i in x:
  if [50,i,50] not in test_cases:
    test_cases.append([50,i,50])
for i in x:
  if [50,50,i] not in test_cases:
    test_cases.append([50,50,i])
len(test_cases)

res = []
for i in range(len(test_cases)):
  t = i + 1
  a = test_cases[i][0]
  b = test_cases[i][1]
  c = test_cases[i][2]
  ans = triangle(a,b,c)
  res.append([t,a,b,c,ans[0],ans[1]])
df = pd.DataFrame(data=res,columns=['Test Cases','a','b','c','Output','Expected Output'])

df

"""# Date time"""

from datetime import datetime

def Time(y,m,d):
  if (y>=1900 and y<=2058) and (m>=1 and m<=12) and (d>=1 and d<=31):
    try:
      date = datetime(y,m,d)
      return [date.strftime("%A"),"Pass"]
    except:
      return ["Invalid date","Pass"]
  else:
    return ["Invalid date","Fail"]

test_cases = []
for i in [1,2,6,11,12]:
  if [i,15,1979] not in test_cases:
    test_cases.append([i,15,1979])
for i in [1,2,15,30,31]:
  if [6,i,1979] not in test_cases:
    test_cases.append([6,i,1979])
for i in [1900,1901,1979,2057,2058]:
  if [6,15,i] not in test_cases:
    test_cases.append([6,15,i])

res = []
for test in test_cases:
  t = t+1
  m = test[0]
  d = test[1]
  y = test[2]
  ans = Time(y,m,d)
  res.append([t,m,d,y,ans[0],ans[1]])
df = pd.DataFrame(data=res,columns=['Test Cases','Month','Day','Year','Output','Expected Output'])

df

"""# PROMBLEM SHEET 1 AND 3

factorial
"""

def factorial(n):
  if type(n)!=int or n<0 or str(n).isdigit() and (str(n)==0 or not str(n).startswith('0')):
    return "Not valid input"
  if n == 0 or n==1:
    return 1
  return n * factorial(n-1)
# POSITIVE TEST CASES
print("factorial(0) = ",factorial(0))
print("factorial(1) = ",factorial(1))
print("factorial(950) = ",factorial(950))
print("factorial(949) = ",factorial(949))
# Negative test cases

print("factorial(+1)",factorial(+1))
print("factorial(-1)",factorial(-1))
print("factorial( 1)",factorial( 1))
print("factorial(1.5)", factorial(1.5))
print("factorial(1.5e)",factorial('e'))
print("factorial(1.5e-1)",factorial(1.5e-1))

"""password"""

def checkPassword(password):
  if len(password) < 6:
    return "Password must be at least 6 characters long"
  elif len(password) > 12:
    return "Password must be less than 12 characters long"
  else:
    return "Valid password"
# Testcases
print("12345:",checkPassword("12345"))
print("123456:",checkPassword("123456"))
print("1234567:",checkPassword("1234567"))
print("123456789012",checkPassword("123456789012"))
print("1234567890123",checkPassword("1234567890123"))

"""calculate discount"""

def calculate_discount(purchase_amount):
    if 1 <= purchase_amount <= 50:
        return 'No Discount'
    elif 51 <= purchase_amount <= 200:
        return '5% Discount'
    elif 201 <= purchase_amount <= 500:
        return '10% Discount'
    elif purchase_amount >= 501:
        return '15% Discount'
    else:
        return 'Invalid'

def test(f, test_cases):
    result = []
    for input, expected in test_cases:
        output = f(input)
        if output == expected:
            result.append([input, expected, output, 'PASSED'])
        else:
            result.append([input, expected, output, 'FAILED'])
    return result

test_cases = [
    # Valid Equivalence Class for No Discount
    (10, 'No Discount'),  # Any value within 1 to 50
    (50, 'No Discount'),  # Upper boundary within 1 to 50

    # Valid Equivalence Class for 5% Discount
    (100, '5% Discount'),  # Any value within 51 to 200
    (200, '5% Discount'),  # Upper boundary within 51 to 200

    # Valid Equivalence Class for 10% Discount
    (300, '10% Discount'),  # Any value within 201 to 500
    (500, '10% Discount'),  # Upper boundary within 201 to 500

    # Valid Equivalence Class for 15% Discount
    (600, '15% Discount'),  # Any value above 501

    # Invalid Equivalence Classes
    (0, 'Invalid'),       # Value below minimum boundary
    (51, '5% Discount'),  # Just above No Discount boundary (valid for 5% Discount)
    (201, '10% Discount'),  # Just above 5% Discount boundary (valid for 10% Discount)
    (501, '15% Discount'),  # Just above 10% Discount boundary (valid for 15% Discount)
]

result = test(calculate_discount, test_cases)

import pandas as pd
df = pd.DataFrame(data = result, columns=['INPUT', 'EXPECTED', 'OUTPUT', 'TEST_RESULT'])
df.to_csv('discount_test_ep_result.csv', index=False)
print(df)

"""determining grade of student"""

def determine_grade(mark1, mark2, mark3):
    if not all(isinstance(mark, int) for mark in [mark1, mark2, mark3]):
        return "Invalid input: Marks must be integers."
    if not all(0 <= mark <= 100 for mark in [mark1, mark2, mark3]):
        return "Invalid input: Marks must be between 0 and 100."

    total_marks = (mark1 + mark2 + mark3) // 3

    if  total_marks >= 90 and total_marks <= 100:
        return "First Class Distinction"
    elif  total_marks >= 75 and total_marks <= 89:
        return "First Class"
    elif total_marks >= 60 and total_marks <= 74:
        return "Second Class"
    elif total_marks >= 50 and total_marks <= 59:
        return "Third Class"
    else:
        return "Fail"
test_cases = [
        (90, 90, 90, "First Class Distinction"),
        (75, 75, 75, "First Class"),
        (60, 60, 60, "Second Class"),
        (50, 50, 50, "Third Class"),
        (49, 49, 49, "Fail"),
        (100, 100, 100, "First Class Distinction"),
        (0, 0, 0, "Fail"),
        (101, 50, 50, "Invalid input: Marks must be between 0 and 100."),
        (-1, 50, 50, "Invalid input: Marks must be between 0 and 100."),
        ("a", 50, 50, "Invalid input: Marks must be integers."),
        (50.5, 50, 50, "Invalid input: Marks must be integers."),
        (85, 90, 95, "First Class Distinction"),
        (70, 75, 80, "First Class"),
        (65, 60, 70, "Second Class"),
        (55, 50, 55, "Third Class"),
        (45, 40, 35, "Fail")
    ]

for mark1, mark2, mark3, expected in test_cases:
    result = determine_grade(mark1, mark2, mark3)
    print(f"Marks: ({mark1}, {mark2}, {mark3}) -> Expected: {expected}, Got: {result}")

"""order pizza"""

def orderPizza(n):
  if not isinstance(n,int) or n<=0:
    return "not valid input"
  elif n >=1 and n<=10:
     return f"success {n} pizzas order placed."
  elif n>=11 and n<=99:
    return "Only 10 Pizza can be ordered"
  else:
    return "Maximum order limit is 99"
print("Output for 11 pizza ordered:",orderPizza(11))
print("Output for 0 pizza ordered:",orderPizza(0))
print("Output for -1 pizza ordered:",orderPizza(-1))
print("Output for 99 pizza ordered:",orderPizza(99))
print("Output of 101 pizza ordered:",orderPizza(101))
# valid input
print("Output for 5 pizza ordered:",orderPizza(5))

"""Tax Calculation Problem."""

def tax_pays(pay):
  if 12000 <= pay <= 15000:
    expected_tax_rate = 0
  elif 15001 <= pay <= 25000:
    expected_tax_rate = 0.18
  elif 25001 <= pay <= 35000:
    expected_tax_rate = 0.20
  else:
    expected_tax_rate = "Invalid Input"

  if expected_tax_rate != "Invalid Input":
    tax_amount = pay * expected_tax_rate
  else:
    tax_amount = "NA"

  return f"Pay: Rs. {pay}, Expected Tax Rate: {expected_tax_rate}, Tax Amount: Rs. {tax_amount}"
test_cases = [
    11999,
    12000,
    14000,
    15000,
    15001,
    20000,
    25000,
    25001,
    34999,
    35000,
    35001,
    23500
]

for pay in test_cases:
    print(tax_pays(pay))