class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        l = self.parent
        while l:
            level += 1
            l = l.parent
        return level
        
    def displayTree(self):
        spaces = ' ' * self.getLevel() * 4
        prefix = spaces + "-->" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.displayTree()

def buildStructTree():
    root = TreeNode("US Government")

    judicialBranch = TreeNode("Judicial Branch")
    
    supremeCourt = TreeNode("Supreme Court")

    legislativeBranch = TreeNode("Legislative Branch")
    
    congress = TreeNode("Congress")

    agencies = TreeNode("Agencies")

    investigationDept = TreeNode("Investigation Department")

    fbi = TreeNode("Federal Bureau Investigation")

    executiveBranch = TreeNode("Executive Branch")

    cabinet = TreeNode("Cabinet")

    root.addChild(judicialBranch)

    judicialBranch.addChild(supremeCourt)
    supremeCourt.addChild(TreeNode("Chief Justice"))
    supremeCourt.addChild(TreeNode("Supreme Court Justice1"))
    supremeCourt.addChild(TreeNode("Supreme Court Justice2"))
    supremeCourt.addChild(TreeNode("Supreme Court Justice3"))
    supremeCourt.addChild(TreeNode("Supreme Court Justice4"))

    root.addChild(legislativeBranch)
    
    legislativeBranch.addChild(congress)
    congress.addChild(TreeNode("Senate"))
    congress.addChild(TreeNode("House of Representatives"))

    legislativeBranch.addChild(agencies)
    agencies.addChild(TreeNode("Archtect Of The Capital"))
    agencies.addChild(TreeNode("General Accounting Office"))
    agencies.addChild(TreeNode("Liberary Of Congress"))
    
    agencies.addChild(investigationDept)
    investigationDept.addChild(TreeNode("Central Intelligence Agency"))
    
    investigationDept.addChild(fbi)
    fbi.addChild(TreeNode("Impossible Mission Force"))

    root.addChild(executiveBranch)
    executiveBranch.addChild(TreeNode("President"))
    executiveBranch.addChild(TreeNode("Vice President"))
    executiveBranch.addChild(TreeNode("Senator Of House"))
    
    executiveBranch.addChild(cabinet)
    cabinet.addChild(TreeNode("Secretary Of State"))
    cabinet.addChild(TreeNode("Secretary Of Defense"))
    cabinet.addChild(TreeNode("Senator Of House"))
    cabinet.addChild(TreeNode("Attorney General"))
    cabinet.addChild(TreeNode("Secretary Of Commerce"))
    cabinet.addChild(TreeNode("Secretary Of Health & Human Services"))
    cabinet.addChild(TreeNode("Secretary Of Transportation"))
    cabinet.addChild(TreeNode("Secretary Of Eductation"))

    root.displayTree()

buildStructTree()