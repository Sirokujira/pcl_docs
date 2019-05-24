
.. _program_listing_file_pcl_docs_source_pcl_kdtree_kdtree.doxy:

Program Listing for File kdtree.doxy
====================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_source_pcl_kdtree_kdtree.doxy>` (``pcl_docs\source\pcl\kdtree\kdtree.doxy``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /**
     \addtogroup kdtree Module kdtree
   
     \section secKDtreePresentation Overview 
   
     The <b>pcl_kdtree</b> library provides the kd-tree data-structure, using
     <a href="http://www.cs.ubc.ca/research/flann/</a>,
     that allows for fast <a href="http://en.wikipedia.org/wiki/Nearest_neighbor_search">nearest neighbor searches</a>.
   
     A <a href="http://en.wikipedia.org/wiki/Kd-tree">Kd-tree</a> (<i>k</i>-dimensional tree) is a space-partitioning data 
     structure that stores a set of k-dimensional points in a tree structure that enables efficient range searches and 
     nearest neighbor searches. Nearest neighbor searches are a core operation when working with point cloud data and can 
     be used to find correspondences between groups of points or feature descriptors or to define the local neighborhood 
     around a point or points.
   
     \image html http://www.pointclouds.org/assets/images/contents/documentation/kdtree_mug.png
     
     \section secKDtreeRequirements Requirements
     - \ref common "common"
   
   */
