
.. _program_listing_file_pcl_outofcore_visualization_common.h:

Program Listing for File common.h
=================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_visualization_common.h>` (``pcl\outofcore\visualization\common.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   // VTK
   #include <vtkPolyData.h>
   #include <vtkSmartPointer.h>
   
   vtkSmartPointer<vtkPolyData>
   getVtkCube (double x_min, double x_max, double y_min, double y_max, double z_min, double z_max);
