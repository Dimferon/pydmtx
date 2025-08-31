import colorsys;
import os;
from PIL import Image, ImageDraw;
import ctypes
path = os.path.realpath("bin/libdmtxwrapper/libdmtx.so.0");
ctypes.CDLL(path);

import pydmtx;

class PyDmtxCreator():
    """docstring for DmCreator."""

    def __init__(self, rawString:str, sizeImage:tuple[int,int]| None, replaceSymbolByFnc:str="", foregroundColor: str | tuple[float,...] | None = "black", backgroundColor: str | tuple[float,...] | None = "white"):
        self.backgroundColor=backgroundColor;
        self.foregroundColor=foregroundColor;

        self.encoderWrapper=pydmtx.DmtxEncoderWrapper();#TODO: в sip
        self.encoderWrapper.replaceSymbolByFnc1(replaceSymbolByFnc);
        
        self.rawString = rawString;
        self.sizeImage=sizeImage;
        self.encodeImage=Image.new(size=self.sizeImage, mode="RGB", color=self.backgroundColor);

    # def __del__(self):
    #     super.__del__();
    
    def toImage(self, sizeImage=None)->Image:
        dmtx = self.encoderWrapper;
        width = dmtx.getWidth();
        height = dmtx.getHeight();
    
        if self.sizeImage is None or self.sizeImage==[0, 0]:
            self.sizeImage = [height*4, width*4];
        
        self.encodeImage=Image.new(size=self.sizeImage, mode="RGB", color=self.backgroundColor);
        testEncoding = self._encodingString();
        self._renderEncode();
        return self.encodeImage;

    def SaveImage(self, name, path="./", format:str="BMP"):
        normPath = os.path.normpath(path);
        if not os.path.isdir(normPath):
            fullPath = os.path.realpath(normPath);
            os.makedirs(fullPath);
            assert os.path.isdir(fullPath), "Error! Not find save dirs!";
        if not str.__contains__(name, format):
            name = f"{name}.{format}";
        imageFileName = f"{normPath}/{name}";
        self.encodeImage = self.toImage();
        text = self.encoderWrapper.getText();
        print(text);
        if self._renderEncode():
            self.encodeImage.save(imageFileName, format=format);
        else: print("Не получилось создать DataMatrix");
    
    def _encodingString(self)->bool:
        dmtx = self.encoderWrapper;
        dmtx.setText(self.rawString);
        return dmtx.encoding();

    def _renderEncode(self, startCoord:tuple[int,int]=[0,0])->bool:
        """
        Рисуем картинку по данным (dmtxEncode.image) полученным при декодировании
        """
        # assert self.encodeImage is None, "Error! Not find image!";
        
        #TODO: DmtxImage
        draw = ImageDraw.Draw(self.encodeImage);

        dmtx = self.encoderWrapper;
        if dmtx is None:
            return False;
        width = dmtx.getWidth();
        height = dmtx.getHeight();

        OFFSET_X = startCoord[0];
        OFFSET_Y = startCoord[1];
        SCALE_X = self.sizeImage[0] / width;
        SCALE_Y = self.sizeImage[1] / height;

        for y in range(0,width):
            for x in range(0, height):
                b =  dmtx.getPixelImage(x,y);
                if b == 0:
                    x1y1 = (OFFSET_X + x * SCALE_X, OFFSET_Y + y * SCALE_Y);
                    x2y2 = (x1y1[0]+SCALE_X, x1y1[1]+SCALE_Y);
                    coord = [x1y1, x2y2];
                    draw.rectangle(xy=coord, fill=self.foregroundColor);
        return True;
        

    