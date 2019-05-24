
.. _program_listing_file_pcl_docs_source_pcl_doc_tutorials_content_sources_iros2011_include_segmentation.h:

Program Listing for File segmentation.h
=======================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_source_pcl_doc_tutorials_content_sources_iros2011_include_segmentation.h>` (``pcl_docs\source\pcl\doc\tutorials\content\sources\iros2011\include\segmentation.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include "typedefs.h"
   
   #include <pcl/ModelCoefficients.h>
   #include <pcl/sample_consensus/method_types.h>
   #include <pcl/sample_consensus/model_types.h>
   #include <pcl/segmentation/sac_segmentation.h>
   #include <pcl/filters/extract_indices.h>
   #include <pcl/segmentation/extract_clusters.h>
   
   
   /* Use SACSegmentation to find the dominant plane in the scene
    * Inputs:
    *   input 
    *     The input point cloud
    *   max_iterations 
    *     The maximum number of RANSAC iterations to run
    *   distance_threshold 
    *     The inlier/outlier threshold.  Points within this distance
    *     from the hypothesized plane are scored as inliers.
    * Return: A pointer to the ModelCoefficients (i.e., the 4 coefficients of the plane, 
    *         represented in c0*x + c1*y + c2*z + c3 = 0 form)
    */
   pcl::ModelCoefficients::Ptr
   fitPlane (const PointCloudPtr & input, float distance_threshold, float max_iterations)
   {
     pcl::ModelCoefficients::Ptr coefficients;
     return (coefficients);
   }
   
   /* Use SACSegmentation and an ExtractIndices filter to find the dominant plane and subtract it
    * Inputs:
    *   input 
    *     The input point cloud
    *   max_iterations 
    *     The maximum number of RANSAC iterations to run
    *   distance_threshold 
    *     The inlier/outlier threshold.  Points within this distance
    *     from the hypothesized plane are scored as inliers.
    * Return: A pointer to a new point cloud which contains only the non-plane points
    */
   PointCloudPtr
   findAndSubtractPlane (const PointCloudPtr & input, float distance_threshold, float max_iterations)
   {
     PointCloudPtr output;
     return (output);
   }
   
   /* Use EuclidieanClusterExtraction to group a cloud into contiguous clusters
    * Inputs:
    *   input
    *     The input point cloud
    *   cluster_tolerance
    *     The maximum distance between neighboring points in a cluster
    *   min/max_cluster_size
    *     The minimum and maximum allowable cluster sizes
    * Return (by reference): a vector of PointIndices containing the points indices in each cluster
    */
   void
   clusterObjects (const PointCloudPtr & input, 
                   float cluster_tolerance, int min_cluster_size, int max_cluster_size,
                   std::vector<pcl::PointIndices> & cluster_indices_out)
   {  
   }
