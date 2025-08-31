
all: dmtx_build dmtx_creator_build
	sip-build
	sip-install

dmtx_build:
	cmake -DCMAKE_BUILD_TYPE=Release -S 3rdparty/libdmtx -B bin/libdmtx
	make -C bin/libdmtx

dmtx_creator_build:
	cmake -DCMAKE_BUILD_TYPE=Release -S dmtxwrapper -B bin/libdmtxwrapper
	make -C bin/libdmtxwrapper

install: dmtx_build dmtx_creator_build
	sip-install

clear:
	pip uninstall pydmtx -y
	rm -r bin
	rm -r build