
.. _program_listing_file_pcl_outofcore_outofcore.doxy:

Program Listing for File outofcore.doxy
=======================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_outofcore.doxy>` (``pcl\outofcore\outofcore.doxy``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /**
     \addtogroup outofcore Module outofcore
   
     \section secOutofcoreOctree Overview
     
     The <b>pcl_outofcore</b> library provides an octree data structure
     for point clouds that are too large to be stored in main memory. The
     data are located instead in an directory-based octree hierary on
     some secondary storage (disk) medium. <b>pcl_outofcore</b> provides
     the framework for constructing and traversing outofcore octrees, a
     command-line tool <b>pcl_outofcore_process</b> for converting a set
     of registered PCD files to outofcore octree, and
     <b>pcl_outofcore_viewer</b> for rendering outofcore octrees.
   
     <b>pcl_outofcore</b> provides an interface to construct and query
     outofcore octrees via OutofcoreOctreeBase. The out of core octree
     can be used with any PCLPointCloud2 with point types containing ``x'',
     ``y'' and ``z'' fields. No internal checking is done to verify
     this. On the other hand, point clouds do not need to be filtered for
     NaN entries; the library will automatically ignore NaN points in the
     insertion methods.
     
     The average user may not need to do any development with this
     library, but rather use the command-line tool
     <b>pcl_outofcore_process</b> to construct an outofcore octree, and
     <b>pcl_outofcore_viewer</b> to view it.
   
     For those interested in developing software with
     <b>pcl_outofcore</b>, the functionality of the OutofcoreOctreeBase
     class provides methods for insertion (<b>addPointCloud</b>), and
     querying bounding boxes (<b>queryBoundingBox</b>).  Furthermore
     <b>OutofcoreDepthFirstIterator</b> provides an iterator for the
     entire tree that gives direct access to the in-memory node
     datastructre, <b>OutofcoreOctreeBaseNode</b>. Please note that this
     library is still under development, and that interested users should
     use the <b>PCLPointCloud2</b>-based insertion and query methods.
   
     \section secOutofcore Example Usage
   
     \section secOutofcoreRequirements Requirements
     - \ref common "common"
     - \ref io "io"
     - \ref visualization "visualization" (for pcl_outofcore_viewer)
     - \ref filters "filters"
   
   */
