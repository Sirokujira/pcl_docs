
.. _program_listing_file_pcl_gpu_utils_include_pcl_gpu_utils_device_cache.hpp:

Program Listing for File cache.hpp
==================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_gpu_utils_include_pcl_gpu_utils_device_cache.hpp>` (``pcl\gpu\utils\include\pcl\gpu\utils\device\cache.hpp``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   
   
   //will contain a lot of load/store utils
   
   namespace pcl
   {
       namespace device
       {
           template<class T>
           struct NonCachedLoad
           {
               __device__ static T Invoke(const T* ptr)
               {
   
   #if (__CUDA_ARCH__ < 200)
                   return *ptr;
   #else
                   //asm code insertion 
                   asm(...);
   #endif
               }
           };
   
       }
   
   }
