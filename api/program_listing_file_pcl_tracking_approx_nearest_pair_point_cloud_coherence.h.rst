
.. _program_listing_file_pcl_tracking_approx_nearest_pair_point_cloud_coherence.h:

Program Listing for File approx_nearest_pair_point_cloud_coherence.h
====================================================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_tracking_approx_nearest_pair_point_cloud_coherence.h>` (``pcl\tracking\approx_nearest_pair_point_cloud_coherence.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <pcl/search/search.h>
   #include <pcl/search/octree.h>
   #include <pcl/tracking/nearest_pair_point_cloud_coherence.h>
   namespace pcl
   {
     namespace tracking
     {
       /** \brief @b ApproxNearestPairPointCloudCoherence computes coherence between two pointclouds using the
            approximate nearest point pairs.
         * \author Ryohei Ueda
         * \ingroup tracking
         */
       template <typename PointInT>
       class ApproxNearestPairPointCloudCoherence: public NearestPairPointCloudCoherence<PointInT>
       {
       public:
         typedef typename NearestPairPointCloudCoherence<PointInT>::PointCoherencePtr PointCoherencePtr;
         typedef typename NearestPairPointCloudCoherence<PointInT>::PointCloudInConstPtr PointCloudInConstPtr;
         //using NearestPairPointCloudCoherence<PointInT>::search_;
         using NearestPairPointCloudCoherence<PointInT>::maximum_distance_;
         using NearestPairPointCloudCoherence<PointInT>::target_input_;
         using NearestPairPointCloudCoherence<PointInT>::point_coherences_;
         using NearestPairPointCloudCoherence<PointInT>::coherence_name_;
         using NearestPairPointCloudCoherence<PointInT>::new_target_;
         using NearestPairPointCloudCoherence<PointInT>::getClassName;
         
         /** \brief empty constructor */
         ApproxNearestPairPointCloudCoherence () : 
           NearestPairPointCloudCoherence<PointInT> (), search_ ()
         {
           coherence_name_ = "ApproxNearestPairPointCloudCoherence";
         }
         
       protected:
         /** \brief This method should get called before starting the actual computation. */
         bool initCompute () override;
         
         /** \brief compute the nearest pairs and compute coherence using point_coherences_ */
         void
         computeCoherence (const PointCloudInConstPtr &cloud, const IndicesConstPtr &indices, float &w_j) override;
   
         typename pcl::search::Octree<PointInT>::Ptr search_;
       };
     }
   }
   
   #ifdef PCL_NO_PRECOMPILE
   #include <pcl/tracking/impl/approx_nearest_pair_point_cloud_coherence.hpp>
   #endif
