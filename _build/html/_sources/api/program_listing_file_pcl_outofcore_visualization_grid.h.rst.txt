
.. _program_listing_file_pcl_outofcore_visualization_grid.h:

Program Listing for File grid.h
===============================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_visualization_grid.h>` (``pcl\outofcore\visualization\grid.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   // C++
   #include <iostream>
   #include <string>
   
   // PCL
   #include "geometry.h"
   #include "object.h"
   
   // VTK
   #include <vtkActor.h>
   #include <vtkRectilinearGrid.h>
   #include <vtkDataSetMapper.h>
   #include <vtkDoubleArray.h>
   #include <vtkPolyData.h>
   #include <vtkSmartPointer.h>
   
   //class Grid : public Geometry
   class Grid : public Object
   {
   public:
   
     // Operators
     // -----------------------------------------------------------------------------
     Grid (std::string name, int size = 10, double spacing = 1.0);
     ~Grid () { }
   
     // Accessors
     // -----------------------------------------------------------------------------
     inline vtkSmartPointer<vtkRectilinearGrid>
     getGrid () const
     {
       return grid_;
     }
   
   //  virtual vtkSmartPointer<vtkActor>
     vtkSmartPointer<vtkActor>
     getGridActor () const
     {
       return grid_actor_;
     }
   
   private:
   
     // Members
     // -----------------------------------------------------------------------------
     vtkSmartPointer<vtkRectilinearGrid> grid_;
     vtkSmartPointer<vtkActor> grid_actor_;
   
   };
