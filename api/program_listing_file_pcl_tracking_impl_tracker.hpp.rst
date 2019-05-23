
.. _program_listing_file_pcl_tracking_impl_tracker.hpp:

Program Listing for File tracker.hpp
====================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_tracking_impl_tracker.hpp>` (``pcl\tracking\impl\tracker.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_TRACKING_IMPL_TRACKER_H_
   #define PCL_TRACKING_IMPL_TRACKER_H_
   
   #include <pcl/common/eigen.h>
   #include <ctime>
   #include <pcl/tracking/tracker.h>
   
   template <typename PointInT, typename StateT> bool
   pcl::tracking::Tracker<PointInT, StateT>::initCompute ()
   {
     if (!PCLBase<PointInT>::initCompute ())
     {
       PCL_ERROR ("[pcl::%s::initCompute] PCLBase::Init failed.\n", getClassName ().c_str ());
       return (false);
     }
   
     // If the dataset is empty, just return
     if (input_->points.empty ())
     {
       PCL_ERROR ("[pcl::%s::compute] input_ is empty!\n", getClassName ().c_str ());
       // Cleanup
       deinitCompute ();
       return (false);
     }
   
     return (true);
   }
   
   template <typename PointInT, typename StateT> void
   pcl::tracking::Tracker<PointInT, StateT>::compute ()
   {
     if (!initCompute ())
       return;
     
     computeTracking ();
     deinitCompute ();
   }
   
   #endif
