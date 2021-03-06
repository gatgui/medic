import medic
from maya import OpenMaya


class NotFreezed(medic.PyTester):
    Identity = OpenMaya.MMatrix()

    def __init__(self):
        super(NotFreezed, self).__init__()

    def Name(self):
        return "NotFreezed"

    def Description(self):
        return "Not freezed mesh(s)"

    def Match(self, node):
        return node.object().hasFn(OpenMaya.MFn.kMesh)

    def test(self, node):
        if node.dag().isInstanced():
            return None

        iden = OpenMaya.MMatrix()

        for p in node.parents():
            transform = p.dag().transformationMatrix()
            if not NotFreezed.Identity == transform:
                return medic.PyReport(node)

        return None


def Create():
    return NotFreezed()
