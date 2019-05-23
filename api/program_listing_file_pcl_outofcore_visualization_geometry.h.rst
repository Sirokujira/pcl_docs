
.. _program_listing_file_pcl_outofcore_visualization_geometry.h:

Program Listing for File geometry.h
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_visualization_geometry.h>` (``pcl\outofcore\visualization\geometry.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
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
   
     
     ~Geometry () { }
   
   public:
   
     // Accessors
     // -----------------------------------------------------------------------------
     virtual vtkSmartPointer<vtkActor>
     getActor () const
     {
       std::cout << "Get Geometry Actor" << std::endl;
       return nullptr;
     }
   
   };
