
.. _program_listing_file_pcl_docs_source_pcl_doc_tutorials_content_sources_iros2011_include_filters.h:

Program Listing for File filters.h
==================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_source_pcl_doc_tutorials_content_sources_iros2011_include_filters.h>` (``pcl_docs\source\pcl\doc\tutorials\content\sources\iros2011\include\filters.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <pcl/filters/passthrough.h>
   #include <pcl/filters/voxel_grid.h>
   #include <pcl/filters/radius_outlier_removal.h>
   
   #include "typedefs.h"
   
   /* Use a PassThrough filter to remove points with depth values that are too large or too small */
   PointCloudPtr
   thresholdDepth (const PointCloudPtr & input, float min_depth, float max_depth)
   {
     PointCloudPtr thresholded;
     return (thresholded);
   }
   
   /* Use a VoxelGrid filter to reduce the number of points */
   PointCloudPtr
   downsample (const PointCloudPtr & input, float leaf_size)
   {
     PointCloudPtr downsampled;
     return (downsampled);
   }
   
   /* Use a RadiusOutlierRemoval filter to remove all points with too few local neighbors */
   PointCloudPtr
   removeOutliers (const PointCloudPtr & input, float radius, int min_neighbors)
   {
     PointCloudPtr inliers;
     return (inliers);
   }
