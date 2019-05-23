
.. _program_listing_file_E__pcl_docs_pcl_gpu_tracking_src_cuda_device.hpp:

Program Listing for File device.hpp
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_E__pcl_docs_pcl_gpu_tracking_src_cuda_device.hpp>` (``E:\pcl_docs\pcl\gpu\tracking\src\cuda\device.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_GPU_TRACKING_DEVICE_HPP_
   #define PCL_GPU_TRACKING_DEVICE_HPP_
   
   #include "internal.h"
   
   namespace pcl
   {
     namespace device
     {
       __device__ __forceinline__ float
         getSampleNormal (const float mean, const float cov, curandState* rng_state)
       {
         float rn = curand_normal(rng_state);
         return (rn*cov + mean);
       }
     }
   }
   
   #endif // PCL_GPU_TRACKING_DEVICE_HPP_
