# 1.Even or Odd
# 👉 Check if a number is even or odd.
# Input: 4
# Output: Even


# conditional statements

# if - else

a=int(input("enter the number:"))
if a % 2==0:
    print("even")
else:
    print("odd")

# while

n=int(input("enter the num:"))
while True:
    if n%2==0:
        print("Even")
    else:
        print("Odd")
    break

# loops
a=input("enter the number:")
for i in a:
    b=int(i)
    if b % 2 == 0:
        print("Even")
    else:
        print("odd")
        
# functions

def EvenOdd(q):
    if  q%2==0:
        print("even")
    else:
        print("odd")
        
EvenOdd(4)

# for loop using range

for i in range(1,10,2):
    print(i)

for i in range(1, 10):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")
        
