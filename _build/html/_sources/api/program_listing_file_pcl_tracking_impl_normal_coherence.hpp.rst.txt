
.. _program_listing_file_pcl_tracking_impl_normal_coherence.hpp:

Program Listing for File normal_coherence.hpp
=============================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_tracking_impl_normal_coherence.hpp>` (``pcl\tracking\impl\normal_coherence.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_TRACKING_IMPL_NORMAL_COHERENCE_H_
   #define PCL_TRACKING_IMPL_NORMAL_COHERENCE_H_
   
   #include <pcl/common/common.h>
   #include <pcl/console/print.h>
   #include <pcl/tracking/normal_coherence.h>
   
   template <typename PointInT> double 
   pcl::tracking::NormalCoherence<PointInT>::computeCoherence (PointInT &source, PointInT &target)
   {
       Eigen::Vector4f n = source.getNormalVector4fMap ();
       Eigen::Vector4f n_dash = target.getNormalVector4fMap ();
       if ( n.norm () <= 1e-5 || n_dash.norm () <= 1e-5 )
       {
           PCL_ERROR("norm might be ZERO!\n");
           std::cout << "source: " << source << std::endl;
           std::cout << "target: " << target << std::endl;
           exit (1);
           return 0.0;
       }
       else
       {
           n.normalize ();
           n_dash.normalize ();
           double theta = pcl::getAngle3D (n, n_dash);
           if (!std::isnan (theta))
               return 1.0 / (1.0 + weight_ * theta * theta);
           else
               return 0.0;
       }
   }
   
   
   #define PCL_INSTANTIATE_NormalCoherence(T) template class PCL_EXPORTS pcl::tracking::NormalCoherence<T>;
   
   #endif
