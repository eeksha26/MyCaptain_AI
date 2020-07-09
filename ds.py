#assigning elements to different list
list1=['1','2','3','4','5']
list2=['a','b','c','d','e']
print("Original Lists:")
print(list1)
print(list2)
x=(int)(input("Enter 1 to add numbers to list1 or 2 to add letters to list2:"))
if x==1:
    a=input("Enter a number:")
    list1.append(a)
elif x==2:
    a=input("Enter a letter:")
    list2.append(a)
print("Updated Lists:")
print(list1)
print(list2)
#accessing elements from a tuple
tup=('R','A','I','N','B','O','W')
choice=(int)(input("Enter 1 to print the first and last letter of the word rainbow or 2 to print custom number of letters if the word rainbow:"))
if choice==1:
    print("The first alphabet in RAINBOW is",tup[0])
    print("The last alphabet in RAINBOW is",tup[6])
elif choice==2:
    print("How many letters of the word rainbow do you want to print?")
    ch=(int)(input("Enter the number(upto 7 only):"))
    for x in range(0,ch):
        print(tup[x])
else:
    print("Invalid Input!")
#deleting different dictionary elements
dict={'A':65,'B':66,'C':67,'D':68,'E':69}
print("Original Dictionary:",dict)
a=input("Enter the key to delete:")
dict.pop(a)
print("Updated dictionary:",dict)
