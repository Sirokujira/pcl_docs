
.. _file_pcl_common_include_pcl_point_types.h:

File point_types.h
==================

|exhale_lsh| :ref:`Parent directory <dir_pcl_common_include_pcl>` (``pcl\common\include\pcl``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS


Defines all the PCL implemented PointT point type structures. 
 

.. contents:: Contents
   :local:
   :backlinks: none

Definition (``pcl\common\include\pcl\point_types.h``)
-----------------------------------------------------


.. toctree::
   :maxdepth: 1

   program_listing_file_pcl_common_include_pcl_point_types.h.rst





Includes
--------


- ``bitset``

- ``boost/mpl/contains.hpp``

- ``boost/mpl/fold.hpp``

- ``boost/mpl/vector.hpp``

- ``pcl/impl/point_types.hpp``

- ``pcl/pcl_macros.h``

- ``pcl/register_point_struct.h``



Included By
-----------


- :ref:`file_pcl_2d_include_pcl_2d_convolution.h`

- :ref:`file_pcl_2d_include_pcl_2d_kernel.h`

- :ref:`file_pcl_common_include_pcl_common_colors.h`

- :ref:`file_pcl_common_include_pcl_common_generate.h`

- :ref:`file_pcl_common_include_pcl_common_impl_accumulators.hpp`

- :ref:`file_pcl_common_include_pcl_common_impl_common.hpp`

- :ref:`file_pcl_common_include_pcl_common_impl_copy_point.hpp`

- :ref:`file_pcl_common_include_pcl_common_impl_intensity.hpp`

- :ref:`file_pcl_common_include_pcl_common_impl_io.hpp`

- :ref:`file_pcl_common_include_pcl_common_impl_pca.hpp`

- :ref:`file_pcl_common_include_pcl_common_transforms.h`

- :ref:`file_pcl_common_include_pcl_point_representation.h`

- :ref:`file_pcl_common_include_pcl_point_types_conversion.h`

- :ref:`file_pcl_common_include_pcl_range_image_bearing_angle_image.h`

- :ref:`file_pcl_common_include_pcl_range_image_range_image.h`

- :ref:`file_pcl_cuda_nn_organized_neighbor_search.h`

- :ref:`file_pcl_doc_tutorials_content_sources_iccv2011_include_typedefs.h`

- :ref:`file_pcl_doc_tutorials_content_sources_iros2011_include_typedefs.h`

- :ref:`file_pcl_doc_tutorials_content_sources_iros2011_include_solution_typedefs.h`

- :ref:`file_pcl_doc_tutorials_content_sources_qt_colorize_cloud_pclviewer.h`

- :ref:`file_pcl_doc_tutorials_content_sources_qt_visualizer_pclviewer.h`

- :ref:`file_pcl_features_include_pcl_features_3dsc.h`

- :ref:`file_pcl_features_include_pcl_features_board.h`

- :ref:`file_pcl_features_include_pcl_features_flare.h`

- :ref:`file_pcl_features_include_pcl_features_impl_spin_image.hpp`

- :ref:`file_pcl_features_include_pcl_features_integral_image_normal.h`

- :ref:`file_pcl_features_include_pcl_features_linear_least_squares_normal.h`

- :ref:`file_pcl_features_include_pcl_features_narf_descriptor.h`

- :ref:`file_pcl_features_include_pcl_features_pfh.h`

- :ref:`file_pcl_features_include_pcl_features_range_image_border_extractor.h`

- :ref:`file_pcl_features_include_pcl_features_shot.h`

- :ref:`file_pcl_features_include_pcl_features_shot_lrf.h`

- :ref:`file_pcl_features_include_pcl_features_shot_lrf_omp.h`

- :ref:`file_pcl_features_include_pcl_features_shot_omp.h`

- :ref:`file_pcl_features_include_pcl_features_spin_image.h`

- :ref:`file_pcl_features_include_pcl_features_usc.h`

- :ref:`file_pcl_features_include_pcl_features_vfh.h`

- :ref:`file_pcl_filters_include_pcl_filters_crop_box.h`

- :ref:`file_pcl_filters_include_pcl_filters_crop_hull.h`

- :ref:`file_pcl_filters_include_pcl_filters_frustum_culling.h`

- :ref:`file_pcl_filters_include_pcl_filters_impl_convolution_3d.hpp`

- :ref:`file_pcl_filters_include_pcl_filters_project_inliers.h`

- :ref:`file_pcl_filters_include_pcl_filters_voxel_grid_covariance.h`

- :ref:`file_pcl_filters_include_pcl_filters_voxel_grid_label.h`

- :ref:`file_pcl_gpu_features_include_pcl_gpu_features_features.hpp`

- :ref:`file_pcl_gpu_features_test_data_source.hpp`

- :ref:`file_pcl_gpu_kinfu_include_pcl_gpu_kinfu_color_volume.h`

- :ref:`file_pcl_gpu_kinfu_include_pcl_gpu_kinfu_kinfu.h`

- :ref:`file_pcl_gpu_kinfu_include_pcl_gpu_kinfu_raycaster.h`

- :ref:`file_pcl_gpu_kinfu_include_pcl_gpu_kinfu_tsdf_volume.h`

- :ref:`file_pcl_gpu_kinfu_tools_tsdf_volume.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_color_volume.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_cyclical_buffer.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_kinfu.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_point_intensity.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_raycaster.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_standalone_marching_cubes.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_tsdf_volume.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_include_pcl_gpu_kinfu_large_scale_world_model.h`

- :ref:`file_pcl_gpu_kinfu_large_scale_tools_color_handler.h`

- :ref:`file_pcl_gpu_octree_include_pcl_gpu_octree_octree.hpp`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_bodyparts_detector.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_colormap.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_face_detector.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_label_segment.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_label_tree.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_organized_plane_detector.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_people_detector.h`

- :ref:`file_pcl_gpu_people_include_pcl_gpu_people_probability_processor.h`

- :ref:`file_pcl_gpu_segmentation_include_pcl_gpu_segmentation_gpu_extract_clusters.h`

- :ref:`file_pcl_gpu_segmentation_include_pcl_gpu_segmentation_gpu_extract_labeled_clusters.h`

- :ref:`file_pcl_gpu_segmentation_include_pcl_gpu_segmentation_gpu_seeded_hue_segmentation.h`

- :ref:`file_pcl_gpu_surface_include_pcl_gpu_surface_convex_hull.h`

- :ref:`file_pcl_gpu_tracking_include_pcl_gpu_tracking_particle_filter.h`

- :ref:`file_pcl_gpu_utils_include_pcl_gpu_utils_repacks.hpp`

- :ref:`file_pcl_io_include_pcl_io_depth_sense_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_dinast_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_hdl_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_impl_vtk_lib_io.hpp`

- :ref:`file_pcl_io_include_pcl_io_png_io.h`

- :ref:`file_pcl_io_include_pcl_io_real_sense_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_robot_eye_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_vlp_grabber.h`

- :ref:`file_pcl_io_include_pcl_io_vtk_lib_io.h`

- :ref:`file_pcl_keypoints_include_pcl_keypoints_agast_2d.h`

- :ref:`file_pcl_keypoints_include_pcl_keypoints_narf_keypoint.h`

- :ref:`file_pcl_ml_include_pcl_ml_densecrf.h`

- :ref:`file_pcl_ml_include_pcl_ml_kmeans.h`

- :ref:`file_pcl_octree_include_pcl_octree_octree_pointcloud.h`

- :ref:`file_pcl_outofcore_include_pcl_outofcore_impl_octree_disk_container.hpp`

- :ref:`file_pcl_outofcore_include_pcl_outofcore_outofcore_iterator_base.h`

- :ref:`file_pcl_outofcore_include_pcl_outofcore_visualization_outofcore_cloud.h`

- :ref:`file_pcl_people_include_pcl_people_ground_based_people_detection_app.h`

- :ref:`file_pcl_people_include_pcl_people_head_based_subcluster.h`

- :ref:`file_pcl_people_include_pcl_people_height_map_2d.h`

- :ref:`file_pcl_people_include_pcl_people_person_cluster.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_cg_hough_3d.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_color_gradient_dot_modality.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_color_gradient_modality.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_color_modality.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_impl_hv_hv_go.hpp`

- :ref:`file_pcl_recognition_include_pcl_recognition_implicit_shape_model.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_point_types.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_ransac_based_auxiliary.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_ransac_based_model_library.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_ransac_based_orr_octree.h`

- :ref:`file_pcl_recognition_include_pcl_recognition_surface_normal_modality.h`

- :ref:`file_pcl_registration_include_pcl_registration_elch.h`

- :ref:`file_pcl_registration_include_pcl_registration_gicp6d.h`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_impl_mlesac.hpp`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_impl_sac_model_plane.hpp`

- :ref:`file_pcl_sample_consensus_include_pcl_sample_consensus_impl_sac_model_registration.hpp`

- :ref:`file_pcl_search_include_pcl_search_organized.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_approximate_progressive_morphological_filter.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_cpc_segmentation.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_crf_segmentation.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_euclidean_cluster_comparator.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_grabcut_segmentation.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_approximate_progressive_morphological_filter.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_crf_normal_segmentation.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_progressive_morphological_filter.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_impl_region_growing.hpp`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_lccp_segmentation.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_progressive_morphological_filter.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_region_growing.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_supervoxel_clustering.h`

- :ref:`file_pcl_segmentation_include_pcl_segmentation_unary_classifier.h`

- :ref:`file_pcl_stereo_include_pcl_stereo_digital_elevation_map.h`

- :ref:`file_pcl_stereo_include_pcl_stereo_disparity_map_converter.h`

- :ref:`file_pcl_stereo_include_pcl_stereo_impl_disparity_map_converter.hpp`

- :ref:`file_pcl_stereo_include_pcl_stereo_stereo_matching.h`

- :ref:`file_pcl_surface_include_pcl_surface_ear_clipping.h`

- :ref:`file_pcl_tracking_include_pcl_tracking_pyramidal_klt.h`

- :ref:`file_pcl_tracking_include_pcl_tracking_tracking.h`

- :ref:`file_pcl_visualization_include_pcl_visualization_image_viewer.h`

- :ref:`file_pcl_visualization_include_pcl_visualization_pcl_plotter.h`




Namespaces
----------


- :ref:`namespace_pcl`


Classes
-------


- :ref:`exhale_struct_structpcl_1_1_histogram`


Enums
-----


- :ref:`exhale_enum_group__common_1ga7b4e0dcfd710e4c96737e6012b318e8b`


Typedefs
--------


- :ref:`exhale_typedef_group__common_1ga010a963efcb59df316596af2902fcb58`

