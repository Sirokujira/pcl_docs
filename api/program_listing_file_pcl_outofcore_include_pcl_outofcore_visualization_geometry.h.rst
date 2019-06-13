
.. _program_listing_file_pcl_outofcore_include_pcl_outofcore_visualization_geometry.h:

Program Listing for File geometry.h
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_include_pcl_outofcore_visualization_geometry.h>` (``pcl\outofcore\include\pcl\outofcore\visualization\geometry.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_OUTOFCORE_GEOMETRY_H_
   #define PCL_OUTOFCORE_GEOMETRY_H_
   
   // C++
   #include <string>
   
   // PCL
   #include "object.h"
   
   // VTK
   #include <vtkActor.h>
   #include <vtkSmartPointer.h>
   
   class Geometry : public Object
   {
   protected:
   
     // Operators
     // -----------------------------------------------------------------------------
     Geometry (std::string name) :
         Object (name)
     {
     }
   
   public:
   
     virtual
     ~Geometry () { }
   
   public:
   
     // Accessors
     // -----------------------------------------------------------------------------
     virtual vtkSmartPointer<vtkActor>
     getActor () const
     {
       std::cout << "Get Geometry Actor" << std::endl;
       return NULL;
     }
   
   };
   
   #endif
