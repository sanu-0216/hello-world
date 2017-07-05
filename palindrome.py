def palindrome():
    number=int(raw_input("Enter a Number"))
    sum=0
    result=number
    while(number>0):
        n=number%10
        number=number/10
        sum=sum*10+n
    if result == sum:
        print result, " is palindrome number"
    else:
        print result, " is not palindrome number"
        
        
        
if __name__=='__main__':
    palindrome()
