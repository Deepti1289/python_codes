#!/usr/bin/python

stack = ["deepti", "raghav", "new", "puja"]
def append_item(i):
    global stack
    stack.append(i)
    return stack

def delete_stack():
    global stack
    stack.pop()
    return stack

def display():
    print(stack)

def main():
    while True:
        print("\nMenu\n(D)isplay\n(A)ppend\n(R)emove\n(Q)uit")
        choice = raw_input("Enter your choice: ")
        stack = ["deepti", "raghav", "new", "puja"]
        if choice == "Q":
            break
        elif choice == "A":
            i = raw_input("Enter the element you want to append: ")
            stack_new = append_item(i)
            print(stack_new)
        elif choice == "R":
            print(delete_stack())
        elif choice == "D":
            display()
        else:
            print("Invalid choice , please try again")                


if __name__ == "__main__":
    main()
