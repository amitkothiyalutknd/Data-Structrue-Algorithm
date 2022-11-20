from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def insert(self, value):
        self.container.appendleft(value)
        print(f"The value {value} in Queue is inserted successfully.")

    def delete(self):
        if len(self.container) == 0:
            print("The Queue Is Empty.")
        else: 
            # return self.container.pop()
            print(f"The Value {self.container.pop()} poped out from Queue successfully.")

    def front(self):
        if len(self.container) == 0:
            print("The Queue Is Empty.")
        else:
            # return len(self.container)
            print("The Front Element Of Queue is:", self.container[-1])

    def rear(self):
        if len(self.container) == 0:
            print("The Queue Is Empty.")
        else:
            # return self.container[1]
            print("The Rear Element Of Queue is:", self.container[0])

    def display(self):
                if len(self.container) == 0:
                    print("The Queue Is Empty.")
                else:
                    for data in self.container:
                        print(data, end="  ")
                print("\nThe Size of Queue is:", len(self.container))

if __name__ == '__main__':
    q = Queue()
    while True:
        chce = int(input('''
            1 Insert Element
            2 Delete Element
            3 Front Element
            4 Rear Element
            5 Display Queue
            6 Exit Oeration
            '''))

        if chce == 1:
            value = eval(input("Enter The Value To Be Insert In Queue.\n"))
            q.insert(value)
        elif chce == 2:
            q.delete()
        elif chce == 3:
            q.front()
        elif chce == 4:
            q.rear()
        elif chce == 5:
            q.display()
        elif chce == 6:
            break
        else:
            print("Invalid Choice.")