
.. _program_listing_file_pcl_visualization_include_pcl_visualization_vtk_pcl_image_canvas_source_2d.h:

Program Listing for File pcl_image_canvas_source_2d.h
=====================================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_visualization_include_pcl_visualization_vtk_pcl_image_canvas_source_2d.h>` (``pcl\visualization\include\pcl\visualization\vtk\pcl_image_canvas_source_2d.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Software License Agreement (BSD License)
    *
    *  Point Cloud Library (PCL) - www.pointclouds.org
    *  Copyright (c) 2010-2012, Willow Garage, Inc.
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
    */
   #ifndef PCL_VTK_IMAGE_CANVAS_SOURCE_2D_H_
   #define PCL_VTK_IMAGE_CANVAS_SOURCE_2D_H_
   
   #include <pcl/pcl_macros.h>
   #include <vtkImageCanvasSource2D.h>
   
   namespace pcl
   {
     namespace visualization
     {
       /** \brief PCLImageCanvasSource2D represents our own custom version of 
         * vtkImageCanvasSource2D, used by the ImageViewer class.
         */
       class PCL_EXPORTS PCLImageCanvasSource2D : public vtkImageCanvasSource2D
       {
         public:
           static PCLImageCanvasSource2D *New ();
   
           void 
           DrawImage (vtkImageData* image);
       };
     }
   }
   
   #endif      // PCL_VTK_IMAGE_CANVAS_SOURCE_2D_H_
