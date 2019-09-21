#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbs2 Tx
# Generated: Sat Sep 21 14:24:21 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print ("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sip
import sys
import time
from gnuradio import qtgui


class dvbs2_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dvbs2 Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dvbs2 Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dvbs2_tx")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 5000000
        self.tx_gain = tx_gain = 0
        self.taps = taps = 100
        self.samp_rate = samp_rate = symbol_rate * 2
        self.rolloff = rolloff = 0.2
        self.constellation = constellation = '16APSK'
        self.code_rate_label = code_rate_label = '1/2     23/ 2322 232/32/3'
        self.code_rate = code_rate = 11
        self.center_freq = center_freq = 1280e6
        self.FEC_Frame_size = FEC_Frame_size = 'Normal'

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 89, 1, 0, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win)
        self._rolloff_options = (0.2, 0.25, 0.35, )
        self._rolloff_labels = (str(self._rolloff_options[0]), str(self._rolloff_options[1]), str(self._rolloff_options[2]), )
        self._rolloff_tool_bar = Qt.QToolBar(self)
        self._rolloff_tool_bar.addWidget(Qt.QLabel('Rolloff'+": "))
        self._rolloff_combo_box = Qt.QComboBox()
        self._rolloff_tool_bar.addWidget(self._rolloff_combo_box)
        for label in self._rolloff_labels: self._rolloff_combo_box.addItem(label)
        self._rolloff_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rolloff_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rolloff_options.index(i)))
        self._rolloff_callback(self.rolloff)
        self._rolloff_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rolloff(self._rolloff_options[i]))
        self.top_grid_layout.addWidget(self._rolloff_tool_bar)
        self.uhd_usrp_sink = uhd.usrp_sink(
        	",".join(('', '')),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink.set_gain(tx_gain, 0)
        self.qtgui_freq_sink = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink.set_update_time(0.10)
        self.qtgui_freq_sink.set_y_axis(-140, 10)
        self.qtgui_freq_sink.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink.enable_autoscale(False)
        self.qtgui_freq_sink.enable_grid(True)
        self.qtgui_freq_sink.set_fft_average(0.2)
        self.qtgui_freq_sink.enable_axis_labels(True)
        self.qtgui_freq_sink.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink.set_line_label(i, labels[i])
            self.qtgui_freq_sink.set_line_width(i, widths[i])
            self.qtgui_freq_sink.set_line_color(i, colors[i])
            self.qtgui_freq_sink.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_win = sip.wrapinstance(self.qtgui_freq_sink.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_win)
        self.file_source = blocks.file_source(gr.sizeof_char*1, '/home/anisan/Downloads/adv16apsk910.ts', True)
        self.file_source.set_begin_tag(pmt.PMT_NIL)
        self.fft_filter = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(1.0, samp_rate, samp_rate/2, rolloff, taps)), 1)
        self.fft_filter.declare_sample_delay(0)
        self.dtv_physical_framer = dtv.dvbs2_physical_cc(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK, dtv.PILOTS_ON, 0)
        self.dtv_modulator = dtv.dvbs2_modulator_bc(dtv.FECFRAME_NORMAL,
        dtv.C9_10, dtv.MOD_16APSK, dtv.INTERPOLATION_OFF)
        self.dtv_ldpc_encoder = dtv.dvb_ldpc_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_OTHER)
        self.dtv_interleaver = dtv.dvbs2_interleaver_bb(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK)
        self.dtv_bch_encoder = dtv.dvb_bch_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10)
        self.dtv_bbscrambler = dtv.dvb_bbscrambler_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10)
        self.dtv_bbheader = dtv.dvb_bbheader_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.RO_0_20, dtv.INPUTMODE_NORMAL, dtv.INBAND_OFF, 168, 4000000)
        self._constellation_options = ('QPSK', '8PSK', '16APSK', '32APSK', )
        self._constellation_labels = (str(self._constellation_options[0]), str(self._constellation_options[1]), str(self._constellation_options[2]), str(self._constellation_options[3]), )
        self._constellation_tool_bar = Qt.QToolBar(self)
        self._constellation_tool_bar.addWidget(Qt.QLabel('Constellation'+": "))
        self._constellation_combo_box = Qt.QComboBox()
        self._constellation_tool_bar.addWidget(self._constellation_combo_box)
        for label in self._constellation_labels: self._constellation_combo_box.addItem(label)
        self._constellation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._constellation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._constellation_options.index(i)))
        self._constellation_callback(self.constellation)
        self._constellation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_constellation(self._constellation_options[i]))
        self.top_grid_layout.addWidget(self._constellation_tool_bar)
        self._code_rate_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._code_rate_label_formatter = None
        else:
          self._code_rate_label_formatter = lambda x: str(x)

        self._code_rate_label_tool_bar.addWidget(Qt.QLabel('Code Rate'+": "))
        self._code_rate_label_label = Qt.QLabel(str(self._code_rate_label_formatter(self.code_rate_label)))
        self._code_rate_label_tool_bar.addWidget(self._code_rate_label_label)
        self.top_grid_layout.addWidget(self._code_rate_label_tool_bar)
        self._code_rate_range = Range(1, 11, 1, 11, 200)
        self._code_rate_win = RangeWidget(self._code_rate_range, self.set_code_rate, 'Code Rate', "slider", int)
        self.top_grid_layout.addWidget(self._code_rate_win)
        self._FEC_Frame_size_options = ('Normal', 'Medium', 'Short', )
        self._FEC_Frame_size_labels = (str(self._FEC_Frame_size_options[0]), str(self._FEC_Frame_size_options[1]), str(self._FEC_Frame_size_options[2]), )
        self._FEC_Frame_size_group_box = Qt.QGroupBox('FEC Frame Size')
        self._FEC_Frame_size_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._FEC_Frame_size_button_group = variable_chooser_button_group()
        self._FEC_Frame_size_group_box.setLayout(self._FEC_Frame_size_box)
        for i, label in enumerate(self._FEC_Frame_size_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._FEC_Frame_size_box.addWidget(radio_button)
        	self._FEC_Frame_size_button_group.addButton(radio_button, i)
        self._FEC_Frame_size_callback = lambda i: Qt.QMetaObject.invokeMethod(self._FEC_Frame_size_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._FEC_Frame_size_options.index(i)))
        self._FEC_Frame_size_callback(self.FEC_Frame_size)
        self._FEC_Frame_size_button_group.buttonClicked[int].connect(
        	lambda i: self.set_FEC_Frame_size(self._FEC_Frame_size_options[i]))
        self.top_grid_layout.addWidget(self._FEC_Frame_size_group_box)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.dtv_bbheader, 0), (self.dtv_bbscrambler, 0))
        self.connect((self.dtv_bbscrambler, 0), (self.dtv_bch_encoder, 0))
        self.connect((self.dtv_bch_encoder, 0), (self.dtv_ldpc_encoder, 0))
        self.connect((self.dtv_interleaver, 0), (self.dtv_modulator, 0))
        self.connect((self.dtv_ldpc_encoder, 0), (self.dtv_interleaver, 0))
        self.connect((self.dtv_modulator, 0), (self.dtv_physical_framer, 0))
        self.connect((self.dtv_physical_framer, 0), (self.fft_filter, 0))
        self.connect((self.fft_filter, 0), (self.qtgui_freq_sink, 0))
        self.connect((self.fft_filter, 0), (self.uhd_usrp_sink, 0))
        self.connect((self.file_source, 0), (self.dtv_bbheader, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dvbs2_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_samp_rate(self.symbol_rate * 2)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink.set_gain(self.tx_gain, 0)


    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink.set_frequency_range(self.center_freq, self.samp_rate)
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self._rolloff_callback(self.rolloff)
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation
        self._constellation_callback(self.constellation)

    def get_code_rate_label(self):
        return self.code_rate_label

    def set_code_rate_label(self, code_rate_label):
        self.code_rate_label = code_rate_label
        Qt.QMetaObject.invokeMethod(self._code_rate_label_label, "setText", Qt.Q_ARG("QString", self.code_rate_label))

    def get_code_rate(self):
        return self.code_rate

    def set_code_rate(self, code_rate):
        self.code_rate = code_rate

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_sink.set_center_freq(self.center_freq, 0)
        self.qtgui_freq_sink.set_frequency_range(self.center_freq, self.samp_rate)

    def get_FEC_Frame_size(self):
        return self.FEC_Frame_size

    def set_FEC_Frame_size(self, FEC_Frame_size):
        self.FEC_Frame_size = FEC_Frame_size
        self._FEC_Frame_size_callback(self.FEC_Frame_size)


def main(top_block_cls=dvbs2_tx, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()