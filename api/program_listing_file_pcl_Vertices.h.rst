
.. _program_listing_file_pcl_Vertices.h:

Program Listing for File Vertices.h
===================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_Vertices.h>` (``pcl\Vertices.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <string>
   #include <vector>
   #include <ostream>
   #include <boost/shared_ptr.hpp>
   #include <pcl/pcl_macros.h>
   
   namespace pcl
   {
     /** \brief Describes a set of vertices in a polygon mesh, by basically
       * storing an array of indices.
       */
     struct Vertices
     {
       Vertices ()
       {}
   
       std::vector<uint32_t> vertices;
   
     public:
       typedef boost::shared_ptr<Vertices> Ptr;
       typedef boost::shared_ptr<Vertices const> ConstPtr;
     }; // struct Vertices
   
   
     typedef boost::shared_ptr<Vertices> VerticesPtr;
     typedef boost::shared_ptr<Vertices const> VerticesConstPtr;
   
     inline std::ostream& operator<<(std::ostream& s, const  ::pcl::Vertices & v)
     {
       s << "vertices[]" << std::endl;
       for (size_t i = 0; i < v.vertices.size (); ++i)
       {
         s << "  vertices[" << i << "]: ";
         s << "  " << v.vertices[i] << std::endl;
       }
       return (s);
     }
   } // namespace pcl
