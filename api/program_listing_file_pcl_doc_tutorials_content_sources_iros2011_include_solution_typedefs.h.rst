
.. _program_listing_file_pcl_doc_tutorials_content_sources_iros2011_include_solution_typedefs.h:

Program Listing for File typedefs.h
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_doc_tutorials_content_sources_iros2011_include_solution_typedefs.h>` (``pcl\doc\tutorials\content\sources\iros2011\include\solution\typedefs.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef TYPEDEFS_H
   #define TYPEDEFS_H
   
   #include <pcl/point_types.h>
   #include <pcl/point_cloud.h>
   
   /* Define some custom types to make the rest of our code easier to read */
   
   // Define "PointCloud" to be a pcl::PointCloud of pcl::PointXYZRGB points
   typedef pcl::PointXYZRGB PointT;
   typedef pcl::PointCloud<PointT> PointCloud;
   typedef pcl::PointCloud<PointT>::Ptr PointCloudPtr;
   typedef pcl::PointCloud<PointT>::ConstPtr PointCloudConstPtr;
   
   // Define "SurfaceNormals" to be a pcl::PointCloud of pcl::Normal points
   typedef pcl::Normal NormalT;
   typedef pcl::PointCloud<NormalT> SurfaceNormals;
   typedef pcl::PointCloud<NormalT>::Ptr SurfaceNormalsPtr;
   typedef pcl::PointCloud<NormalT>::ConstPtr SurfaceNormalsConstPtr;
   
   // Define "LocalDescriptors" to be a pcl::PointCloud of pcl::FPFHSignature33 points
   typedef pcl::FPFHSignature33 LocalDescriptorT;
   typedef pcl::PointCloud<LocalDescriptorT> LocalDescriptors;
   typedef pcl::PointCloud<LocalDescriptorT>::Ptr LocalDescriptorsPtr;
   typedef pcl::PointCloud<LocalDescriptorT>::ConstPtr LocalDescriptorsConstPtr;
   
   // Define "GlobalDescriptors" to be a pcl::PointCloud of pcl::VFHSignature308 points
   typedef pcl::VFHSignature308 GlobalDescriptorT;
   typedef pcl::PointCloud<GlobalDescriptorT> GlobalDescriptors;
   typedef pcl::PointCloud<GlobalDescriptorT>::Ptr GlobalDescriptorsPtr;
   typedef pcl::PointCloud<GlobalDescriptorT>::ConstPtr GlobalDescriptorsConstPtr;
   
   #endif
