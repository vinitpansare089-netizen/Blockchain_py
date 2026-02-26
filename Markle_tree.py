from typing import List
import hashlib

class Node:
    def __init__(self, left, right, value=str, content=None, is_copied=False) -> None:##__init__(automatically called)
        self.left:Node = left
        self.right:Node = right
        self.value = value
        self.content = content
        self.is_copied = is_copied

    def hash(val: str) -> str:
        return hashlib.sha256(val.encode()).hexdigest()
    
    def __str__(self) -> str:
        return self.value
    
    def copy(self): 
        return Node(self.left, self.right, self.value, self.content, True)
    
class MerkleTree:
    def __init__(self, values: List[str]) -> None:
        self.__buildTree(values)

    def __buildTree(self, values: List[str]) -> None:
        leaves: List[Node] = [Node(None, None, Node.hash(e), e) for e in values]

        if len(leaves) % 2 == 1: 
            leaves.append(leaves[-1].copy())
            self.root = self.__buildTree(leaves)
    
    def __buildTree(self, nodes: List[Node]) -> Node:
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1].copy())
        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value), nodes[0].content + "+" + nodes[1].content)
        
        left: Node = self.__buildTree(nodes[:half])
        right: Node = self.__buildTree(nodes[half:])

        value: str = Node.hash(left.value + right.value)
        content: str = f'{left.content} + {right.content}'

        return Node(left, right, value, content)
    
    def printTree(self) -> None:
        self.__printTreeRec(self.root)

    def __printTreeRec(self, node: Node, level=0) -> None:
        if node != None:
            if node.left != None:
                print("Left:" +str(node.left))
                print("Right: "+str(node.right))
            else:
                print("Input")

            if node.is_copied:
                print("(padding)")
            print("value: "+str(node.value))
            print("content: "+str(node.content))
            print("")
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)

    def getrootHash(self) -> str:
        return self.root.value
    
def mixmarkletree() -> None:
    elems = ["Medicaps CFI", "A", "computer", "science", "portal", "for", "students"]

    print("Inputs: ")
    print(*elems, sep=" | ")
    print("")
    mtree = MerkleTree(elems)
    print("Root Hash: "+mtree.getrootHash()+"\n")
    mtree.printTree()


mixmarkletree()