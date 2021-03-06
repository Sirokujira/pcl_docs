
.. _program_listing_file_pcl_outofcore_include_pcl_outofcore_outofcore_depth_first_iterator.h:

Program Listing for File outofcore_depth_first_iterator.h
=========================================================

|exhale_lsh| :ref:`Return to documentation for file <file_pcl_outofcore_include_pcl_outofcore_outofcore_depth_first_iterator.h>` (``pcl\outofcore\include\pcl\outofcore\outofcore_depth_first_iterator.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   /*
    * Software License Agreement (BSD License)
    *
    *  Point Cloud Library (PCL) - www.pointclouds.org
    *  Copyright (c) 2010-2012, Willow Garage, Inc.
    *
    *  All rights reserved.
    *
    *  Redistribution and use in source and binary forms, with or without
    *  modification, are permitted provided that the following conditions
    *  are met:
    *
    *   * Redistributions of source code must retain the above copyright
    *     notice, this list of conditions and the following disclaimer.
    *   * Redistributions in binary form must reproduce the above
    *     copyright notice, this list of conditions and the following
    *     disclaimer in the documentation and/or other materials provided
    *     with the distribution.
    *   * Neither the name of Willow Garage, Inc. nor the names of its
    *     contributors may be used to endorse or promote products derived
    *     from this software without specific prior written permission.
    *
    *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
    *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    *  POSSIBILITY OF SUCH DAMAGE.
    *
    * $Id$
    */
   
   #ifndef PCL_OUTOFCORE_DEPTH_FIRST_ITERATOR_H_
   #define PCL_OUTOFCORE_DEPTH_FIRST_ITERATOR_H_
   
   #include <pcl/outofcore/outofcore_iterator_base.h>
   namespace pcl
   {
     namespace outofcore
     {
       /** \class OutofcoreDepthFirstIterator
        *
        *  \ingroup outofcore
        *  \author Stephen Fox (foxstephend@gmail.com)
        *  \note Code adapted from \ref octree_iterator.h in Module \ref pcl::octree written by Julius Kammerl
        */
       template<typename PointT=pcl::PointXYZ, typename ContainerT=OutofcoreOctreeDiskContainer<pcl::PointXYZ> >
       class OutofcoreDepthFirstIterator : public OutofcoreIteratorBase<PointT, ContainerT>
       {
         public:
           typedef typename pcl::outofcore::OutofcoreOctreeBase<ContainerT, PointT> OctreeDisk;
           typedef typename pcl::outofcore::OutofcoreOctreeBaseNode<ContainerT, PointT> OctreeDiskNode;
   
           typedef typename pcl::outofcore::OutofcoreOctreeBaseNode<ContainerT, PointT> LeafNode;
           typedef typename pcl::outofcore::OutofcoreOctreeBaseNode<ContainerT, PointT> BranchNode;
   
           explicit
           OutofcoreDepthFirstIterator (OctreeDisk& octree_arg);
   
           virtual
           ~OutofcoreDepthFirstIterator ();
         
           OutofcoreDepthFirstIterator&
           operator++ ();
         
           inline OutofcoreDepthFirstIterator
           operator++ (int)
           {
             OutofcoreDepthFirstIterator _Tmp = *this;
             ++*this;
             return (_Tmp);
           }
         
           void
           skipChildVoxels ();
         
         protected:
           unsigned char currentChildIdx_;
           std::vector<std::pair<OctreeDiskNode*, unsigned char> > stack_;
       };
     }
   }
   
   #endif //PCL_OUTOFCORE_DEPTH_FIRST_ITERATOR_H_
