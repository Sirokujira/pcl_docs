
.. _program_listing_file_pcl_tracking_include_pcl_tracking_impl_distance_coherence.hpp:

Program Listing for File distance_coherence.hpp
===============================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_tracking_include_pcl_tracking_impl_distance_coherence.hpp>` (``pcl\tracking\include\pcl\tracking\impl\distance_coherence.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_TRACKING_IMPL_DISTANCE_COHERENCE_H_
   #define PCL_TRACKING_IMPL_DISTANCE_COHERENCE_H_
   
   #include <Eigen/Dense>
   #include <pcl/tracking/distance_coherence.h>
   
   namespace pcl
   {
     namespace tracking
     {
       template <typename PointInT> double
       DistanceCoherence<PointInT>::computeCoherence (PointInT &source, PointInT &target)
       {
          Eigen::Vector4f p = source.getVector4fMap ();
          Eigen::Vector4f p_dash = target.getVector4fMap ();
          double d = (p - p_dash).norm ();
          return 1.0 / (1.0 + d * d * weight_);
       }
     }
   }
   
   #define PCL_INSTANTIATE_DistanceCoherence(T) template class PCL_EXPORTS pcl::tracking::DistanceCoherence<T>;
   
   #endif
