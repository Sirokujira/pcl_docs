
.. _program_listing_file_pcl_io_include_pcl_io_image_metadata_wrapper.h:

Program Listing for File image_metadata_wrapper.h
=================================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_io_include_pcl_io_image_metadata_wrapper.h>` (``pcl\io\include\pcl\io\image_metadata_wrapper.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Software License Agreement (BSD License)
    * 
    * Point Cloud Library (PCL) - www.pointclouds.org
    * Copyright (c) 2009-2012, Willow Garage, Inc.
    * Copyright (c) 2012-, Open Perception, Inc.
    * Copyright (c) 2014, respective authors.
    * 
    * All rights reserved.
    * 
    * Redistribution and use in source and binary forms, with or without
    * modification, are permitted provided that the following conditions
    * are met:
    * 
    *  * Redistributions of source code must retain the above copyright
    *    notice, this list of conditions and the following disclaimer.
    *  * Redistributions in binary form must reproduce the above
    *    copyright notice, this list of conditions and the following
    *    disclaimer in the documentation and/or other materials provided
    *    with the distribution.
    *  * Neither the name of the copyright holder(s) nor the names of its
    *    contributors may be used to endorse or promote products derived
    *    from this software without specific prior written permission.
    * 
    * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
    * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    * POSSIBILITY OF SUCH DAMAGE.
    *
    */
   
   #pragma once
   #ifndef PCL_IO_IMAGE_METADATA_WRAPPER_H_
   #define PCL_IO_IMAGE_METADATA_WRAPPER_H_
   
   #include <pcl/pcl_config.h>
   #include <pcl/pcl_macros.h>
   
   namespace pcl
   {
     namespace io
     {
   
       /**
       * Pure abstract interface to wrap native frame data types.
       */
       class FrameWrapper
       {
         public:
           typedef boost::shared_ptr<FrameWrapper> Ptr;
   
           virtual const void*
           getData () const = 0;
   
           virtual unsigned
           getDataSize () const = 0;
   
           virtual unsigned
           getWidth () const = 0;
   
           virtual unsigned
           getHeight () const = 0;
   
           virtual unsigned
           getFrameID () const = 0;
   
           // Microseconds from some arbitrary start point
           virtual pcl::uint64_t
           getTimestamp () const = 0;
       };
   
     } // namespace
   }
   
   #endif // PCL_IO_IMAGE_METADATA_WRAPPER_H_
