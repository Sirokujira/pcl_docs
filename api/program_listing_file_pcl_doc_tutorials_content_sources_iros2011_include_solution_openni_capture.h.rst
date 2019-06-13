
.. _program_listing_file_pcl_doc_tutorials_content_sources_iros2011_include_solution_openni_capture.h:

Program Listing for File openni_capture.h
=========================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_doc_tutorials_content_sources_iros2011_include_solution_openni_capture.h>` (``pcl\doc\tutorials\content\sources\iros2011\include\solution\openni_capture.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef OPENNI_CAPTURE_H
   #define OPENNI_CAPTURE_H
   
   #include "typedefs.h"
   
   #include <pcl/io/openni_grabber.h>
   #include <pcl/visualization/pcl_visualizer.h>
   
   /* A simple class for capturing data from an OpenNI camera */
   class OpenNICapture
   {
     public:
       OpenNICapture (const std::string& device_id = "");
       ~OpenNICapture ();
       
       void setTriggerMode (bool use_trigger);
       const PointCloudPtr snap ();
       const PointCloudPtr snapAndSave (const std::string & filename);
   
     protected:
       void onNewFrame (const PointCloudConstPtr &cloud);
       void onKeyboardEvent (const pcl::visualization::KeyboardEvent & event);
   
       void waitForTrigger ();
   
       pcl::OpenNIGrabber grabber_;
       boost::shared_ptr<pcl::visualization::PCLVisualizer> preview_;
       int frame_counter_;
       PointCloudPtr most_recent_frame_;
       bool use_trigger_, trigger_;
       boost::mutex mutex_;
   };
   
   #endif
