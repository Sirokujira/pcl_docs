
.. _program_listing_file_pcl_docs_source_pcl_doc_tutorials_content_sources_qt_visualizer_pclviewer.h:

Program Listing for File pclviewer.h
====================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_source_pcl_doc_tutorials_content_sources_qt_visualizer_pclviewer.h>` (``pcl_docs\source\pcl\doc\tutorials\content\sources\qt_visualizer\pclviewer.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <iostream>
   
   // Qt
   #include <QMainWindow>
   
   // Point Cloud Library
   #include <pcl/point_cloud.h>
   #include <pcl/point_types.h>
   #include <pcl/visualization/pcl_visualizer.h>
   
   // Visualization Toolkit (VTK)
   #include <vtkRenderWindow.h>
   
   typedef pcl::PointXYZRGBA PointT;
   typedef pcl::PointCloud<PointT> PointCloudT;
   
   namespace Ui
   {
     class PCLViewer;
   }
   
   class PCLViewer : public QMainWindow
   {
     Q_OBJECT
   
   public:
     explicit PCLViewer (QWidget *parent = 0);
     ~PCLViewer ();
   
   public Q_SLOTS:
     void
     randomButtonPressed ();
   
     void
     RGBsliderReleased ();
   
     void
     pSliderValueChanged (int value);
   
     void
     redSliderValueChanged (int value);
   
     void
     greenSliderValueChanged (int value);
   
     void
     blueSliderValueChanged (int value);
   
   protected:
     pcl::visualization::PCLVisualizer::Ptr viewer;
     PointCloudT::Ptr cloud;
   
     unsigned int red;
     unsigned int green;
     unsigned int blue;
   
   private:
     Ui::PCLViewer *ui;
   
   };
