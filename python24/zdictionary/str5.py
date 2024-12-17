# Swap first 2 chars of 2 strings.

a,b = map(str,input().split())
new_a=b[:2]+a[2:]
new_b=a[:2]+b[2:]
print(new_a,new_b)
