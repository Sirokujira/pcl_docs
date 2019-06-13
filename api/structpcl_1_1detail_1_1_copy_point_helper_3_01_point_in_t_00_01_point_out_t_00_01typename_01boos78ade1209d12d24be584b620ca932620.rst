.. _exhale_struct_structpcl_1_1detail_1_1_copy_point_helper_3_01_point_in_t_00_01_point_out_t_00_01typename_01boos78ade1209d12d24be584b620ca932620:

Template Struct CopyPointHelper< PointInT, PointOutT, typename boost::enable_if< boost::mpl::and_< boost::mpl::not_< boost::is_same< PointInT, PointOutT > >, boost::mpl::or_< boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgb >, pcl::traits::has_field< PointOutT, pcl::fields::rgba > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgba >, pcl::traits::has_field< PointOutT, pcl::fields::rgb > > > > >::type >
===============================================================================================================================================================================================================================================================================================================================================================================================================================================================

- Defined in :ref:`file_pcl_common_include_pcl_common_impl_copy_point.hpp`


Struct Documentation
--------------------


.. doxygenstruct:: pcl::detail::CopyPointHelper< PointInT, PointOutT, typename boost::enable_if< boost::mpl::and_< boost::mpl::not_< boost::is_same< PointInT, PointOutT > >, boost::mpl::or_< boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgb >, pcl::traits::has_field< PointOutT, pcl::fields::rgba > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgba >, pcl::traits::has_field< PointOutT, pcl::fields::rgb > > > > >::type >
   :members:
   :protected-members:
   :undoc-members: