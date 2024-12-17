#DATE : 22-10-2024
#Sort a dictionary by keys in ascending and descending order
#PROGRAM
d={"apple":10,"kiwi":20,"orange":40,"banana":30}
print("Original Dictionary :",d)
a_result=dict(sorted(d.items()))
print("In Ascending order :",a_result)
d_result=dict(sorted(d.items(),reverse=True))
print("In Descending order :",d_result)
