
.. _program_listing_file_pcl_segmentation_include_pcl_segmentation_crf_normal_segmentation.h:

Program Listing for File crf_normal_segmentation.h
==================================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_segmentation_include_pcl_segmentation_crf_normal_segmentation.h>` (``pcl\segmentation\include\pcl\segmentation\crf_normal_segmentation.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Software License Agreement (BSD License)
    *
    *  Point Cloud Library (PCL) - www.pointclouds.org
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
   
   #ifndef PCL_CRF_NORMAL_SEGMENTATION_H_
   #define PCL_CRF_NORMAL_SEGMENTATION_H_
   
   #include <pcl/point_cloud.h>
   
   namespace pcl
   {
     /** \brief
       * \author Christian Potthast
       * 
       */
     template <typename PointT>
     class PCL_EXPORTS CrfNormalSegmentation
     {
       public:
   
         /** \brief Constructor that sets default values for member variables. */
         CrfNormalSegmentation ();
   
         /** \brief Destructor that frees memory. */
         ~CrfNormalSegmentation ();
   
         /** \brief This method sets the input cloud.
           * \param[in] input_cloud input point cloud
           */
         void
         setCloud (typename pcl::PointCloud<PointT>::Ptr input_cloud);
   
         /** \brief This method simply launches the segmentation algorithm */
         void
         segmentPoints ();
   
       protected:
   
       protected:
   
   
       public:
         EIGEN_MAKE_ALIGNED_OPERATOR_NEW
     };
   }
   
   #ifdef PCL_NO_PRECOMPILE
   #include <pcl/segmentation/impl/crf_normal_segmentation.hpp>
   #endif
   
   #endif
