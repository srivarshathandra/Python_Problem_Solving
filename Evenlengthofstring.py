# Write a program that takes a string, string should be of even length.
# Divide the string into two equals parts, 
# check the number of vowels in both the parts of the string.
# If both parts of string have same number of vowels then return true 
# otherwise return false.

# Testcase1	:  rebels
# Output     	:  true
# Explanation 	:  Given sring rebels divided into two parts, reb and els. In both parts vowels count is same that is 1(e is presented in both the parts) so it returns true.

def check_vowels(s):
    if len(s)% 2!=0:
        return False
    # dividing of strings into two
    m=len(s)//2
    p1=s[:m]
    p2=s[m:]
    # defining of vowels
    vowels = "aeiouAEIOU"
    # counting of vowels
    v1=0    
    v2=0
    
    for i in p1:
        if i in vowels:
            v1+=1
    
    for j in p2:
        if j in vowels:
            v2+=1
    
    return v1==v2

print(check_vowels("rebels"))    
    
    
    