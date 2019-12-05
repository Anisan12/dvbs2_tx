# Install script for directory: /home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_bbheader_bb.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_mode_adapt_bb.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_bbscrambler_bb.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_bch_bb.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_ldpc_bb.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_modulator_bc.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_physical_cc.xml"
    "/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/grc/dvbs2_interleaver_bb.xml"
    )
endif()

