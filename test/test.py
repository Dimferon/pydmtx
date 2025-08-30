import ctypes
ctypes.CDLL("/home/ubuntu/pydmtx/bin/libdmtxcreator/libdmtx.so");

import pydmtx;

test = pydmtx.DmtxCreator();

test.setText("test12345");
testText = test.getText();
print(testText);

import pydmtx_creator

test = pydmtx_creator.PyDmtxCreator("tesggadsgaagsddgsagdsaaggasgdt", [100,100]);
test.SaveImage(name="test.BMP");

test = pydmtx_creator.PyDmtxCreator("testgaasdgasdgasdgasdgasdgasgadg1", [100,100]);
test.SaveImage(name="test1.BMP");

test = pydmtx_creator.PyDmtxCreator("testasdgasdgasdgasgasgdasgasgdasgd2", [100,100]);
test.SaveImage(name="test2.BMP");