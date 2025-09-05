class DmtxDecoderWrapper {
    %TypeHeaderCode
    #include <dmtxencoderwrapper.h>
    %End

    public:
        DmtxDecoderWrapper();

        std::string getText();

        bool decoding();

        void setImage();
        void getImage();

        int getWidth();
        int getHeight();

        std::string symbolByFnc1();
        void replaceSymbolByFnc1(std::string symbole);
};
