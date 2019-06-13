
.. _program_listing_file_pcl_outofcore_include_pcl_outofcore_visualization_object.h:

Program Listing for File object.h
=================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_include_pcl_outofcore_visualization_object.h>` (``pcl\outofcore\include\pcl\outofcore\visualization\object.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef PCL_OUTOFCORE_OBJECT_H_
   #define PCL_OUTOFCORE_OBJECT_H_
   
   // C++
   #include <map>
   #include <set>
   #include <string>
   
   // VTK
   #include <vtkActor.h>
   #include <vtkActorCollection.h>
   #include <vtkRenderer.h>
   #include <vtkSmartPointer.h>
   
   // Boost
   //#include <boost/date_time.hpp>
   //#include <boost/filesystem.hpp>
   #include <boost/thread.hpp>
   
   //Forward Declaration
   class Scene;
   
   class Object
   {
   public:
   
     // Operators
     // -----------------------------------------------------------------------------
     Object (std::string name);
   
     virtual
     ~Object () { }
   
   
     // Accessors
     // -----------------------------------------------------------------------------
     std::string
     getName () const;
   
     void
     setName (std::string name);
   
     virtual void
     render (vtkRenderer* renderer);
   
     bool
     hasActor (vtkActor *actor);
   
     void
     addActor (vtkActor *actor);
   
     void
     removeActor (vtkActor *actor);
   
     vtkSmartPointer<vtkActorCollection>
     getActors ();
   
   protected:
     vtkSmartPointer<vtkActorCollection> actors_;
     boost::mutex actors_mutex_;
   
   private:
   
     // Members
     // -----------------------------------------------------------------------------
     std::string name_;
     std::map<vtkActor*, std::set<vtkRenderer*> > associated_renderers_;
   
   };
   
   #endif
