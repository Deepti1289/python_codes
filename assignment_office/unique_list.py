#Ques: Input will be a list and remove all duplicate elemnts and return new list?
#!/usr/bin/python


def main():
    list1 = [2,3,4,51,1,3,1,2,6,7,8,9]
    s = set(list1)
    print(list(s))

if __name__ == "__main__":
    main()
