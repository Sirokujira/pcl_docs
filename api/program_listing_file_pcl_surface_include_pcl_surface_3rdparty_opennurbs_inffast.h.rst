
.. _program_listing_file_pcl_surface_include_pcl_surface_3rdparty_opennurbs_inffast.h:

Program Listing for File inffast.h
==================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_surface_include_pcl_surface_3rdparty_opennurbs_inffast.h>` (``pcl\surface\include\pcl\surface\3rdparty\opennurbs\inffast.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /* inffast.h -- header to use inffast.c
    * Copyright (C) 1995-2003 Mark Adler
    * For conditions of distribution and use, see copyright notice in zlib.h
    */
   
   /* WARNING: this file should *not* be used by applications. It is
      part of the implementation of the compression library and is
      subject to change. Applications should only use zlib.h.
    */
   
   void inflate_fast OF((z_streamp strm, unsigned start));
