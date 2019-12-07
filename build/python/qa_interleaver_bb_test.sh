#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/anisan/dvbs2_tx/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/anisan/dvbs2_tx/build/python:$PATH
export LD_LIBRARY_PATH=/home/anisan/dvbs2_tx/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/anisan/dvbs2_tx/build/swig:$PYTHONPATH
/usr/bin/python2 /home/anisan/dvbs2_tx/python/qa_interleaver_bb.py 
