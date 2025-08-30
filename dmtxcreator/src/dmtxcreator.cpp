#include "dmtxcreator.h"
#include <assert.h>
#include <locale.h>
#include <iostream>

DmtxCreator::DmtxCreator(/* args */)
{
}

DmtxCreator::~DmtxCreator()
{
    dmtxEncodeDestroy(&m_enc);
}

bool DmtxCreator::isCreateImage()
{
    return _isCreateImage;
}

void DmtxCreator::setText(string text)
{
    this->m_text = text;
    std::cout << this->m_text << std::endl;
    std::cout << this->m_text.size()<< std::endl;
}

string DmtxCreator::getText()
{
    return this->m_text;
}

bool DmtxCreator::encoding()
{
    if (m_enc)
    {
        dmtxEncodeDestroy(&m_enc);
    }
    m_enc = dmtxEncodeCreate();
    assert(m_enc != NULL);
    dmtxEncodeSetProp(m_enc, DmtxPropBytesPerPixel, 1);

    dmtxEncodeDataMatrix(m_enc, m_text.length(), (unsigned char *)m_text.c_str());

    _rowSizeBytes = m_enc->image->rowSizeBytes;
    _bytesPerPixel = m_enc->image->bytesPerPixel;
    std::cout << "row =" << _rowSizeBytes << "; bytes =" << _bytesPerPixel << std::endl;
    _code_width = dmtxImageGetProp(m_enc->image, DmtxPropWidth);
    _code_height = dmtxImageGetProp(m_enc->image, DmtxPropHeight);

    _isCreateImage = true;
    return true;
}

bool DmtxCreator::getPixelImage(int x, int y)
{
    assert(x < _code_width && y < _code_height);
    int ind = y * _rowSizeBytes + x * _bytesPerPixel;
    unsigned char b = m_enc->image->pxl[ind];
    return b;
}

int DmtxCreator::getWidth()
{
    int widthImage = -1;
    if (m_enc)
    {
        widthImage = dmtxImageGetProp(m_enc->image, DmtxPropWidth);
    }
    return widthImage;
}

int DmtxCreator::getHeight()
{
    int heightImage = -1;
    if (m_enc)
    {
        heightImage = dmtxImageGetProp(m_enc->image, DmtxPropHeight);
    }
    return heightImage;
}