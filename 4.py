list1 = input().split()
list2 = input().split()
value = input().strip()

if value in list1 and value in list2:
    print("Принадлежит")
else:
    print("Не принадлежит")