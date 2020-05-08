# --------------
#Code starts here

#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
        
        
#Code ends here  


# --------------
def a_scramble(str_1,str_2):
    str_1 = list(str_1.lower())
    str_2 = list(str_2.lower())
    flg=1
    for letter in str_2:
        if letter not in str_1:
            flg = 0
            break
        else:
            flg = 1
            str_1.remove(letter)
    return flg      
   

print(a_scramble("baby shower","shows"))


# --------------
#Code starts here
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def check_fib(num):
    n = 0
    a = fibonacci(n)
    while(1):
        if a < num :
            n+=1
            a = fibonacci(n)
        elif a>num:
            return False
        else :
            return True
    
    



# --------------
def compress(word):
    word = list(word.lower())
    word.append(" ")
    wl = []
    for i in range(len(word)):
        if i == len(word)-1:
            break
        else:
            if i==0:
                w_count=1
            else:
                if word[i] == word[i-1]:
                    w_count+=1
                else:
                    w_count=1
            if word[i] != word[i+1]:
                wl.append(word[i])
                wl.append(str(w_count))

    return "".join(wl)


# --------------
def k_distinct(string,k):
    return len(set(string.lower())) == k



