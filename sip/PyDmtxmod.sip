%Module(name=pydmtx, language="C++")
%DefaultEncoding "UTF-8"

%MappedType std::string
{
%TypeHeaderCode
#include <string>
%End

%ConvertFromTypeCode
    // Convert an std::string to a Python (Unicode) string
    PyObject* newstring;
    newstring = PyUnicode_FromStringAndSize(sipCpp->data(), sipCpp->size());
    return newstring;
%End

%ConvertToTypeCode
    // Convert a Python (Unicode) string to an std::string
    if (sipIsErr == NULL) {
        return PyUnicode_Check(sipPy);
    }
    if (PyUnicode_Check(sipPy)) {
        *sipCppPtr = new std::string(PyUnicode_AsUTF8(sipPy));
        return 1;
    }
    return 0;
%End
};

//%Include DmtxEncoderWraper.sip
//%Include DmtxDecoderWraper.sip

