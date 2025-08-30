table = [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]];

class DmtxCreator():
    """docstring for DmtxCreator."""

    def __init__(self):
        self.height = 5;
        self.width = 5;

    def setText(self, text:str):
        self.text = text;

    def encoding(self, arg)->bool:
        return true;

    def isCreateImage(self, arg)->bool:
        return true;

    def getPixelImage(self, x:int, y:int)->bool:
        return table[y][x];

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    