#!/usr/bin/python

queue = ["deepti", "raghav", "new", "puja"]
def append_item(i):
    global queue
    queue.append(i)
    return queue

def delete_queue():
    global queue
    queue.pop(0)
    return queue

def display():
    print(queue)

def main():
    while True:
        print("\nMenu\n(D)isplay\n(A)ppend\n(R)emove\n(Q)uit")
        choice = raw_input("Enter your choice: ")
        #stack = ["deepti", "raghav", "new", "puja"]
        if choice == "Q":
            break
        elif choice == "A":
            i = raw_input("Enter the element you want to append: ")
            queue_new = append_item(i)
            print(queue_new)
        elif choice == "R":
            print(delete_queue())
        elif choice == "D":
            display()
        else:
            print("Invalid choice , please try again")                


if __name__ == "__main__":
    main()
