from pandas.io import json
from vscodedebugvisualizer import globalVisualizationFactory

class DL:    
    class Node:
        def __init__(self,e,n,p):
            self.element = e
            self.next = n
            self.prev = p

    class DLVisualizer:
        def checkType(self, t):
            """ checks if the given object `t` is an instance of Person """
            return isinstance(t, DL)

        def visualize(self, data):
            formatted = {
                "kind": {"graph": True},
                "nodes": [],
                "edges": []
            }
            curNode = data._gHead
            formatted["nodes"].append({"id": "0", "label": "_gHead"})
            for i in range(1, len(data)+1):
                curNode = curNode.next
                formatted["edges"].append({"from": formatted["nodes"][-1]["id"], "to": str(i)})
                formatted["nodes"].append({"id": str(i), "label": str(curNode.element)})
            formatted["edges"].append({"from": formatted["nodes"][-1]["id"], "to": "-1"})
            formatted["nodes"].append({"id": "-1", "label": "_gTail"})
            return json.dumps(formatted)


    def __init__(self):
        self._size = 0
        self._gHead = self.Node(None, None, None)
        self._gTail = self.Node(None, None, self._gHead)
        self._gHead.next = self._gTail

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def add_first(self, e):
        if self.is_empty():
            new = self.Node(e, self._gTail, self._gHead)
            self._gHead.next = new
            self._gTail.prev = new
        else:
            new = self.Node(e, self._gHead.next, self._gHead)
            self._gHead.next.prev = new
            self._gHead.next = new
        self._size += 1

    def add_last(self, e):
        if self.is_empty():
            new = self.Node(e, self._gTail, self._gHead)
            self._gHead.next = new
            self._gTail.prev = new
        else:
            new = self.Node(e, self._gTail, self._gTail.prev)
            self._gTail.prev.next = new
            self._gTail.prev = new
        self._size += 1

    def add_before(self, find, elem):
        curNode = self._gHead
        while True:
            curNode = curNode.next
            if curNode == self._gTail:
                raise Exception(find, "not found")
            if curNode.element == find:
                break

        new = self.Node(elem, curNode, curNode.prev)
        curNode.prev.next = new
        curNode.prev = new
        self._size += 1

    def add_after(self, find, elem):
        curNode = self._gHead
        while True:
            curNode = curNode.next
            if curNode == self._gTail:
                raise Exception(find, "not found")
            if curNode.element == find:
                break

        new = self.Node(elem, curNode.next, curNode)
        curNode.next.prev = new
        curNode.next = new
        self._size += 1

    def __str__(self):
        curNode = self._gHead
        s = ""
        for _ in range(len(self) - 1):
            s += str(curNode.next.element)
            s += " -> "
            curNode = curNode.next
        s += str(self._gTail.prev.element)
        return s

globalVisualizationFactory.addVisualizer(DL.DLVisualizer())
dl = DL()
dl.add_first(1)
dl.add_last(2)
dl.add_before(2, 3)
pass