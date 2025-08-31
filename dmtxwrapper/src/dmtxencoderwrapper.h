#ifndef DMTX_ENCODER_WRAPPER_H
#define DMTX_ENCODER_WRAPPER_H

#include "../../3rdparty/libdmtx/dmtx.h"
#include <string>

using std::string;

class DmtxEncoderWrapper
{
private:
    bool _isCreateImage = false;
    string _symbolByFnc1;
    int _code_width = 0,
        _code_height = 0;
    int _rowSizeBytes = 0;
    int _bytesPerPixel = 0;
    int _maxIndex = -1;
    string m_text;
    DmtxEncode *m_enc = nullptr;

public:
    DmtxEncoderWrapper();
    ~DmtxEncoderWrapper();

    void setText(string text);
    string getText();

    bool encoding();

    bool isCreateImage();
    bool getPixelImage(int x, int y);

    string symbolByFnc1();
    void replaceSymbolByFnc1(string symbole);

    int getWidth();
    int getHeight();
};

#endif