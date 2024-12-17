#DATE : 22-10-2024
#Program to merge 2 dictionaries
dict1={"apple":10,"banana":20,"cherry":30,"kiwi":40}
dict2={"mango":50,"pineapple":60,"grapes":70}
print(dict1)
print(dict2)
dict1.update(dict2)
print(dict1)
print(dict1|dict2)
