class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insertAtBeginning(self, value):
        newNode = Node(value)
        newNode.next = self.head 
        self.head = newNode
        return None
                
    def insertAtEnd(self, value):
        current = self.head
        node = Node(value)
        if current is None:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node
        return self.head

    def getNode(self, value):
        newNode = Node(value)
        return newNode

    def insertViaIndex(self, position, value):
        index, length, newNode, temp = 1, self.listSize(), Node(value), self.head
        if position < 1 or position > (length + 1):
            print("The Given Position Is Out Of Linked List Index's Range.")
            return None
        elif position == (length + 1):
            self.insertAtEnd(value)
            print(f"{value} Value Added Successfully At The position {position} of Singly Linked List.")
            return None
        else:
            while temp:
                if index + 1 == position:
                    newNode = self.getNode(value)
                    newNode.next = temp.next
                    temp.next = newNode
                    break
                temp = temp.next
                index +=1
            print(f"{value} Value Added Successfully At The position {position} of Singly Linked List.")
            return None

    # def insertInBulk(self, datalist):
    #     current = self.head
    #     node = Node(datalist)
    #     if current is None:
    #         self.head = node
    #     else:
    #         while current.next:
    #             current = current.next
    #         current.next = node
    #     return self.head

    def deleteDuplicates(self):
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing Any Duplicates To Remove.")
            return None
        global prev
        current, collection, flag = self.head, set(), 0
        while current:
            if current.value in collection:
                flag = 1
                prev.next = current.next
            else:
                collection.add(current.value)
                prev = current
            current = prev.next
        if flag == 1:
            print("All The Duplicates Values From The Singly List Are Deleted Successfully.")
        else:
            print("No Any Duplicates Values Present In the Singly List.")
        return self.head
        
    def deleteAtBeginning(self):
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing To Remove.")
            return None
        self.head = self.head.next
        print("First Node Of Singly Linked List Removed Successfully.")

    def deleteAtEnd(self):
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing To Remove.")
            return None
        temp = self.head
        global prev
        while temp.next != None:
          prev = temp
          temp = temp.next
        prev.next = None
        temp = None
        print("Last Node Of Singly Linked List Removed Successfully.")

    def deleteViaIndex(self, position):
        size = self.listSize()
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing To Remove.")
            return None
        if position < 1 or position > size:
            print("Position Is Out Of Singly Linked List Index's Range.")
            return None
        if position == 1:
            self.deleteAtBeginning()
            return None
        if position ==  size:
            self.deleteAtEnd()
            return  None
        index = 1
        current = self.head
        global prev
        while current.next and index < position:
            prev = current
            current = current.next
            index += 1
        prev.next = current.next
        print(f"Value or Node At {position} Position Is Deleted From Singly Linked List Successfully.")
        return None

    def deleteViaValue(self, number):
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing To Remove.")
            return None
        if number == self.head.value:
            self.head = self.head.next
            print(f"Node {number} Via Value Is Deleted Successfully.")
            return None
        current = self.head
        while current.next != None:
            if number == current.next.value:
                current.next = current.next.next
                print(f"Node {number} Via Value In Singly Linked List Is Deleted Successfully.")
                return None
            current = current.next
        print("Node Isn't Present In The Singly Linked List For Deletion.")
        return None

    def deleteSinglyLinkedList(self):
        if self.head is None:
            print("Singly Linked List Is Already Empty. Nothing To Be Deletion.")
            return None
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
        print("All Nodes Of Singly Linked List Are Deleted Successfully.") 

    def searchValue(self, number):
        temp = self.head
        if temp != None:
            flag, index = 0, 0
            while temp != None:
                index += 1
                if temp.value == number:
                    flag = 1
                    break
                temp = temp.next
            if flag == 1:
                print(f"'{number}' Number Is Exist on Position {index} In The Singly Linked List.")
            else:
                print(f"'{number}' Number Isn't Exist In The Singly Linked List.")
        else:
            print("Singly Linked List Is Empty. Nothing To Be Search.")

    def findMinMax(self):
        if self.head is None:
            print("Singly Linked List Is Empty.")
            return None
        temp = self.head
        min, max = temp.value, temp.value
        while temp != None:
            if min >  temp.value:
                min = temp.value
            if max < temp.value:
                max = temp.value
            temp = temp.next
        print(f"The Smallest & Largest Value Of Singly Linked List are {min} & {max} respectively.")

    def listSize(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp: 
            count += 1
            temp = temp.next
        return count

    def display(self):
        if self.head is None:
            print("Singly Linked List Is Empty. Nothing To Display.")
            return None
        temp = self.head
        while temp:
            print(f" --> {temp.value}", end = "")
            temp = temp.next

if __name__ == "__main__":
    singleLinkList = SingleLinkList()
    while True:
        try:
            choice = int(input('''
            1> Insertion At Beginning                                       6> Deletion At Beginning
            2> Insertion At End                                             7> Deletion At End
            3> Insertion Via Index                                          8> Deletion Via Index
            4> Insertion Values In Bulk At Beginning                        9> Deletion Via Value
            5> Insertion Values In Bulk At End                              10> Deletion Of Complete Singly Linked List
            11> Remove Duplicate Values From The Linked List                12> Search The Value In Linked List                 
            13> Get Linked List Length                                      14> Display Linked List
            15> Search The Smallest & Largest                               16> Exit Operation
                Values From The Singly Linked List
            ---------------------:Choose Any One Operation From Above List To Perfrom:------------------
                    '''))
            if choice == 1:
                value = eval(input("Enter The Number To Be Insert At The Beginning Of Linked List.:\t"))
                singleLinkList.insertAtBeginning(value)
                print("Value At The Beginning of Singly Linked List Added Successfully.")
            elif choice == 2:
                value = eval(input("Enter The Number To Be Insert At The End Of Linked List.:\t"))
                singleLinkList.insertAtEnd(value)
                print("Value At The End of Singly Linked List Added Successfully.")
            elif choice == 3:
                try:
                    index, value = (map(int, input("Enter The Index & It's Value To Be Insert In LinkedList. Seperate Inputs from Single Space.:\t").split(' ')))
                    singleLinkList.insertViaIndex(index, value)
                except Exception as error:
                    print(f"{error}. Kindly! Insert Inputs Carefully.")
            elif choice == 4:
                try:
                    listValues = list(map(int, input("Enter Multiple Elements To Be Insert In Singly Linked List. Seperate Inputs from Single Space.:\t").split(' ')))
                    # listValues = (map(int, input("Enter Multiple Elements To Be Insert In Singly Linked List. Seperate Inputs from Single Space.:\t").split(' ')))
                    # head = None
                    for value in reversed(listValues):
                        # head = singleLinkList.insertInBulk(listValues)
                        singleLinkList.insertAtBeginning(value)
                    print(f"All The {len(listValues)} Values Added Successfully In The Singly Linked List.")
                except Exception as error:
                    print(f"{error}. Kindly! Insert Inputs Carefully.")
            elif choice == 5:
                try:
                    listValues = list(map(int, input("Enter Multiple Elements To Be Insert In Singly Linked List. Seperate Inputs from Single Space.:\t").split(' ')))
                    # listValues = (map(int, input("Enter Multiple Elements To Be Insert In Singly Linked List. Seperate Inputs from Single Space.:\t").split(' ')))
                    # head = None
                    for value in (listValues):
                        # head = singleLinkList.insertInBulk(listValues)
                        singleLinkList.insertAtEnd(value)
                    print(f"All The {len(listValues)} Values Added Successfully In The Singly Linked List.")
                except Exception as error:
                        print(f"{error}. Kindly! Insert Inputs Carefully.")    
            elif choice == 6:
                singleLinkList.deleteAtBeginning()
            elif choice == 7:
                singleLinkList.deleteAtEnd()
            elif choice == 8:
                index = eval(input("Enter The Position Of Node To Be Deletion:\t"))
                singleLinkList.deleteViaIndex(index)
            elif choice == 9:
                value = eval(input("Enter The Value Of Node To Be Deletion:\t")) 
                singleLinkList.deleteViaValue(value)
            elif choice == 10:
                singleLinkList.deleteSinglyLinkedList()
            elif choice == 11:
                singleLinkList.deleteDuplicates()
            elif choice == 12:
                number = eval(input("Enter The Number To Be Searh In The Linked List.:\t"))
                singleLinkList.searchValue(number)
            elif choice == 13:
                print("The Size of Singly Linked List Is:", singleLinkList.listSize())
            elif choice == 14:
                singleLinkList.display()
            elif choice == 15:
                singleLinkList.findMinMax()
            elif choice == 16:
                break
            else:
                print("Kindly! Choose Correct Number From The Mentioned Operation List.")
        except Exception as error:
            print(f"{error}. Kindly! Choose Correct Number From The Mentioned Operation List.")

        