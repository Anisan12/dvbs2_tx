#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbs2 Tx
# Generated: Thu Dec  5 16:36:34 2019
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
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import dvbs2
import sip
import sys
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

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 5000000
        self.tx_gain = tx_gain = 0
        self.taps = taps = 100
        self.samp_rate = samp_rate = symbol_rate * 2
        self.rolloff = rolloff = 0.2
        self.qtgui_variable = qtgui_variable = '"labul'
        self.pilots = pilots = 0
        self.noise_type = noise_type = "Gaussian"
        self.noise = noise = 0.1
        self.code_rate_qpsk = code_rate_qpsk = "9/10"
        self.code_rate_8psk = code_rate_8psk = "9/10"
        self.code_rate_32apsk = code_rate_32apsk = "9/10"
        self.code_rate_16apsk = code_rate_16apsk = "9/10"
        self.center_freq = center_freq = 1280e6
        self.browse_button = browse_button = 0
        self.FEC_Frame_size = FEC_Frame_size = 'Normal'

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 89, 1, 0, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._rolloff_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.constellation_tab = Qt.QTabWidget()
        self.constellation_tab_widget_0 = Qt.QWidget()
        self.constellation_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellation_tab_widget_0)
        self.constellation_tab_grid_layout_0 = Qt.QGridLayout()
        self.constellation_tab_layout_0.addLayout(self.constellation_tab_grid_layout_0)
        self.constellation_tab.addTab(self.constellation_tab_widget_0, 'QPSK')
        self.constellation_tab_widget_1 = Qt.QWidget()
        self.constellation_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellation_tab_widget_1)
        self.constellation_tab_grid_layout_1 = Qt.QGridLayout()
        self.constellation_tab_layout_1.addLayout(self.constellation_tab_grid_layout_1)
        self.constellation_tab.addTab(self.constellation_tab_widget_1, '8PSK')
        self.constellation_tab_widget_2 = Qt.QWidget()
        self.constellation_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellation_tab_widget_2)
        self.constellation_tab_grid_layout_2 = Qt.QGridLayout()
        self.constellation_tab_layout_2.addLayout(self.constellation_tab_grid_layout_2)
        self.constellation_tab.addTab(self.constellation_tab_widget_2, '16APSK')
        self.constellation_tab_widget_3 = Qt.QWidget()
        self.constellation_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellation_tab_widget_3)
        self.constellation_tab_grid_layout_3 = Qt.QGridLayout()
        self.constellation_tab_layout_3.addLayout(self.constellation_tab_grid_layout_3)
        self.constellation_tab.addTab(self.constellation_tab_widget_3, '32APSK')
        self.top_grid_layout.addWidget(self.constellation_tab, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._qtgui_variable_tool_bar = Qt.QToolBar(self)

        if None:
          self._qtgui_variable_formatter = None
        else:
          self._qtgui_variable_formatter = lambda x: str(x)

        self._qtgui_variable_tool_bar.addWidget(Qt.QLabel('label'+": "))
        self._qtgui_variable_label = Qt.QLabel(str(self._qtgui_variable_formatter(self.qtgui_variable)))
        self._qtgui_variable_tool_bar.addWidget(self._qtgui_variable_label)
        self.top_grid_layout.addWidget(self._qtgui_variable_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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

        labels = ['DVB-S2', '', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._pilots_options = (1, 0, )
        self._pilots_labels = ("On", "Off", )
        self._pilots_group_box = Qt.QGroupBox('Pilots')
        self._pilots_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._pilots_button_group = variable_chooser_button_group()
        self._pilots_group_box.setLayout(self._pilots_box)
        for i, label in enumerate(self._pilots_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._pilots_box.addWidget(radio_button)
        	self._pilots_button_group.addButton(radio_button, i)
        self._pilots_callback = lambda i: Qt.QMetaObject.invokeMethod(self._pilots_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._pilots_options.index(i)))
        self._pilots_callback(self.pilots)
        self._pilots_button_group.buttonClicked[int].connect(
        	lambda i: self.set_pilots(self._pilots_options[i]))
        self.top_grid_layout.addWidget(self._pilots_group_box, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._noise_type_options = ("Uniform", "Gaussian", "Laplacian", "Impulse", )
        self._noise_type_labels = (str(self._noise_type_options[0]), str(self._noise_type_options[1]), str(self._noise_type_options[2]), str(self._noise_type_options[3]), )
        self._noise_type_tool_bar = Qt.QToolBar(self)
        self._noise_type_tool_bar.addWidget(Qt.QLabel('Noise Type'+": "))
        self._noise_type_combo_box = Qt.QComboBox()
        self._noise_type_tool_bar.addWidget(self._noise_type_combo_box)
        for label in self._noise_type_labels: self._noise_type_combo_box.addItem(label)
        self._noise_type_callback = lambda i: Qt.QMetaObject.invokeMethod(self._noise_type_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._noise_type_options.index(i)))
        self._noise_type_callback(self.noise_type)
        self._noise_type_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_noise_type(self._noise_type_options[i]))
        self.top_grid_layout.addWidget(self._noise_type_tool_bar, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.noise_source = analog.noise_source_c(analog.GR_GAUSSIAN, 0, 0)
        self._noise_range = Range(0, 1, 0.01, 0.1, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise', "counter", float)
        self.top_grid_layout.addWidget(self._noise_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.file_source = blocks.file_source(gr.sizeof_char*1, '/home/anisan/videos/The_Maker/900.ts', True)
        self.file_source.set_begin_tag(pmt.PMT_NIL)
        self.fft_filter = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(1.0, samp_rate, samp_rate/2, rolloff, taps)), 1)
        self.fft_filter.declare_sample_delay(0)
        self.dvbs2_physical = dvbs2.physical_cc(dvbs2.FECFRAME_NORMAL, dvbs2.C9_10, dvbs2.MOD_16APSK, dvbs2.PILOTS_OFF, 0)
        self.dvbs2_modulator = dvbs2.modulator_bc(dvbs2.FECFRAME_NORMAL,
        dvbs2.C9_10, dvbs2.MOD_16APSK)
        self.dvbs2_ldpc = dvbs2.ldpc_bb(dvbs2.FECFRAME_NORMAL, dvbs2.C9_10, dvbs2.MOD_OTHER)
        self.dvbs2_interleaver = dvbs2.interleaver_bb(dvbs2.FECFRAME_NORMAL, dvbs2.C9_10, dvbs2.MOD_16APSK)
        self.dvbs2_bbscrambler = dvbs2.bbscrambler_bb(dvbs2.FECFRAME_NORMAL, dvbs2.C9_10)
        self.dvbs2_bbheader = dvbs2.bbheader_bb(dvbs2.FECFRAME_NORMAL, dvbs2.C9_10, dvbs2.RO_0_20)
        self.dvb_bch = dtv.dvb_bch_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10)
        self._code_rate_qpsk_options = ["1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "5/6", "8/9", "9/10"]
        self._code_rate_qpsk_labels = map(str, self._code_rate_qpsk_options)
        self._code_rate_qpsk_group_box = Qt.QGroupBox('Code Rate')
        self._code_rate_qpsk_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._code_rate_qpsk_button_group = variable_chooser_button_group()
        self._code_rate_qpsk_group_box.setLayout(self._code_rate_qpsk_box)
        for i, label in enumerate(self._code_rate_qpsk_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._code_rate_qpsk_box.addWidget(radio_button)
        	self._code_rate_qpsk_button_group.addButton(radio_button, i)
        self._code_rate_qpsk_callback = lambda i: Qt.QMetaObject.invokeMethod(self._code_rate_qpsk_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._code_rate_qpsk_options.index(i)))
        self._code_rate_qpsk_callback(self.code_rate_qpsk)
        self._code_rate_qpsk_button_group.buttonClicked[int].connect(
        	lambda i: self.set_code_rate_qpsk(self._code_rate_qpsk_options[i]))
        self.constellation_tab_layout_0.addWidget(self._code_rate_qpsk_group_box)
        self._code_rate_8psk_options = ["3/5", "2/3", "3/4", "4/5", "5/6", "8/9", "9/10"]
        self._code_rate_8psk_labels = map(str, self._code_rate_8psk_options)
        self._code_rate_8psk_group_box = Qt.QGroupBox('Code Rate')
        self._code_rate_8psk_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._code_rate_8psk_button_group = variable_chooser_button_group()
        self._code_rate_8psk_group_box.setLayout(self._code_rate_8psk_box)
        for i, label in enumerate(self._code_rate_8psk_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._code_rate_8psk_box.addWidget(radio_button)
        	self._code_rate_8psk_button_group.addButton(radio_button, i)
        self._code_rate_8psk_callback = lambda i: Qt.QMetaObject.invokeMethod(self._code_rate_8psk_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._code_rate_8psk_options.index(i)))
        self._code_rate_8psk_callback(self.code_rate_8psk)
        self._code_rate_8psk_button_group.buttonClicked[int].connect(
        	lambda i: self.set_code_rate_8psk(self._code_rate_8psk_options[i]))
        self.constellation_tab_layout_1.addWidget(self._code_rate_8psk_group_box)
        self._code_rate_32apsk_options = ["3/4", "4/5", "5/6", "8/9", "9/10"]
        self._code_rate_32apsk_labels = map(str, self._code_rate_32apsk_options)
        self._code_rate_32apsk_group_box = Qt.QGroupBox('Code Rate')
        self._code_rate_32apsk_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._code_rate_32apsk_button_group = variable_chooser_button_group()
        self._code_rate_32apsk_group_box.setLayout(self._code_rate_32apsk_box)
        for i, label in enumerate(self._code_rate_32apsk_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._code_rate_32apsk_box.addWidget(radio_button)
        	self._code_rate_32apsk_button_group.addButton(radio_button, i)
        self._code_rate_32apsk_callback = lambda i: Qt.QMetaObject.invokeMethod(self._code_rate_32apsk_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._code_rate_32apsk_options.index(i)))
        self._code_rate_32apsk_callback(self.code_rate_32apsk)
        self._code_rate_32apsk_button_group.buttonClicked[int].connect(
        	lambda i: self.set_code_rate_32apsk(self._code_rate_32apsk_options[i]))
        self.constellation_tab_layout_3.addWidget(self._code_rate_32apsk_group_box)
        self._code_rate_16apsk_options = [ "2/3", "3/4", "4/5", "5/6", "8/9", "9/10"]
        self._code_rate_16apsk_labels = map(str, self._code_rate_16apsk_options)
        self._code_rate_16apsk_group_box = Qt.QGroupBox('Code Rate')
        self._code_rate_16apsk_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._code_rate_16apsk_button_group = variable_chooser_button_group()
        self._code_rate_16apsk_group_box.setLayout(self._code_rate_16apsk_box)
        for i, label in enumerate(self._code_rate_16apsk_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._code_rate_16apsk_box.addWidget(radio_button)
        	self._code_rate_16apsk_button_group.addButton(radio_button, i)
        self._code_rate_16apsk_callback = lambda i: Qt.QMetaObject.invokeMethod(self._code_rate_16apsk_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._code_rate_16apsk_options.index(i)))
        self._code_rate_16apsk_callback(self.code_rate_16apsk)
        self._code_rate_16apsk_button_group.buttonClicked[int].connect(
        	lambda i: self.set_code_rate_16apsk(self._code_rate_16apsk_options[i]))
        self.constellation_tab_grid_layout_2.addWidget(self._code_rate_16apsk_group_box)
        _browse_button_push_button = Qt.QPushButton('Browse')
        self._browse_button_choices = {'Pressed': 1, 'Released': 0}
        _browse_button_push_button.pressed.connect(lambda: self.set_browse_button(self._browse_button_choices['Pressed']))
        _browse_button_push_button.released.connect(lambda: self.set_browse_button(self._browse_button_choices['Released']))
        self.top_grid_layout.addWidget(_browse_button_push_button, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.add_bloc = blocks.add_vcc(1)
        self._FEC_Frame_size_options = ('Normal', 'Short', )
        self._FEC_Frame_size_labels = (str(self._FEC_Frame_size_options[0]), str(self._FEC_Frame_size_options[1]), )
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
        self.top_grid_layout.addWidget(self._FEC_Frame_size_group_box, 4, 1, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.add_bloc, 0), (self.qtgui_freq_sink, 0))
        self.connect((self.dvb_bch, 0), (self.dvbs2_ldpc, 0))
        self.connect((self.dvbs2_bbheader, 0), (self.dvbs2_bbscrambler, 0))
        self.connect((self.dvbs2_bbscrambler, 0), (self.dvb_bch, 0))
        self.connect((self.dvbs2_interleaver, 0), (self.dvbs2_modulator, 0))
        self.connect((self.dvbs2_ldpc, 0), (self.dvbs2_interleaver, 0))
        self.connect((self.dvbs2_modulator, 0), (self.dvbs2_physical, 0))
        self.connect((self.dvbs2_physical, 0), (self.fft_filter, 0))
        self.connect((self.fft_filter, 0), (self.add_bloc, 0))
        self.connect((self.file_source, 0), (self.dvbs2_bbheader, 0))
        self.connect((self.noise_source, 0), (self.add_bloc, 1))

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

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink.set_frequency_range(self.center_freq, self.samp_rate)
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self._rolloff_callback(self.rolloff)
        self.fft_filter.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_qtgui_variable(self):
        return self.qtgui_variable

    def set_qtgui_variable(self, qtgui_variable):
        self.qtgui_variable = qtgui_variable
        Qt.QMetaObject.invokeMethod(self._qtgui_variable_label, "setText", Qt.Q_ARG("QString", self.qtgui_variable))

    def get_pilots(self):
        return self.pilots

    def set_pilots(self, pilots):
        self.pilots = pilots
        self._pilots_callback(self.pilots)

    def get_noise_type(self):
        return self.noise_type

    def set_noise_type(self, noise_type):
        self.noise_type = noise_type
        self._noise_type_callback(self.noise_type)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise

    def get_code_rate_qpsk(self):
        return self.code_rate_qpsk

    def set_code_rate_qpsk(self, code_rate_qpsk):
        self.code_rate_qpsk = code_rate_qpsk
        self._code_rate_qpsk_callback(self.code_rate_qpsk)

    def get_code_rate_8psk(self):
        return self.code_rate_8psk

    def set_code_rate_8psk(self, code_rate_8psk):
        self.code_rate_8psk = code_rate_8psk
        self._code_rate_8psk_callback(self.code_rate_8psk)

    def get_code_rate_32apsk(self):
        return self.code_rate_32apsk

    def set_code_rate_32apsk(self, code_rate_32apsk):
        self.code_rate_32apsk = code_rate_32apsk
        self._code_rate_32apsk_callback(self.code_rate_32apsk)

    def get_code_rate_16apsk(self):
        return self.code_rate_16apsk

    def set_code_rate_16apsk(self, code_rate_16apsk):
        self.code_rate_16apsk = code_rate_16apsk
        self._code_rate_16apsk_callback(self.code_rate_16apsk)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink.set_frequency_range(self.center_freq, self.samp_rate)

    def get_browse_button(self):
        return self.browse_button

    def set_browse_button(self, browse_button):
        self.browse_button = browse_button

    def get_FEC_Frame_size(self):
        return self.FEC_Frame_size

    def set_FEC_Frame_size(self, FEC_Frame_size):
        self.FEC_Frame_size = FEC_Frame_size
        self._FEC_Frame_size_callback(self.FEC_Frame_size)


def main(top_block_cls=dvbs2_tx, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
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
