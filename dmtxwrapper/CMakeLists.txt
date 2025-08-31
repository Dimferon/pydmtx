cmake_minimum_required(VERSION 3.5)
project(dmtxwrapper VERSION 0.0.1 LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(DEFAULT_SHARED_LIBS ON)
set(DEFAULT_STATIC_LIBS OFF)


set(DMTX_INCLUDE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}/../3rdparty/libdmtx")

set(DMTX_LIB_DIR ${CMAKE_BINARY_DIR}/../libdmtx)
set(DMTX_LIB_PATTERN "${DMTX_LIB_DIR}/*dmtx*.*")

link_directories(${DMTX_LIB_DIR})

file(GLOB DMTX_LIBS ${DMTX_LIB_PATTERN})

message(STATUS "Copy libs and header")
file(COPY ${DMTX_INCLUDE_DIRS}/dmtx.h DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY ${DMTX_LIBS} DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

include_directories(${DMTX_INCLUDE_DIRS})

set(DEFAULT_SHARED_LIBS "ON")
if(DEFINED BUILD_SHARED_LIBS AND NOT BUILD_SHARED_LIBS STREQUAL "")
    set(DEFAULT_SHARED_LIBS "${BUILD_SHARED_LIBS}")
endif()
option(DMTX_CREATOR_SHARED "Build DMTX as shared library" "${DEFAULT_SHARED_LIBS}")

file(GLOB WRAPER_SOURCE "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
file(GLOB WRAPER_HEADER "${CMAKE_CURRENT_SOURCE_DIR}/src/*.h")

if(DMTX_CREATOR_SHARED)
    set(PNAME ${PROJECT_NAME}_shared)
    add_library(${PNAME} SHARED ${WRAPER_SOURCE})
    target_include_directories(${PNAME} PRIVATE ${DMTX_INCLUDE_DIRS})
    if (MSVC)
        set_target_properties(${PNAME} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
    else()
        set_target_properties(${PNAME} PROPERTIES
        VERSION ${PROJECT_VERSION}
        SOVERSION ${PROJECT_VERSION_MAJOR}
        )
        target_link_libraries(${PNAME} PUBLIC m)
    endif()
    target_link_libraries(${PNAME} PRIVATE dmtx m)
    set_target_properties(${PNAME} PROPERTIES
        PUBLIC_HEADER ${WRAPER_HEADER}
        OUTPUT_NAME "dmtxwrapper"
    )
    
    install(TARGETS ${PNAME} LIBRARY ARCHIVE RUNTIME PUBLIC_HEADER)
endif()

set(DEFAULT_STATIC_LIBS OFF)
if(DEFINED BUILD_STATIC_LIBS AND NOT BUILD_STATIC_LIBS STREQUAL "")
  set(DEFAULT_STATIC_LIBS "${BUILD_STATIC_LIBS}")
endif()
option(DMTX_CREATOR_STATIC "Build DMTX as static library" "${DEFAULT_STATIC_LIBS}")
if(DMTX_CREATOR_STATIC)
    set(PNAME ${PROJECT_NAME}_static)
    add_library(${PNAME} SHARED ${WRAPER_SOURCE})
    target_include_directories(dmtxdecoderwrapper PRIVATE ${DMTX_INCLUDE_DIRS})

    if (MSVC)
        set_target_properties(${PNAME} PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
    else()
        target_link_libraries(${PNAME} PUBLIC m)
    endif()
    target_link_libraries(${PNAME} PRIVATE dmtx m)
    set_target_properties(${PNAME} PROPERTIES
        PUBLIC_HEADER ${WRAPER_HEADER}
        OUTPUT_NAME "dmtxwrapper"
    )
    
    install(TARGETS ${PNAME} LIBRARY ARCHIVE RUNTIME PUBLIC_HEADER)
endif()

add_compile_definitions(VERSION="${PROJECT_VERSION}")