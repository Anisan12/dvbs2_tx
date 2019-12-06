#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/build/lib:$PATH
export LD_LIBRARY_PATH=/home/louis-normand/Documents/dvb-s2/pfe/dvbs2_tx/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-dvbs2 
