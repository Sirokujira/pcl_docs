
.. _program_listing_file_pcl_docs_source_pcl_gpu_people_include_pcl_gpu_people_person_attribs.h:

Program Listing for File person_attribs.h
=========================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_docs_source_pcl_gpu_people_include_pcl_gpu_people_person_attribs.h>` (``pcl_docs\source\pcl\gpu\people\include\pcl\gpu\people\person_attribs.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #pragma once
   
   #include <string>
   #include <vector>
   #include <iosfwd>
   #include <boost/shared_ptr.hpp>
   
   #include <pcl/pcl_exports.h>
   
   namespace pcl
   {
     namespace gpu
     {
       namespace people
       {
         class PCL_EXPORTS PersonAttribs
         {
           public:
             typedef boost::shared_ptr<PersonAttribs> Ptr;
   
             /** \brief Constructor creates generic values from **/
             PersonAttribs();
   
             /**
              * \brief Read XML configuration file for a specific person
              * \param[in] is input stream of file
              * \return 0 when successful, -1 when an error occurred, datastructure might become corrupted in the process
              **/
             int
             readPersonXMLConfig (std::istream& is);
   
             /**
              * \brief Write XML configuration file for a specific person
              * \param[in] os output stream of file, extension determines format
              **/
             void
             writePersonXMLConfig (std::ostream& os);
   
             std::string                                 name_;                  // Name of the person
             std::vector<float>                          max_part_size_;         // Max primary eigenvalue for each body part
             std::vector<std::vector<float> >            part_ideal_length_;     // Ideal length between two body parts
             std::vector<std::vector<float> >            max_length_offset_;     // Max allowed length offset between two body parts
             std::vector<int>                            nr_of_children_;        // The number of children for each part
         };
       }
     }
   }
