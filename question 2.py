def climb_stairs(n):
  #write your code here
    if( n == 0 or n == 1) :
        print(1)
    
    
    step1 = 1
    step2 = 1
    current = 0
    for i in range(2,n + 1):
        current = step1 + step2
        step1 = step2
        step2 = current
        
    return current

if __name__ == "__main__":
    n = 2
    print(climb_stairs(n))
