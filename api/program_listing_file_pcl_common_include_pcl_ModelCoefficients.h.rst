
.. _program_listing_file_pcl_common_include_pcl_ModelCoefficients.h:

Program Listing for File ModelCoefficients.h
============================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_common_include_pcl_ModelCoefficients.h>` (``pcl\common\include\pcl\ModelCoefficients.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_MESSAGE_MODELCOEFFICIENTS_H
   #define PCL_MESSAGE_MODELCOEFFICIENTS_H
   #include <string>
   #include <vector>
   #include <ostream>
   
   // Include the correct Header path here
   #include <pcl/PCLHeader.h>
   
   namespace pcl
   {
     struct ModelCoefficients
     {
       ModelCoefficients () : header (), values ()
       {
       }
   
       ::pcl::PCLHeader header;
   
       std::vector<float> values;
   
     public:
       typedef boost::shared_ptr< ::pcl::ModelCoefficients> Ptr;
       typedef boost::shared_ptr< ::pcl::ModelCoefficients  const> ConstPtr;
     }; // struct ModelCoefficients
   
     typedef boost::shared_ptr< ::pcl::ModelCoefficients> ModelCoefficientsPtr;
     typedef boost::shared_ptr< ::pcl::ModelCoefficients const> ModelCoefficientsConstPtr;
   
     inline std::ostream& operator<<(std::ostream& s, const  ::pcl::ModelCoefficients & v)
     {
       s << "header: " << std::endl;
       s << v.header;
       s << "values[]" << std::endl;
       for (size_t i = 0; i < v.values.size (); ++i)
       {
         s << "  values[" << i << "]: ";
         s << "  " << v.values[i] << std::endl;
       }
       return (s);
     }
   
   } // namespace pcl
   
   #endif // PCL_MESSAGE_MODELCOEFFICIENTS_H
   
