numbers = [6, 7, 3, 5, 9]
products = ["awes", "awe"]
a = ["a", "b"]
addList = a + products
print(sorted(addList))
my_list = list(range(30))
print(my_list)


def smallest_number(numb):
    smallest = numb[0]
    for i in range(1, len(numb)):
        if numb[i] < smallest:
            smallest = numb[i]
    print(smallest)

def total_sum(strings):
    res=0
    for word in strings:
        if "s" in word:
            index=word.index("s")
            res+=index

    return res

print("total sum is",total_sum(["awe","saf","ss"]))




smallest_number([2, 4, 6, 1, -5])


list_ex=["awes","sew","aaa","awerfg"]
print(list_ex)
list_ex[2:3]=["aaaaa","bbbb"]
print(list_ex)

def powerball_numbers(unit_numbers):
    squared_list=[]
    for i in range(0,len(unit_numbers)):
        squared_list.append(unit_numbers[i]*unit_numbers[i])
    print(squared_list)
powerball_numbers([2,4,6,8,10])
awes=[1,2,3,4]
aw=[7,8,9]
awes.extend(aw)
print(awes)