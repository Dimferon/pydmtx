
all: dmtx_build dmtx_creator_build

dmtx_build:
	cmake -DCMAKE_BUILD_TYPE=Release -S 3rdparty/libdmtx -B bin/libdmtx
	make -C bin/libdmtx

dmtx_creator_build:
	cmake -DCMAKE_BUILD_TYPE=Release -S dmtxcreator -B bin/libdmtxcreator
	make -C bin/libdmtxcreator

install: dmtx_build dmtx_creator_build
	sip-install

clear:
	pip uninstall pydmtx -y