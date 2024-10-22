def compress(chars):
   #write your code here
    count = {}
    for i in chars:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    chars.clear()
    for i in count:
        chars.append(i)
        if 10 > count[i] > 1:
            chars.append(str(count[i]))
        elif count[i] >= 10:
            let = str(count[i])
            for j in let:
                chars.append(j)
    return len(chars)       

if __name__ == "__main__":
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    newSize = compress(chars)
    print("New length:", newSize)
    print(chars[:newSize])