
.. _program_listing_file_pcl_io_include_pcl_io_file_grabber.h:

Program Listing for File file_grabber.h
=======================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_io_include_pcl_io_file_grabber.h>` (``pcl\io\include\pcl\io\file_grabber.h``)

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
    * $Id: file_grabber.h 8413 2013-01-15 08:37:39Z sdmiller $
    *
    */
   
   #pragma once
   #ifndef PCL_IO_FILE_GRABBER_H_
   #define PCL_IO_FILE_GRABBER_H_
   
   #include <pcl/point_cloud.h>
   
   namespace pcl
   {
     /** \brief FileGrabber provides a container-style interface for grabbers which operate on fixed-size input
       * \author Stephen Miller
       * \ingroup io
       */
     template <typename PointT>
     class PCL_EXPORTS FileGrabber
     {
     public:
   
       /** \brief Empty destructor */
       virtual ~FileGrabber () {}
   
       /** \brief operator[] Returns the idx-th cloud in the dataset, without bounds checking.
        *  Note that in the future, this could easily be modified to do caching
        *  \param[in] idx The frame to load
        */
       virtual const boost::shared_ptr< const pcl::PointCloud<PointT> >
       operator[] (size_t idx) const = 0;
   
       /** \brief size Returns the number of clouds currently loaded by the grabber */
       virtual size_t
       size () const = 0;
       
       /** \brief at Returns the idx-th cloud in the dataset, with bounds checking
        *  \param[in] idx The frame to load
        */
       virtual const boost::shared_ptr< const pcl::PointCloud<PointT> >
       at (size_t idx) const
       {
         if (idx >= size ())
         {
           // Throw error 
           throw pcl::IOException ("[pcl::FileGrabber] Attempted to access element which is out of bounds!");
         }
         else
         {
           return (operator[] (idx));
         }
       }
     };
   }
   #endif//PCL_IO_FILE_GRABBER_H_
   
