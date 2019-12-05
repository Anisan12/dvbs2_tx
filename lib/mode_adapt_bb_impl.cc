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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "mode_adapt_bb_impl.h"

namespace gr {
  namespace dvbs2 {

    mode_adapt_bb::sptr
    mode_adapt_bb::make(dvbs2_framesize_t framesize, dvbs2_issyi_t issyiparam)
    {
      return gnuradio::get_initial_sptr
        (new mode_adapt_bb_impl(framesize, issyiparam));
    }

    /*
     * The private constructor
     */
    mode_adapt_bb_impl::mode_adapt_bb_impl(dvbs2_framesize_t framesize, dvbs2_issyi_t issyiparam) : gr::block("mode_adapt_bb",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)))
    {
        frame_size = framesize;

        if (framesize == FECFRAME_NORMAL) {
          switch (rate) {
            case C1_4:
              kbch = 16008;
              break;
            case C1_3:
              kbch = 21408;
              break;
            case C2_5:
              kbch = 25728;
              break;
            case C1_2:
              kbch = 32208;
              break;
            case C3_5:
              kbch = 38688;
              break;
            case C2_3:
              kbch = 43040;
              break;
            case C3_4:
              kbch = 48408;
              break;
            case C4_5:
              kbch = 51648;
              break;
            case C5_6:
              kbch = 53840;
              break;
            case C8_9:
              kbch = 57472;
              break;
            case C9_10:
              kbch = 58192;
              break;
            case C2_9_VLSNR:
              kbch = 14208;
              break;
            case C13_45:
              kbch = 18528;
              break;
            case C9_20:
              kbch = 28968;
              break;
            case C90_180:
              kbch = 32208;
              break;
            case C96_180:
              kbch = 34368;
              break;
            case C11_20:
              kbch = 35448;
              break;
            case C100_180:
              kbch = 35808;
              break;
            case C104_180:
              kbch = 37248;
              break;
            case C26_45:
              kbch = 37248;
              break;
            case C18_30:
              kbch = 38688;
              break;
            case C28_45:
              kbch = 40128;
              break;
            case C23_36:
              kbch = 41208;
              break;
            case C116_180:
              kbch = 41568;
              break;
            case C20_30:
              kbch = 43008;
              break;
            case C124_180:
              kbch = 44448;
              break;
            case C25_36:
              kbch = 44808;
              break;
            case C128_180:
              kbch = 45888;
              break;
            case C13_18:
              kbch = 46608;
              break;
            case C132_180:
              kbch = 47328;
              break;
            case C22_30:
              kbch = 47328;
              break;
            case C135_180:
              kbch = 48408;
              break;
            case C140_180:
              kbch = 50208;
              break;
            case C7_9:
              kbch = 50208;
              break;
            case C154_180:
              kbch = 55248;
              break;
            default:
              kbch = 0;
              break;
          }
        }
        else if (framesize == FECFRAME_SHORT) {
          switch (rate) {
            case C1_4:
              kbch = 3072;
              break;
            case C1_3:
              kbch = 5232;
              break;
            case C2_5:
              kbch = 6312;
              break;
            case C1_2:
              kbch = 7032;
              break;
            case C3_5:
              kbch = 9552;
              break;
            case C2_3:
              kbch = 10632;
              break;
            case C3_4:
              kbch = 11712;
              break;
            case C4_5:
              kbch = 12432;
              break;
            case C5_6:
              kbch = 13152;
              break;
            case C8_9:
              kbch = 14232;
              break;
            case C11_45:
              kbch = 3792;
              break;
            case C4_15:
              kbch = 4152;
              break;
            case C14_45:
              kbch = 4872;
              break;
            case C7_15:
              kbch = 7392;
              break;
            case C8_15:
              kbch = 8472;
              break;
            case C26_45:
              kbch = 9192;
              break;
            case C32_45:
              kbch = 11352;
              break;
            case C1_5_VLSNR_SF2:
              kbch = 2512;
              break;
            case C11_45_VLSNR_SF2:
              kbch = 3792;
              break;
            case C1_5_VLSNR:
              kbch = 3072;
              break;
            case C4_15_VLSNR:
              kbch = 4152;
              break;
            case C1_3_VLSNR:
              kbch = 5232;
              break;
            default:
              kbch = 0;
              break;
          }
        }
        else {
          switch (rate) {
            case C1_5_MEDIUM:
              kbch = 5660;
              break;
            case C11_45_MEDIUM:
              kbch = 7740;
              break;
            case C1_3_MEDIUM:
              kbch = 10620;
              break;
            default:
              kbch = 0;
              break;
          }
        }
    }      

    void
    mode_adapt_bb_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
       ninput_items_required[0] = noutput_items;
    }

    char
    issy_bb_impl::check_if_issy_on(char* frame){
        return frame[4];
    }


    int
    mode_adapt_bb_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];
      unsigned char c_out = (unsigned char) *output_items;

      //10 bit of headers
      unsigned int offset = 0;
      unsigned char b;
      unsigned int dfl = kbch - 80;

      if (!check_if_issy_on(&c_cout){
        out[i] = in[i];
        return 0;
      }
      //for all the frame
      for (int i = 0; i < noutput_items; i += kbch) {

        if (frame_size == FECFRAME_MEDIUM) {

          offset = offset + kbch;
          //for all the packets within the frame

          counter  = (counter + 1) % 4194304;
          bc_cout[offset++] = *in++;

          for (int n = 23; n >= 0; n--) {
            //put the msb to 1
            if (n==23){
              c_cout[offset++] = counter | (1 << n);
              
            }
            //put the 6th bit to 0
            else if (n==22){
              c_cout[offset++] = counter & (1 << n);
            }
            else{
              c_cout[offset++] = counter & (1 << n) ? 1 : 0;
            }
          }

        // the frame is SHORT otherwise
        }else{

          offset = offset + kbch;

          counter  = (counter + 1) % 32768;

          bc_cout[offset++] = *in++;
  
          //the rest is encoded over 21 last bits
          for (int n = 14; n >= 0; n--) {
            //put the msb to 1
            if (n==14){
              c_cout[offset++] = counter & (1 << n);
              //put the 6th bit to 0
            }
            else{
              c_cout[offset++] = counter & (1 << n) ? 1 : 0;
            }
          }
        }
        out[i] = in[i];
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }
  } /* namespace dvbs2 */
} /* namespace gr */

