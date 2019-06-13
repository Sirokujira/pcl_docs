
.. _program_listing_file_pcl_surface_include_pcl_surface_3rdparty_poisson4_hash.h:

Program Listing for File hash.h
===============================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_surface_include_pcl_surface_3rdparty_poisson4_hash.h>` (``pcl\surface\include\pcl\surface\3rdparty\poisson4\hash.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   #ifndef HASH_INCLUDED
   #define HASH_INCLUDED
   #if defined _WIN32 && !defined __MINGW32__
   #define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS
   #include <hash_map>
   using namespace stdext;
   #else // !_WIN32 || __MINGW32__
   #define _GLIBCXX_PERMIT_BACKWARD_HASH
   #include <ext/hash_map>
   using namespace __gnu_cxx;
   
   
   namespace __gnu_cxx
   {
     template<> struct hash<long long> {
       size_t operator()(long long __x) const { return __x; }
     };
     template<> struct hash<const long long> {
       size_t operator()(const long long __x) const { return __x; }
     };
     
     
     template<> struct hash<unsigned long long> {
       size_t operator()(unsigned long long __x) const { return __x; }
     };
     template<> struct hash<const unsigned long long> {
       size_t operator()(const unsigned long long __x) const { return __x; }
     };
   }
   #endif // _WIN32 && !__MINGW32__
   #endif // HASH_INCLUDED
   
