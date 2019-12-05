/* -*- c++ -*- */
/* 
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
 */

#ifndef INCLUDED_DVBS2_ISSY_BB_IMPL_H
#define INCLUDED_DVBS2_ISSY_BB_IMPL_H

#include <dvbs2/issy_bb.h>

namespace gr {
  namespace dvbs2 {

    class issy_bb_impl : public issy_bb 
    {
     private:

     unsigned int frame_size;
     unsigned int counter;
     unsigned int kbch;

     char issy_bb_impl::check_if_issy_on(char* frame);

    }

     public:
      issy_bb_impl(dvbs2_framesize_t framesize);
      ~issy_bb_impl();

      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items);
    };

  } // namespace dvbs2
} // namespace gr

#endif /* INCLUDED_DVBS2_ISSY_BB_IMPL_H */

