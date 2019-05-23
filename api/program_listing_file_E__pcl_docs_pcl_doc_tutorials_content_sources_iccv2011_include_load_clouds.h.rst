
.. _program_listing_file_E__pcl_docs_pcl_doc_tutorials_content_sources_iccv2011_include_load_clouds.h:

Program Listing for File load_clouds.h
======================================

|exhale_lsh| :ref:`Return to documentation for file <file_E__pcl_docs_pcl_doc_tutorials_content_sources_iccv2011_include_load_clouds.h>` (``E:\pcl_docs\pcl\doc\tutorials\content\sources\iccv2011\include\load_clouds.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include "typedefs.h"
   
   #include <pcl/io/pcd_io.h>
     
   template <typename PointT>
   typename pcl::PointCloud<PointT>::Ptr
   loadPointCloud (std::string filename, std::string suffix)
   {
     typename pcl::PointCloud<PointT>::Ptr output (new pcl::PointCloud<PointT>);
     filename.append (suffix);
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
   
   PointCloudPtr
   loadPoints (std::string filename)
   {
     PointCloudPtr output (new PointCloud);
     filename.append ("_points.pcd");
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
   
   SurfaceNormalsPtr
   loadSurfaceNormals(std::string filename)
   {
     SurfaceNormalsPtr output (new SurfaceNormals);
     filename.append ("_normals.pcd");
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
   
   PointCloudPtr
   loadKeypoints (std::string filename)
   {
     PointCloudPtr output (new PointCloud);
     filename.append ("_keypoints.pcd");
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
   
   LocalDescriptorsPtr
   loadLocalDescriptors (std::string filename)
   {
     LocalDescriptorsPtr output (new LocalDescriptors);
     filename.append ("_localdesc.pcd");
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
   
   GlobalDescriptorsPtr
   loadGlobalDescriptors (std::string filename)
   {
     GlobalDescriptorsPtr output (new GlobalDescriptors);
     filename.append ("_globaldesc.pcd");
     pcl::io::loadPCDFile (filename, *output);
     pcl::console::print_info ("Loaded %s (%lu points)\n", filename.c_str (), output->size ());
     return (output);
   }
