#Ques; Create another list which will have all the elemnts of list1 and list2 but not common?
#!/usr/bin/python

def main():
    list1 = [1,2,3,4,5,6,6]
    list2 = [4,5,6,7,78,8,9]
    s1 = set(list1)
    s2 = set(list2)
    s3 = s1.union(s2)
    s4 = s1.intersection(s2)
    result = s3-s4
    list3 = list(result)
    print(list3)

if __name__ == "__main__":
     main()

