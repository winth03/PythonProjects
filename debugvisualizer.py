from pandas.io import json
from vscodedebugvisualizer import globalVisualizationFactory
from DL_Class import DL

class DLVisualizer:
    def checkType(self, t):
        return isinstance(t, DL)

    def visualize(self, data):
        formatted = {
            "kind": {"graph": True},
            "nodes": [],
            "edges": []
        }
        curNode = data._gHead
        formatted["nodes"].append({"id": str(curNode), "label": "_gHead", "color": "orange"})
        formatted["edges"].append({"from": str(curNode), "to": str(curNode.next), "label": "next"})
        formatted["nodes"].append({"id": str(data._gTail), "label": "_gTail", "color": "orange"})
        formatted["edges"].append({"from": str(data._gTail), "to": str(data._gTail.prev), "label": "prev"})
        for _ in range(len(data)):
            curNode = curNode.next
            formatted["edges"].append({"from": str(curNode), "to": str(curNode.next), "label": "next"})
            formatted["edges"].append({"from": str(curNode), "to": str(curNode.prev), "label": "prev"})
            formatted["nodes"].append({"id": str(curNode), "label": str(curNode.element)})
        return json.dumps(formatted)

globalVisualizationFactory.addVisualizer(DLVisualizer())