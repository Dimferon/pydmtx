#ifndef DMTX_CREATOR_H
#define DMTX_CREATOR_H

#include "../../3rdparty/libdmtx/dmtx.h"
#include <string>

using std::string;

class DmtxCreator
{
private:
    bool _isCreateImage = false;
    int _code_width = 0,
        _code_height = 0;
    int _rowSizeBytes = 0;
    int _bytesPerPixel = 0;
    int _maxIndex = -1;
    string m_text;
    DmtxEncode *m_enc = nullptr;

public:
    DmtxCreator();
    ~DmtxCreator();

    void setText(string text);
    string getText();

    bool encoding();

    bool isCreateImage();
    bool getPixelImage(int x, int y);

    int getWidth();
    int getHeight();
};

#endif