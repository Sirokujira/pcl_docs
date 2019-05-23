
.. _program_listing_file_E__pcl_docs_pcl_doc_tutorials_content_sources_iros2011_include_surface.h:

Program Listing for File surface.h
==================================

|exhale_lsh| :ref:`Return to documentation for file <file_E__pcl_docs_pcl_doc_tutorials_content_sources_iros2011_include_surface.h>` (``E:\pcl_docs\pcl\doc\tutorials\content\sources\iros2011\include\surface.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <pcl/kdtree/kdtree_flann.h>
   #include <pcl/surface/mls.h>
   #include <pcl/surface/convex_hull.h>
   #include <pcl/surface/concave_hull.h>
   #include <pcl/surface/gp3.h>
   #include <pcl/surface/marching_cubes_hoppe.h>
   
   #include "typedefs.h"
   
   
   class Mesh
   {
   public:
     Mesh () : points (new PointCloud) {}
     PointCloudPtr points;
     std::vector<pcl::Vertices> faces;
   };
   
   typedef boost::shared_ptr<Mesh> MeshPtr;
   
   PointCloudPtr
   smoothPointCloud (const PointCloudPtr & input, float radius, int polynomial_order)
   {
     PointCloudPtr output (new PointCloud);
     return (output);
   }
   
   SurfaceElementsPtr
   computeSurfaceElements (const PointCloudPtr & input, float radius, int polynomial_order)
   {
     SurfaceElementsPtr surfels (new SurfaceElements);
     return (surfels);
   }
   
   MeshPtr
   computeConvexHull (const PointCloudPtr & input)
   {
     MeshPtr output (new Mesh);
     return (output);
   }
   
   
   MeshPtr
   computeConcaveHull (const PointCloudPtr & input, float alpha)
   {
     MeshPtr output (new Mesh);
     return (output);
   }
   
   pcl::PolygonMesh::Ptr
   greedyTriangulation (const SurfaceElementsPtr & surfels, float radius, float mu, int max_nearest_neighbors, 
                        float max_surface_angle, float min_angle, float max_angle)
   
   {
     pcl::PolygonMesh::Ptr output (new pcl::PolygonMesh);
     return (output);
   }
   
   
   pcl::PolygonMesh::Ptr
   marchingCubesTriangulation (const SurfaceElementsPtr & surfels, float leaf_size, float iso_level)
   {
     pcl::PolygonMesh::Ptr output (new pcl::PolygonMesh);
     return (output);
   }
