str1=input("Enter a string:")
freq={}#dictionary
for c in str1:
	if c in freq:
		freq[c]=freq[c]+1
	else:
		freq[c]=1
print(freq)
