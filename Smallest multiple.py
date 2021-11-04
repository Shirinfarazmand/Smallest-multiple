#Works but it's slow
number = 1
def smallestmultiple(number):
    for i in range (1,21):
        if number % i != 0 :
            return False

    
    return True

def is_prim(number):
    prime = True
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            prime = False
            break
    return prime

while True:
    if smallestmultiple(number):
        break
    elif is_prim(number):
        pass

    elif number <1000000:
        pass
    
    number +=1

print(number)
