#Ques: Input will be two list and create another list that will have common elements of list1 and list2?
#!/usr/bin/python


def main():
    list1 = [1,2,3,4,5,6,6]
    list2 = [4,5,6,7,78,8,9]
    s1 = set(list1)
    s2 = set(list2)
    s = s1.intersection(s2)
    list3 = list(s)
    print(list3)
    
if __name__ == "__main__":
     main()
