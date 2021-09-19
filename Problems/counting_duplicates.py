def counter(alist):

    dit_name={}

    for  j in alist:
        # print(j)
        count=0
        for k in alist:
            if k==j:
                count+=1
            dit_name.update({j:count})
        
    return dit_name

a=[1,3,5,6,7,1,5,1]

print(counter(a))

# Other approach

result={i:a.count(i) for i in a}

print(result)
