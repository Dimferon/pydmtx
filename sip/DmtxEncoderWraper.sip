
class DmtxEncoderWrapper {
    %TypeHeaderCode
    #include <dmtxencoderwrapper.h>
    %End

    public:
        DmtxEncoderWrapper();

        void setText(std::string text);
        std::string getText();

        bool encoding();

        bool isCreateImage();
        bool getPixelImage(int x, int y);

        int getWidth();
        int getHeight();

        std::string symbolByFnc1();
        void replaceSymbolByFnc1(std::string symbole);
};
