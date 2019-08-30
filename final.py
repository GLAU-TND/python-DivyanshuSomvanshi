n = int(input())
res = list(map(int,input().split(' ')))

list=[]
for i in res:
    list.append(res.count(i))
    print(max(list))