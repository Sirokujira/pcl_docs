
.. _program_listing_file_pcl_docs_pcl_registration_registration.doxy:

Program Listing for File registration.doxy
==========================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_pcl_registration_registration.doxy>` (``pcl_docs\pcl\registration\registration.doxy``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /**
     \addtogroup registration Module registration
   
     \section secRegistrationPresentation Overview
   
   Combining several datasets into a global consistent model is usually performed
   using a technique called registration. The key idea is to identify
   corresponding points between the data sets and find a transformation that
   minimizes the distance (alignment error) between corresponding points. This
   process is repeated, since correspondence search is affected by the relative
   position and orientation of the data sets. Once the alignment errors fall below
   a given threshold, the registration is said to be complete.
   
   The <b>pcl_registration</b> library implements a plethora of point cloud
   registration algorithms for both organized an unorganized (general purpose)
   datasets.
   
   \image html http://www.pointclouds.org/assets/images/contents/documentation/registration_outdoor.png
   \image html http://www.pointclouds.org/assets/images/contents/documentation/registration_closeup.png
   
     \section secRegistrationRequirements Requirements
     - \ref common "common"
     - \ref kdtree "kdtree"
     - \ref sample_consensus "sample_consensus"
     - \ref features "features"
   
   */
