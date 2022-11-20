from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
        print(f"The value {value} on stack is inserted successfully.")

    def pop(self):
        if len(self.container) == 0:
            print("The Stack Is Empty.")
        else: 
            # return self.container.pop()
            print(f"The Value {self.container.pop()} poped out from stack successfully.")

    def peek(self):
        if len(self.container) == 0:
            print("The Stack Is Empty.")
        else:
            # return len(self.container)
            print("The Top Element Of Stack is:", self.container[-1])

    def first(self):
        if len(self.container) == 0:
            print("The Stack Is Empty.")
        else:
            # return self.container[1]
            print("The First Element Of Stack is:", self.container[0])

    def display(self):
        if len(self.container) == 0:
            print("The Stack Is Empty.")
        else:
            for data in reversed(self.container):
                print(data)
        print("\nThe Size of Stack is:", len(self.container))

if __name__ == '__main__':
    s = Stack()
    while True:
        chce = int(input('''
            1 Push Element
            2 Pop Element
            3 Top(Peek) Element
            4 First Element
            5 Display Stack
            6 Exit Oeration
            '''))

        if chce == 1:
            value = eval(input("Enter The Value To Be Insert In Stack.\n"))
            s.push(value)
        elif chce == 2:
            s.pop()
        elif chce == 3:
            s.peek()
        elif chce == 4:
            s.first()
        elif chce == 5:
            s.display()
        elif chce == 6:
            break
        else:
            print("Invalid Choice")