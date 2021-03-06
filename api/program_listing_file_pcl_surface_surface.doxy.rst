
.. _program_listing_file_pcl_surface_surface.doxy:

Program Listing for File surface.doxy
=====================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_surface_surface.doxy>` (``pcl\surface\surface.doxy``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /**
     \addtogroup surface Module surface
   
     \section secSurfacePresentation Overview
   
   The <b>pcl_surface</b> library deals with reconstructing the original
   surfaces from 3D scans.  Depending on the task at hand, this can be for
   example the hull, a mesh representation or a smoothed/resampled surface with
   normals.
   
   Smoothing and resampling can be important if the cloud is noisy, or if it is
   composed of multiple scans that are not aligned perfectly.  The complexity
   of the surface estimation can be adjusted, and normals can be estimated in
   the same step if needed.
   
   \image html http://www.pointclouds.org/documentation/tutorials/_images/resampling_1.jpg
   
   Meshing is a general way to create a surface out of points, and currently
   there are two algorithms provided: a very fast triangulation of the original
   points, and a slower meshing that does smoothing and hole filling as well.
   
   \image html http://www.pointclouds.org/assets/images/contents/documentation/surface_meshing.png
   
   Creating a convex or concave hull is useful for example when there is a need
   for a simplified surface representation or when boundaries need to be
   extracted.
   
   \image html http://www.pointclouds.org/assets/images/contents/documentation/surface_hull.png
   
   Please visit the tutorials on http://www.pointclouds.org for more information.
     
     \section secSurfaceRequirements Requirements
     - \ref common "common"
     - \ref search "search"
     - \ref kdtree "kdtree"
     - \ref octree "octree"
   
   */
