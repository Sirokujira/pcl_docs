
.. _file_pcl_common_include_pcl_common_common.h:

File common.h
=============

|exhale_lsh| :ref:`Parent directory <dir_pcl_common_include_pcl_common>` (``pcl\common\include\pcl\common``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS


Define standard C methods and C++ classes that are common to all methods. 
 

.. contents:: Contents
   :local:
   :backlinks: none

Definition (``pcl\common\include\pcl\common\common.h``)
-------------------------------------------------------


.. toctree::
   :maxdepth: 1

   program_listing_file_pcl_common_include_pcl_common_common.h.rst





Includes
--------


- ``cfloat``

- ``pcl/common/impl/common.hpp``

- ``pcl/pcl_base.h``



Included By
-----------


- :ref:`file_pcl_common_include_pcl_common_common_headers.h`

- :ref:`file_pcl_common_include_pcl_common_distances.h`

- :ref:`file_pcl_common_include_pcl_common_impl_common.hpp`

- :ref:`file_pcl_common_include_pcl_common_intersections.h`

- :ref:`file_pcl_features_include_pcl_features_cvfh.h`

- :ref:`file_pcl_features_include_pcl_features_gasd.h`

- :ref:`file_pcl_features_include_pcl_features_impl_crh.hpp`

- :ref:`file_pcl_features_include_pcl_features_impl_esf.hpp`

- :ref:`file_pcl_features_include_pcl_features_impl_vfh.hpp`

- :ref:`file_pcl_features_include_pcl_features_our_cvfh.h`

- :ref:`file_pcl_filters_include_pcl_filters_impl_approximate_voxel_grid.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_grid_minimum.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_morphological_filter.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_uniform_sampling.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_voxel_grid.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_voxel_grid_covariance.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_impl_voxel_grid_occlusion_estimation.hpp`

- :ref:`file_pcl_gpu_features_test_data_source.hpp`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_label_segment.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_label_tree.h`

- :ref:`file_pcl_io_include_pcl_compression_impl_organized_pointcloud_compression.hpp`

- :ref:`file_pcl_io_include_pcl_compression_libpng_wrapper.h`

- :ref:`file_pcl_io_include_pcl_compression_octree_pointcloud_compression.h`

- :ref:`file_pcl_io_include_pcl_compression_organized_pointcloud_compression.h`

- :ref:`file_pcl_ml_include_pcl_ml_branch_estimator.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_forest.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_forest_evaluator.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_forest_trainer.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_tree.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_tree_data_provider.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_tree_evaluator.h`

- :ref:`file_pcl_ml_include_pcl_ml_dt_decision_tree_trainer.h`

- :ref:`file_pcl_ml_include_pcl_ml_feature_handler.h`

- :ref:`file_pcl_ml_include_pcl_ml_ferns_fern.h`

- :ref:`file_pcl_ml_include_pcl_ml_ferns_fern_evaluator.h`

- :ref:`file_pcl_ml_include_pcl_ml_ferns_fern_trainer.h`

- :ref:`file_pcl_ml_include_pcl_ml_impl_dt_decision_forest_evaluator.hpp`

- :ref:`file_pcl_ml_include_pcl_ml_impl_dt_decision_tree_evaluator.hpp`

- :ref:`file_pcl_ml_include_pcl_ml_impl_ferns_fern_evaluator.hpp`

- :ref:`file_pcl_ml_include_pcl_ml_multi_channel_2d_comparison_feature.h`

- :ref:`file_pcl_ml_include_pcl_ml_multi_channel_2d_comparison_feature_handler.h`

- :ref:`file_pcl_ml_include_pcl_ml_multi_channel_2d_data_set.h`

- :ref:`file_pcl_ml_include_pcl_ml_multiple_data_2d_example_index.h`

- :ref:`file_pcl_ml_include_pcl_ml_point_xy_32f.h`

- :ref:`file_pcl_ml_include_pcl_ml_point_xy_32i.h`

- :ref:`file_pcl_ml_include_pcl_ml_regression_variance_stats_estimator.h`

- :ref:`file_pcl_ml_include_pcl_ml_stats_estimator.h`

- :ref:`file_pcl_octree_include_pcl_octree_impl_octree_pointcloud.hpp`

- :ref:`file_pcl_outofcore_include_pcl_outofcore_impl_octree_base_node.hpp`

- :ref:`file_pcl_recognition_include_pcl_recognition_crh_alignment.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_face_detection_face_detector_data_provider.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_hv_greedy_verification.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_hv_hv_go.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_hv_hv_papazov.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_hv_hypotheses_verification.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_hv_occlusion_reasoning.h`

- :ref:`file_pcl_registration_include_pcl_registration_ia_fpcs.h`

- :ref:`file_pcl_registration_include_pcl_registration_matching_candidate.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_impl_sac_model_parallel_line.hpp`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_sac_model_cone.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_sac_model_cylinder.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_sac_model_normal_sphere.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_sac_model_parallel_plane.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_sac_model_perpendicular_plane.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_approximate_progressive_morphological_filter.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_lccp_segmentation.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_progressive_morphological_filter.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_concave_hull.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_convex_hull.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_grid_projection.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_marching_cubes.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_marching_cubes_hoppe.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_marching_cubes_rbf.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_impl_poisson.hpp`

- :ref:`file_pcl_surface_include_pcl_surface_mls.h`

- :ref:`file_pcl_tracking_include_pcl_tracking_impl_normal_coherence.hpp`

- :ref:`file_pcl_tracking_include_pcl_tracking_impl_particle_filter.hpp`




Namespaces
----------


- :ref:`namespace_pcl`


Functions
---------


- :ref:`exhale_function_group__common_1ga1a9e18520c49be76f2a28834e2da8a56`

- :ref:`exhale_function_group__common_1ga8c74d7c459961a2650c22eff8126aef8`

- :ref:`exhale_function_group__common_1ga54999c02ba9bee56404539747b0fda51`

- :ref:`exhale_function_group__common_1gab64d6ba9e834d29feda71a76d3ec841f`

- :ref:`exhale_function_group__common_1ga1583a71aef0f54550adef0ebfef89edd`

- :ref:`exhale_function_group__common_1gab5669ac9649b383c053ef67cc06e6b55`

- :ref:`exhale_function_group__common_1ga3349ce9c26d4acbb1adae1e9b2d5f7e5`

- :ref:`exhale_function_group__common_1gacb684087702126b29c8b99f1e2c2786b`

- :ref:`exhale_function_group__common_1gaacff2e632283be60810678d329b166ec`

- :ref:`exhale_function_group__common_1ga287e6ce2d4be348c059baf31eaf2dd54`

- :ref:`exhale_function_group__common_1ga3166f09aafd659f69dc75e63f5e10f81`

- :ref:`exhale_function_group__common_1gafd9010977f5e52b35b484be7624df3f8`

- :ref:`exhale_function_group__common_1ga47dac23a8a283dd07f62fa7aa21b63ec`

- :ref:`exhale_function_group__common_1ga41eb246206d51f77a8cb82b5d963e6a2`

- :ref:`exhale_function_group__common_1gab831a44b375fa7e6bada740d1d17e247`

