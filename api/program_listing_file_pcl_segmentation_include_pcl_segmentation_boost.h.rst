
.. _program_listing_file_pcl_segmentation_include_pcl_segmentation_boost.h:

Program Listing for File boost.h
================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_segmentation_include_pcl_segmentation_boost.h>` (``pcl\segmentation\include\pcl\segmentation\boost.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Software License Agreement (BSD License)
    *
    *  Point Cloud Library (PCL) - www.pointclouds.org
    *  Copyright (c) 2010-2011, Willow Garage, Inc.
    *  Copyright (c) 2012-, Open Perception, Inc.
    *
    *  All rights reserved.
    *
    *  Redistribution and use in source and binary forms, with or without
    *  modification, are permitted provided that the following conditions
    *  are met:
    *
    *   * Redistributions of source code must retain the above copyright
    *     notice, this list of conditions and the following disclaimer.
    *   * Redistributions in binary form must reproduce the above
    *     copyright notice, this list of conditions and the following
    *     disclaimer in the documentation and/or other materials provided
    *     with the distribution.
    *   * Neither the name of the copyright holder(s) nor the names of its
    *     contributors may be used to endorse or promote products derived
    *     from this software without specific prior written permission.
    *
    *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
    *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    *  POSSIBILITY OF SUCH DAMAGE.
    *
    * $Id: io.h 5850 2012-06-06 14:04:59Z stfox88 $
    *
    */
   
   #ifndef PCL_SEGMENTATION_BOOST_H_
   #define PCL_SEGMENTATION_BOOST_H_
   
   #ifdef __GNUC__
   #pragma GCC system_header 
   #endif
   
   #ifndef Q_MOC_RUN
   // Marking all Boost headers as system headers to remove warnings
   #include <boost/version.hpp>
   #include <boost/make_shared.hpp>
   #include <boost/graph/adjacency_list.hpp>
   #include <boost/multi_array.hpp>
   #include <boost/ptr_container/ptr_list.hpp>
   
   #if (BOOST_VERSION >= 104400) 
     #include <boost/graph/boykov_kolmogorov_max_flow.hpp>
   #endif 
   #endif
   
   #endif    // PCL_SEGMENTATION_BOOST_H_
