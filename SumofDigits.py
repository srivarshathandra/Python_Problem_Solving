# Sum of digits

# 👉 Example:
# Input: 1234 → Output: 10

# a=int(input("enter the number:"))
# total=0

# while a>0:
#     d=a%10
#     total=total+d
#     a=a//10
# print("sum",total)




# Reverse a number

# Example:

# Input: 1234
# Output: 4321

# a=int(input("enter:---"))

# b=0
# while a >0:
#     d=a%10
#     b=b*10+d
#     a=a//10
    
# print("reverse",b)

a="Varsha"
total=0
while a>0:
    d=a%10
    total=total*10+d
    a=a//10
print(total)

# palindrome
# 121 → Palindrome  
# 123 → Not Palindrome  

# n=1232421

# a=0
# b=n
# while n>0:
#     d=n%10
#     a=a*10+d
#     n=n//10
# if a==b:
#     print("palindrome")
# else:
#     print("not a palindrome")
    
    
# 👉 Check Armstrong number

# Example:

# 153 → 1³ + 5³ + 3³ = 153 ✔

# It uses the same pattern + powers

# a=1532

# t=0
# o=a
# i=len(str(a))
# while a>0:
#     d=a%10
#     t=t+d**i
#     a=a//10

# if t ==o:
#     print("Armstrong")
# else:
#     print("Not a Armstrong")


# 🔹 Q1. Count digits

# 👉 Input: 12345
# 👉 Output: 5


n=123456

total=0

while n>0:
    n=n//10
    total+=1
    
print(total)
    

# Count even and odd digits

# 👉 Input: 123456
# 👉 Output:

# Even digits: 3
# Odd digits: 3

n=123456
t=0
while n>0:
    if n% 2==0:
        t+=1
        print("even count:",t)
        
    else:
        if not n% 2==0:
            t+=1
            print("Odd digits:",t)
    