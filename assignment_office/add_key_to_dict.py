#Ques: Create a dictionary and check if key is present then change its value with a new value, and if key not present then add that key with va#lue None?
#!/usr/bin/python
def add_key(k):
    my_dict = {"a":2, "b":5, "d":6}
    if k in my_dict.keys():
        my_dict[k] += 1
    else:
        my_dict[k] = None
    print(my_dict)

def main():
    k = raw_input("Enter key: ")
    add_key(k)

if __name__ == "__main__":
    main()
