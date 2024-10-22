def generate_pascal_triangle(n):
    #write your code here
    ans = [[1],[1,1]]
    for i in range(3,n+1):
        let = [1,]
        work = ans[-1]
        for j in range(len(work) - 1):
            s = work[j]+ work[j + 1]
            let.append(s)
            
        let.append(1)
        ans.append(let)
        
    print(ans)

if __name__ == "__main__":
    n = 5
    generate_pascal_triangle(n)
