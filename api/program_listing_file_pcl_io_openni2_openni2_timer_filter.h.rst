
.. _program_listing_file_pcl_io_openni2_openni2_timer_filter.h:

Program Listing for File openni2_timer_filter.h
===============================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_io_openni2_openni2_timer_filter.h>` (``pcl\io\openni2\openni2_timer_filter.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Copyright (c) 2013, Willow Garage, Inc.
    * All rights reserved.
    *
    * Redistribution and use in source and binary forms, with or without
    * modification, are permitted provided that the following conditions are met:
    *
    *     * Redistributions of source code must retain the above copyright
    *       notice, this list of conditions and the following disclaimer.
    *     * Redistributions in binary form must reproduce the above copyright
    *       notice, this list of conditions and the following disclaimer in the
    *       documentation and/or other materials provided with the distribution.
    *     * Neither the name of the Willow Garage, Inc. nor the names of its
    *       contributors may be used to endorse or promote products derived from
    *       this software without specific prior written permission.
    *
    * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
    * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    * POSSIBILITY OF SUCH DAMAGE.
    *
    *      Author: Julius Kammerl (jkammerl@willowgarage.com)
    */
   
   #pragma once
   
   #include <deque>
   
   #include "OpenNI.h"
   
   namespace pcl
   {
     namespace io
     {
       namespace openni2
       {
   
         class OpenNI2TimerFilter
         {
           public:
             OpenNI2TimerFilter (std::size_t filter_len);
             virtual ~OpenNI2TimerFilter ();
   
             void
             addSample (double sample);
   
             double
             getMedian ();
   
             double
             getMovingAvg ();
   
             void
             clear ();
   
           private:
             std::size_t filter_len_;
   
             std::deque<double> buffer_;
         };
   
       } // namespace
     }
   }
