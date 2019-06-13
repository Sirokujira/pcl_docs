
.. _program_listing_file_pcl_outofcore_include_pcl_outofcore_visualization_viewport.h:

Program Listing for File viewport.h
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_include_pcl_outofcore_visualization_viewport.h>` (``pcl\outofcore\include\pcl\outofcore\visualization\viewport.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_OUTOFCORE_VIEWPORT_H_
   #define PCL_OUTOFCORE_VIEWPORT_H_
   
   // C++
   #include <iostream>
   #include <string>
   
   // PCL
   #include "camera.h"
   
   // VTK
   #include <vtkActor.h>
   #include <vtkCallbackCommand.h>
   #include <vtkObject.h>
   #include <vtkTextActor.h>
   #include <vtkRenderer.h>
   #include <vtkRenderWindow.h>
   #include <vtkSmartPointer.h>
   
   class Viewport
   {
   public:
   
     // Operators
     // -----------------------------------------------------------------------------
     Viewport (vtkSmartPointer<vtkRenderWindow> window, double xmin = 0.0, double ymin = 0.0, double xmax = 1.0,
               double ymax = 1.0);
   
     // Accessors
     // -----------------------------------------------------------------------------
     inline vtkSmartPointer<vtkRenderer>
     getRenderer () const
     {
       return renderer_;
     }
   
     void
     setCamera (Camera* camera)
     {
       renderer_->SetActiveCamera (vtkCamera::SafeDownCast (camera->getCamera ()));
       camera_hud_actor_->SetInput (camera->getName ().c_str ());
       renderer_->ResetCamera ();
     }
   
   private:
   
     // Callbacks
     // -----------------------------------------------------------------------------
     static void
     viewportModifiedCallback (vtkObject* caller, unsigned long int vtkNotUsed(eventId), void* vtkNotUsed(clientData),
                               void* vtkNotUsed(callData));
   
     void
     viewportModified ();
   
     static void
     viewportActorUpdateCallback (vtkObject* caller, unsigned long int vtkNotUsed(eventId), void* vtkNotUsed(clientData),
                                  void* vtkNotUsed(callData));
   
     void
     viewportActorUpdate ();
   
     static void
     viewportHudUpdateCallback (vtkObject* caller, unsigned long int vtkNotUsed(eventId), void* vtkNotUsed(clientData),
                                void* vtkNotUsed(callData));
   
     void
     viewportHudUpdate ();
   
     // Members
     // -----------------------------------------------------------------------------
     vtkSmartPointer<vtkRenderer> renderer_;
     vtkSmartPointer<vtkCallbackCommand> viewport_modified_callback_;
     vtkSmartPointer<vtkCallbackCommand> viewport_actor_update_callback_;
     vtkSmartPointer<vtkCallbackCommand> viewport_hud_callback_;
   
     vtkSmartPointer<vtkTextActor> camera_hud_actor_;
     vtkSmartPointer<vtkTextActor> fps_hud_actor_;
     vtkSmartPointer<vtkTextActor> points_hud_actor_;
   };
   
   #endif
