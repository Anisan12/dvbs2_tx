# Install script for directory: /home/anisan/dvbs2_tx/include/dvbs2

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/dvbs2" TYPE FILE FILES
    "/home/anisan/dvbs2_tx/include/dvbs2/api.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/bbheader_bb.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/bbscrambler_bb.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/bch_bb.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/ldpc_bb.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/modulator_bc.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/physical_cc.h"
    "/home/anisan/dvbs2_tx/include/dvbs2/interleaver_bb.h"
    )
endif()

