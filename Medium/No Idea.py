
n,m = map(int,input().split())
master_arr = list(map(int,input().split()))
set_a=set(map(int,input().split()))
set_b=set(map(int,input().split()))

# count=0
# for i in master_arr:
#     if i in set_a:
#         count +=1
#     elif i in set_b:
#         count -=1
# print(count)

print(sum((i in set_a)-(i in set_b) for i in master_arr))