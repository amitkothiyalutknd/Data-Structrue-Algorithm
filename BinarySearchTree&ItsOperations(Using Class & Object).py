class BinarySearchTree():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def insertInBST(self, value):
        if self.value == value:
            return print(f"The value:{value} you want to be insert in an element is already exist.")
        elif self.value > value:
            if self.left:
                self.left.insertInBST(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insertInBST(value)
            else:
                self.right = BinarySearchTree(value)

    def preOrderBST(self):
        preOrder = []
        preOrder.append(self.value)
        if self.left:
            preOrder += self.left.preOrderBST()
        if self.right:
            preOrder += self.right.preOrderBST()
        return preOrder

    def inOrderBST(self):
        inOrder = []
        if self.left:
            inOrder += self.left.inOrderBST()
        inOrder.append(self.value)
        if self.right:
            inOrder += self.right.inOrderBST()
        return inOrder

    def postOrderBST(self):
        postOrder = []
        if self.left:
            postOrder += self.left.postOrderBST()
        if self.right:
            postOrder += self.right.postOrderBST()
        postOrder.append(self.value)
        return postOrder

    def searchInBST(self, number):
        if self.value == number:
            return print(f"Number:{number} is exist in Binary Search Tree.")
        if self.value > number:
            if self.left:
                return self.left.searchInBST(number)
            else:
                return print(f"Number:{number} doesn't exist in Binary Search Tree.")
        elif self.value < number:
            if self.right:
                return self.right.searchInBST(number)
            else:
                return print(f"Number:{number} doesn't exist in Binary Search Tree.")

    def minInBST(self):
        while self.left:
            self = self.left
        return self.value

    def maxInBST(self):
        while self.right:
            self = self.right
        return self.value

    def deletionInBST(self, element):
        if self.value == element:
            if self.right and self.left: 
                [psucc, succ] = self.right.min(self)
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                succ.left = self.left
                succ.right = self.right
                return succ                
            else:
                if self.left:
                    return self.left
                else:
                    return self.right 
        else:
            if self.value > element:
                if self.left:
                    self.left = self.left.deletionInBST(element)
            else:
                if self.right:
                    self.right = self.right.deletionInBST(element)
        return self

    def min(self, parent):
        if self.left:
            return self.left.min(self)
        else:
            return [parent, self]
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

if __name__ == "__main__":
    while True:
        try:
            choice = int(input('''
            1> Insert Root Node In Binary Search Tree                           2> Insertion In Binary Search Tree
            3> Pre-Order Traversal Of BST                                       4> In-Order Traversal Of BST
            5> Post-Order Traversal Of BST                                      6> Searach An Element In Binary Search Tree
            7> Minimum Number In BST                                            8> Maximum Number In BST
            9> Deletion In Binary Search Tree(Except Root Node)                 10> Display Of Binary Search Tree
            11> Build BST from Bulk Values                                       12> Exit From The Programme
            ---------------------:Choose Any One Operation From Above List To Perfrom:------------------
                    '''))
            if choice == 1:
                root = eval(input("Enter The Root Node To Be Insert In Binary Search Tree.:\t"))
                bst = BinarySearchTree(root)
                print(f"Root:{root} Successfully Added In Binary Search Tree.")
            elif choice == 2:
                value = eval(input("Enter The Value To Be Insert In Binary Search Tree.:\t"))
                bst.insertInBST(value)
                print(f"Value:{value} Successfully Added In Binary Search Tree.")
            elif choice == 3:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("Below Values are the Pre-Order Display of Binary Search Tree.\n", bst.preOrderBST())
            elif choice == 4:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("Below Values are the In-Order Display of Binary Search Tree.\n", bst.inOrderBST())
            elif choice == 5:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("Below Values are the Post-Order Display of Binary Search Tree.\n", bst.postOrderBST())
            elif choice == 6:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    number = eval(input("Enter The Number To Be Search In Binary Search Tree.:\t"))
                    bst.searchInBST(number)
            elif choice == 7:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("The Minimum Value of Binary Search Tree Is:\t", bst.minInBST())
            elif choice == 8:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("The Maximum Value of Binary Search Tree Is:\t", bst.maxInBST())
            elif choice == 9:
                element = eval(input("Enter The Number To Be Deletion In Binary Search Tree.:\t"))
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    bst.deletionInBST(element)
                    print(f"The value:{element} to be deletion in Binary Search Tree is successfully deleted.")
            elif choice == 10:
                if 'bst' not in globals():
                    print("Binary Search Tree has not any value yet.")
                else:
                    print("The tree structure display of Binary Search Tree.\n")
                    bst.display()
            elif choice == 11:
                try:
                    listValues = list(map(int, input("Enter Multiple Elements To Be Insert In Singly Linked List. Seperate Inputs from Single Space.:\t").split(' ')))
                    for value in (listValues):
                        bst.insertInBST(value)
                    print(f"All The {len(listValues)} Values Added Successfully In The Binary Search Tree.")
                except Exception as error:
                        print(f"{error}. Kindly! Insert Inputs Carefully.")
            elif choice == 12:
                break
            else:
                print("Kindly! Choose Correct Number From The Above Mentioned Operation List.")
        except Exception as error:
            print(f"{error}. Kindly! Choose Correct Number From The Above Mentioned Operation List.")