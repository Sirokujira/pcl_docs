.. _exhale_struct_structpcl_1_1detail_1_1_copy_point_helper_3_01_point_in_t_00_01_point_out_t_00_01typename_01boos298cad4992871f48d657cbf32cc4fd8b:

Template Struct CopyPointHelper< PointInT, PointOutT, typename boost::enable_if< boost::mpl::and_< boost::mpl::not_< boost::is_same< PointInT, PointOutT > >, boost::mpl::or_< boost::mpl::not_< pcl::traits::has_color< PointInT > >, boost::mpl::not_< pcl::traits::has_color< PointOutT > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgb >, pcl::traits::has_field< PointOutT, pcl::fields::rgb > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgba >, pcl::traits::has_field< PointOutT, pcl::fields::rgba > > > > >::type >
================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

- Defined in :ref:`file_pcl_common_include_pcl_common_impl_copy_point.hpp`


Struct Documentation
--------------------


.. doxygenstruct:: pcl::detail::CopyPointHelper< PointInT, PointOutT, typename boost::enable_if< boost::mpl::and_< boost::mpl::not_< boost::is_same< PointInT, PointOutT > >, boost::mpl::or_< boost::mpl::not_< pcl::traits::has_color< PointInT > >, boost::mpl::not_< pcl::traits::has_color< PointOutT > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgb >, pcl::traits::has_field< PointOutT, pcl::fields::rgb > >, boost::mpl::and_< pcl::traits::has_field< PointInT, pcl::fields::rgba >, pcl::traits::has_field< PointOutT, pcl::fields::rgba > > > > >::type >
   :members:
   :protected-members:
   :undoc-members: