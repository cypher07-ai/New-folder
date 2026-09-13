# thisset = {"apple", "banana", "cherry"}
# thisset.update(["orange", "mango", "grapes"])
# print(thisset)
# print(len(thisset))
# thisset.remove("banana")
# print(thisset)
# # thisset.clear()
# # print(thisset)
# # del thisset
# # print(thisset)
# x = thisset.pop()
# print(x)
# print(thisset)
# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_items = set(my_list)
# print(unique_items)
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A|B)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print(set1.intersection(set2))
