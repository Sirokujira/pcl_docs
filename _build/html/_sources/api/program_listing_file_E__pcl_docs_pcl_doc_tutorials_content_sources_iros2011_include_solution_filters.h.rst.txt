
.. _program_listing_file_E__pcl_docs_pcl_doc_tutorials_content_sources_iros2011_include_solution_filters.h:

Program Listing for File filters.h
==================================

|exhale_lsh| :ref:`Return to documentation for file <file_E__pcl_docs_pcl_doc_tutorials_content_sources_iros2011_include_solution_filters.h>` (``E:\pcl_docs\pcl\doc\tutorials\content\sources\iros2011\include\solution\filters.h``)

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
     pcl::PassThrough<PointT> pass_through;
     pass_through.setInputCloud (input);
     pass_through.setFilterFieldName ("z");
     pass_through.setFilterLimits (min_depth, max_depth);
     PointCloudPtr thresholded (new PointCloud);
     pass_through.filter (*thresholded);
   
     return (thresholded);
   }
   
   /* Use a VoxelGrid filter to reduce the number of points */
   PointCloudPtr
   downsample (const PointCloudPtr & input, float leaf_size)
   {
     pcl::VoxelGrid<PointT> voxel_grid;
     voxel_grid.setInputCloud (input);
     voxel_grid.setLeafSize (leaf_size, leaf_size, leaf_size);
     PointCloudPtr downsampled (new PointCloud);
     voxel_grid.filter (*downsampled);
   
     return (downsampled);
   }
   
   /* Use a RadiusOutlierRemoval filter to remove all points with too few local neighbors */
   PointCloudPtr
   removeOutliers (const PointCloudPtr & input, float radius, int min_neighbors)
   {
     pcl::RadiusOutlierRemoval<pcl::PointXYZRGB> radius_outlier_removal;
     radius_outlier_removal.setInputCloud (input);
     radius_outlier_removal.setRadiusSearch (radius);
     radius_outlier_removal.setMinNeighborsInRadius (min_neighbors);
     PointCloudPtr inliers (new PointCloud);
     radius_outlier_removal.filter (*inliers);
   
     return (inliers);
   }
   
   /* Apply a series of filters (threshold depth, downsample, and remove outliers) */
   PointCloudPtr
   applyFilters (const PointCloudPtr & input, float min_depth, float max_depth, float leaf_size, float radius, 
                 float min_neighbors)
   {
     PointCloudPtr filtered;
     filtered = thresholdDepth (input, min_depth, max_depth);
     filtered = downsample (filtered, leaf_size);
     filtered = removeOutliers (filtered, radius, min_neighbors);
   
     return (filtered);
   }
