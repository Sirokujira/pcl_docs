
.. _program_listing_file_pcl_docs_pcl_visualization_visualization.doxy:

Program Listing for File visualization.doxy
===========================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_pcl_visualization_visualization.doxy>` (``pcl_docs\pcl\visualization\visualization.doxy``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /**
     \addtogroup visualization Module visualization
   
     \section secVisualizationPresentation Overview
   
     The <b>pcl_visualization</b> library was built for the purpose of being able to quickly prototype and visualize the 
     results of algorithms operating on 3D point cloud data. Similar to OpenCV's <b>highgui</b> routines for displaying 
     2D images and for drawing basic 2D shapes on screen, the library offers:
   
     <ul>
     <li> methods for rendering and setting visual properties (colors, point sizes, opacity, etc) for any n-D point cloud 
          datasets in pcl::PointCloud<T> format;
          \image html http://www.pointclouds.org/documentation/overview/_images/bunny.jpg
     <li> methods for drawing basic 3D shapes on screen (e.g., cylinders, spheres,lines, polygons, etc) either from sets 
          of points or from parametric equations;
          \image html http://www.pointclouds.org/documentation/overview/_images/shapes.jpg
     <li> a histogram visualization module (PCLHistogramVisualizer) for 2D plots;
          \image html http://www.pointclouds.org/documentation/overview/_images/histogram.jpg
     <li> a multitude of Geometry and Color handler for pcl::PointCloud<T> datasets;
          \image html http://www.pointclouds.org/documentation/overview/_images/normals.jpg
          \image html http://www.pointclouds.org/documentation/overview/_images/pcs.jpg
     <li> a pcl::RangeImage visualization module.
          \image html http://www.pointclouds.org/documentation/overview/_images/range_image.jpg
     </ul>
   
     The package makes use of the VTK library for 3D rendering for range image and 2D operations.
   
     For implementing your own visualizers, take a look at the tests and examples accompanying the library.
     
     \section secVisualizationRequirements Requirements
     - \ref common "common"
     - VTK
     - \ref io "io"
     - \ref kdtree "kdtree"
     - \ref pcl::RangeImage "RangeImage"
   
   */
