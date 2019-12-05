/* -*- c++ -*- */
/* 
 * Copyright 2014,2016 Ron Economos.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_DVBS2_PHYSICAL_CC_H
#define INCLUDED_DVBS2_PHYSICAL_CC_H

#include <dvbs2/api.h>
#include <dvbs2/dvbs2_config.h>
#include <gnuradio/block.h>

namespace gr {
  namespace dvbs2 {

    /*!
     * \brief Signals DVB-S2 physical layer frames.
     * \ingroup dvbs2
     *
     * Input: QPSK, 8PSK, 16APSK or 32APSK modulated complex IQ values (XFECFRAME).
     * Output: DVB-S2 PLFRAME.
     */
    class DVBS2_API physical_cc : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<physical_cc> sptr;

      /*!
       * \brief Create a DVB-S2 physical layer framer.
       *
       * \param framesize FEC frame size (normal or short).
       * \param rate FEC code rate.
       * \param constellation DVB-S2 constellation.
       * \param pilots pilot symbols (on/off).
       * \param goldcode physical layer scrambler Gold code (0 to 262141 inclusive).
       */
      static sptr make(dvbs2_framesize_t framesize, dvbs2_code_rate_t rate, dvbs2_constellation_t constellation, dvbs2_pilots_t pilots, int goldcode);
    };

  } // namespace dvbs2
} // namespace gr

#endif /* INCLUDED_DVBS2_PHYSICAL_CC_H */

