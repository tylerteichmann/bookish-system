import random

# def undup(l):
#     return list(set(l))

# l = [1,2,3,3,4,1,5,5,5]
# print(undup(l))

# def numres(nl):
#     list = [ len(nl), sum(nl), sum(nl)/len(nl) ]
#     return list

# nl = [1,2,3]
# print(numres(nl))

# xlist = [1, ['a','b',['x','y']]]
# print(xlist[1][2][1])

# randlist = []
# for i in range(20):
#     randlist.append(random.randint(1, 100))

# randlist.sort()
# print(randlist)

# li = "Mary had a little lamb."

# def how_many_a_in_li(a, li):
#     print(li.count(a))

# how_many_a_in_li('a', li)

# tlist = [(i, i**2) for i in range(1, 11)]
# print(tlist)

# lol = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7],
#     [8, 9, 10, 11]
# ]

# lot = [(v[0], v[-1]) for v in lol]
# print(lot)

# string = "Mary had a little lamb"
# string = string.replace(' ', '*')

# # list = string.split()
# # string = '*'.join(list)

# print(string)

# adict = {
#     "Joe":175,
#     "Tom":190,
#     "Dick":150,
#     "Jerry":150
# }

# new_dict = {}

# for key, value in adict.items():
#     new_dict[value] = key

# print(new_dict)

# print(len(str(2**100)))

# alist = list("This is just a proof of generality")

alist = list("qwertyuiopasdfghjkl")
dict_count = {}

for letter in alist:
    dict_count[letter] = (alist.count(letter), 4)

for key, value in dict_count:
    print(key)