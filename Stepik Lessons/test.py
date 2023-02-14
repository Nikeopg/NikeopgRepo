# dic = {input().lower() for i in range(int(input()))}
# print(dic, type(dic))
#
# x = set(input())
# print(x)

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}
print(wrd)