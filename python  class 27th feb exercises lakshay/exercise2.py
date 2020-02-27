
for i in range(1,101):
    
    if i % 5 ==0 and i % 3 ==0:
        print(f' fizzbuzz')
    elif i % 3 ==0:
       print( f' fizz')
    
    elif i % 5 ==0:
       print(f' buzz')
    
    else:
         print(f'{i}')