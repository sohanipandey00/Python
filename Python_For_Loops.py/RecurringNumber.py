l = []
l2 =[]
count=0
items = int(input("Enter the items you want to add"))
for item in range(items):
    item = input("Enter the item")
    l.append(item)
for x in l:
    if l.count(x) > 1:
        l2.append(x)

print("The recurring no. found in the list are: ", l2)
    
