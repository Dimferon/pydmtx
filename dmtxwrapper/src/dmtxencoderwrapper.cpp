#include "dmtxencoderwrapper.h"
#include <assert.h>
#include <locale.h>
#include <iostream>

DmtxEncoderWrapper::DmtxEncoderWrapper()
{
}

DmtxEncoderWrapper::~DmtxEncoderWrapper()
{
    dmtxEncodeDestroy(&m_enc);
}

bool DmtxEncoderWrapper::isCreateImage()
{
    return _isCreateImage;
}

void DmtxEncoderWrapper::setText(string text)
{
    this->m_text = text;
    std::cout << this->m_text << std::endl;
    std::cout << this->m_text.size()<< std::endl;
}

string DmtxEncoderWrapper::getText()
{
    return this->m_text;
}

bool DmtxEncoderWrapper::encoding()
{
    if (m_enc)
    {
        dmtxEncodeDestroy(&m_enc);
    }
    m_enc = dmtxEncodeCreate();

    assert(m_enc != NULL);

    dmtxEncodeSetProp(m_enc, DmtxPropBytesPerPixel, 1);

    if (_symbolByFnc1.length()>0)
    {        
        dmtxEncodeSetProp(m_enc, DmtxPropFnc1, _symbolByFnc1[0]);
    }

    dmtxEncodeDataMatrix(m_enc, m_text.length(), (unsigned char *)m_text.c_str());

    _rowSizeBytes = m_enc->image->rowSizeBytes;
    _bytesPerPixel = m_enc->image->bytesPerPixel;
    std::cout << "row =" << _rowSizeBytes << "; bytes =" << _bytesPerPixel << std::endl;
    _code_width = dmtxImageGetProp(m_enc->image, DmtxPropWidth);
    _code_height = dmtxImageGetProp(m_enc->image, DmtxPropHeight);

    _isCreateImage = true;
    return true;
}

bool DmtxEncoderWrapper::getPixelImage(int x, int y)
{
    assert(x < _code_width && y < _code_height);
    int ind = y * _rowSizeBytes + x * _bytesPerPixel;
    unsigned char b = m_enc->image->pxl[ind];
    return b;
}

string DmtxEncoderWrapper::symbolByFnc1()
{
    return _symbolByFnc1;
}

void DmtxEncoderWrapper::replaceSymbolByFnc1(string symbol)
{
    _symbolByFnc1 = symbol;
}

int DmtxEncoderWrapper::getWidth()
{
    int widthImage = -1;
    if (m_enc)
    {
        widthImage = dmtxImageGetProp(m_enc->image, DmtxPropWidth);
    }
    return widthImage;
}

int DmtxEncoderWrapper::getHeight()
{
    int heightImage = -1;
    if (m_enc)
    {
        heightImage = dmtxImageGetProp(m_enc->image, DmtxPropHeight);
    }
    return heightImage;
}