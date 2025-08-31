import ctypes
import os
path = os.path.realpath("bin/libdmtxwrapper/libdmtx.so");
ctypes.CDLL(path);

import pydmtx;

test = pydmtx.DmtxEncoderWrapper();

test.setText("test12345");
testText = test.getText();
print(testText);

import pydmtx_creator
print("--------------")
test = pydmtx_creator.PyDmtxCreator("+tesggadsgaagsd+dgsagdsaaggasgdt", [100,100], replaceSymbolByFnc="+");
test.SaveImage(name="test_fnc1.BMP", path="./test/tmp");

print("--------------")
test = pydmtx_creator.PyDmtxCreator("-tesggadsgaagsd-dgsagdsaag-gasgdt", [100,100], replaceSymbolByFnc="-");
test.SaveImage(name="test_fnc1_2.BMP", path="./test/tmp");
print("--------------")
test = pydmtx_creator.PyDmtxCreator("testasdgasdgasdgasgasgdasgasgdasgd2", [100,100]);
test.SaveImage(name="test2.BMP", path="./test/tmp");