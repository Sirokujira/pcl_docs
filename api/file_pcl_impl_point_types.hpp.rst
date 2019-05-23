
.. _file_pcl_impl_point_types.hpp:

File point_types.hpp
====================

|exhale_lsh| :ref:`Parent directory <dir_pcl_impl>` (``pcl\impl``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. contents:: Contents
   :local:
   :backlinks: none

Definition (``pcl\impl\point_types.hpp``)
-----------------------------------------


.. toctree::
   :maxdepth: 1

   program_listing_file_pcl_impl_point_types.hpp.rst





Includes
--------


- ``Eigen/Core``

- ``ostream``

- ``pcl/common/point_tests.h``



Included By
-----------


- :ref:`file_pcl_point_types.h`




Namespaces
----------


- :ref:`namespace_pcl`


Classes
-------


- :ref:`exhale_struct_structpcl_1_1___axis`

- :ref:`exhale_struct_structpcl_1_1___intensity`

- :ref:`exhale_struct_structpcl_1_1___intensity32u`

- :ref:`exhale_struct_structpcl_1_1___intensity8u`

- :ref:`exhale_struct_structpcl_1_1___normal`

- :ref:`exhale_struct_structpcl_1_1___point_d_e_m`

- :ref:`exhale_struct_structpcl_1_1___point_normal`

- :ref:`exhale_struct_structpcl_1_1___point_surfel`

- :ref:`exhale_struct_structpcl_1_1___point_with_range`

- :ref:`exhale_struct_structpcl_1_1___point_with_scale`

- :ref:`exhale_struct_structpcl_1_1___point_with_viewpoint`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_h_s_v`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_i`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_i_normal`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_l`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_l_normal`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_r_g_b`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_r_g_b_a`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_r_g_b_l`

- :ref:`exhale_struct_structpcl_1_1___point_x_y_z_r_g_b_normal`

- :ref:`exhale_struct_structpcl_1_1___reference_frame`

- :ref:`exhale_struct_structpcl_1_1___r_g_b`

- :ref:`exhale_struct_structpcl_1_1_axis`

- :ref:`exhale_struct_structpcl_1_1_border_description`

- :ref:`exhale_struct_structpcl_1_1_boundary`

- :ref:`exhale_struct_structpcl_1_1_b_r_i_s_k_signature512`

- :ref:`exhale_struct_structpcl_1_1_c_p_p_f_signature`

- :ref:`exhale_struct_structpcl_1_1_e_s_f_signature640`

- :ref:`exhale_struct_structpcl_1_1_f_p_f_h_signature33`

- :ref:`exhale_struct_structpcl_1_1_g_a_s_d_signature512`

- :ref:`exhale_struct_structpcl_1_1_g_a_s_d_signature7992`

- :ref:`exhale_struct_structpcl_1_1_g_a_s_d_signature984`

- :ref:`exhale_struct_structpcl_1_1_g_f_p_f_h_signature16`

- :ref:`exhale_struct_structpcl_1_1_g_r_s_d_signature21`

- :ref:`exhale_struct_structpcl_1_1_histogram`

- :ref:`exhale_struct_structpcl_1_1_intensity`

- :ref:`exhale_struct_structpcl_1_1_intensity32u`

- :ref:`exhale_struct_structpcl_1_1_intensity8u`

- :ref:`exhale_struct_structpcl_1_1_intensity_gradient`

- :ref:`exhale_struct_structpcl_1_1_interest_point`

- :ref:`exhale_struct_structpcl_1_1_label`

- :ref:`exhale_struct_structpcl_1_1_moment_invariants`

- :ref:`exhale_struct_structpcl_1_1_narf36`

- :ref:`exhale_struct_structpcl_1_1_normal`

- :ref:`exhale_struct_structpcl_1_1_normal_based_signature12`

- :ref:`exhale_struct_structpcl_1_1_p_f_h_r_g_b_signature250`

- :ref:`exhale_struct_structpcl_1_1_p_f_h_signature125`

- :ref:`exhale_struct_structpcl_1_1_point_d_e_m`

- :ref:`exhale_struct_structpcl_1_1_point_normal`

- :ref:`exhale_struct_structpcl_1_1_point_surfel`

- :ref:`exhale_struct_structpcl_1_1_point_u_v`

- :ref:`exhale_struct_structpcl_1_1_point_with_range`

- :ref:`exhale_struct_structpcl_1_1_point_with_scale`

- :ref:`exhale_struct_structpcl_1_1_point_with_viewpoint`

- :ref:`exhale_struct_structpcl_1_1_point_x_y`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_h_s_v`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_i`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_i_normal`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_l`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_l_normal`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_r_g_b`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_r_g_b_a`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_r_g_b_l`

- :ref:`exhale_struct_structpcl_1_1_point_x_y_z_r_g_b_normal`

- :ref:`exhale_struct_structpcl_1_1_p_p_f_r_g_b_signature`

- :ref:`exhale_struct_structpcl_1_1_p_p_f_signature`

- :ref:`exhale_struct_structpcl_1_1_principal_curvatures`

- :ref:`exhale_struct_structpcl_1_1_principal_radii_r_s_d`

- :ref:`exhale_struct_structpcl_1_1_reference_frame`

- :ref:`exhale_struct_structpcl_1_1_r_g_b`

- :ref:`exhale_struct_structpcl_1_1_shape_context1980`

- :ref:`exhale_struct_structpcl_1_1_s_h_o_t1344`

- :ref:`exhale_struct_structpcl_1_1_s_h_o_t352`

- :ref:`exhale_struct_structpcl_1_1_unique_shape_context1960`

- :ref:`exhale_struct_structpcl_1_1_v_f_h_signature308`


Functions
---------


- :ref:`exhale_function_namespacepcl_1aaa69fd139cdf30136859e5c44171ce84`

- :ref:`exhale_function_namespacepcl_1a1e8528949adf7d108f67295784ea8f4c`

- :ref:`exhale_function_namespacepcl_1aab08c0deb092684b90e6bf986bd77e4f`

- :ref:`exhale_function_namespacepcl_1a9ee8aad293f74d3742a25238a786c2e9`

- :ref:`exhale_function_namespacepcl_1a2458afa4cdfef33ff38dace1ad221e73`

- :ref:`exhale_function_namespacepcl_1a105b339fcb7ac0a6adc12d4d7d8b6054`

- :ref:`exhale_function_namespacepcl_1a3d52efa0d7cbf23909bd816bb0a1c666`

- :ref:`exhale_function_namespacepcl_1a63c118315e1092054d743db6c859d40a`

- :ref:`exhale_function_namespacepcl_1ae13addefb957e51551de773268c65c82`

- :ref:`exhale_function_namespacepcl_1abc8cfa2a02fbd9dac7f8122dcf6e2bb7`

- :ref:`exhale_function_namespacepcl_1a4534a2c1bd0618b111647e999e77df33`

- :ref:`exhale_function_namespacepcl_1aa6ae936041311537e8a56dec6159ced9`

- :ref:`exhale_function_namespacepcl_1a5d952d1be42065f1810999eccc365ddf`

- :ref:`exhale_function_namespacepcl_1a2b039494767b268e50f0a1bb2976fa48`

- :ref:`exhale_function_namespacepcl_1a0d41b561831d49b78d04200ee37d3002`

- :ref:`exhale_function_namespacepcl_1a19343463a3278d1d0e3db79c4e018aaa`

- :ref:`exhale_function_namespacepcl_1a3de48790dd4f9e19c9a1550fb848ea3d`

- :ref:`exhale_function_namespacepcl_1a1608e058a8bc248efa6f5220e655cff7`

- :ref:`exhale_function_namespacepcl_1a90501d20b65f614f006f508b852e5770`

- :ref:`exhale_function_namespacepcl_1a0225d96d6b8de7b63f878ccbe58c1e82`

- :ref:`exhale_function_namespacepcl_1a1dc7a0ea4cd99f38691a573b989f5540`

- :ref:`exhale_function_namespacepcl_1aaebc412871f2707e575fa34ce572572a`

- :ref:`exhale_function_namespacepcl_1aa18dfb13fd6d95ba40ccad228917d1b2`

- :ref:`exhale_function_namespacepcl_1a01fab9179c9352d802406f948da4951b`

- :ref:`exhale_function_namespacepcl_1af20aa5d2c41247323461c041a257f1bc`

- :ref:`exhale_function_namespacepcl_1a45fe4f8c4719b2ffbc7b617333767f46`

- :ref:`exhale_function_namespacepcl_1a5b1153a607ce169857125edae09cfe39`

- :ref:`exhale_function_namespacepcl_1ac837bb01edfb9daaec3f6c6459662445`

- :ref:`exhale_function_namespacepcl_1af6ce409883a619f6e9b4bfb3ce61d0c7`

- :ref:`exhale_function_namespacepcl_1a1c99ce77bc64a87b38980b612e31c921`

- :ref:`exhale_function_namespacepcl_1a72338648bb90c152d9877996101dc59e`

- :ref:`exhale_function_namespacepcl_1a4827eb3b63ef3565d88791ff9d674eb5`

- :ref:`exhale_function_namespacepcl_1a259fa5168292d2f0a5bbfee6208304a4`

- :ref:`exhale_function_namespacepcl_1ab125cc601b291e5d99552aafce17a53e`

- :ref:`exhale_function_namespacepcl_1aeec9af0fa6d2045038d97086d2564b04`

- :ref:`exhale_function_namespacepcl_1ae2821e799172bdcc306b9efd1f759b63`

- :ref:`exhale_function_namespacepcl_1a61bc5840d2339ab463518c23d2eec429`

- :ref:`exhale_function_namespacepcl_1a502d6cf6fd2b60cbed256dfa64574eb4`

- :ref:`exhale_function_namespacepcl_1adc0503cf66eb447c6a1d6f460f3c5265`

- :ref:`exhale_function_namespacepcl_1a5fcc1cb564b3460bc9f09a0ff4fb0dc9`

- :ref:`exhale_function_namespacepcl_1ae032ca18d8a2d681bb9c6f61dc47722a`

- :ref:`exhale_function_namespacepcl_1a90abb02fce3fae16f4f6812fba2027a1`

- :ref:`exhale_function_namespacepcl_1a9d43ea244ae0faf522aebc5559673fa8`

- :ref:`exhale_function_namespacepcl_1a194bce1cd392f2839fdf417016be09f1`

- :ref:`exhale_function_namespacepcl_1a5d15602f8e84118e21dc97048232d5c6`

- :ref:`exhale_function_namespacepcl_1aad38e7946d98cae3c778e06ecbaa4df9`

- :ref:`exhale_function_namespacepcl_1a0cf0dccceb5499828fdeb277ec86ee24`

- :ref:`exhale_function_namespacepcl_1ae7c5f8626f928698f5b3a8967f0b046a`

- :ref:`exhale_function_namespacepcl_1a87ec5383674604eedd381f0c379b04f5`

- :ref:`exhale_function_namespacepcl_1a412c39716aa2a36ff6ab9ade75c169c4`

- :ref:`exhale_function_namespacepcl_1a509826a38db4aeebcf04422c06dda97a`

- :ref:`exhale_function_namespacepcl_1a23eb640f2481ebea8e9b2c9428ea213f`

- :ref:`exhale_function_namespacepcl_1a06bd0eda0fca53206e567da9048be531`

- :ref:`exhale_function_namespacepcl_1a4ad2d3d0146b30ce1ea5d3d816caec10`


Defines
-------


- :ref:`exhale_define_point__types_8hpp_1a30e66aff23884bed8bbd36864374fa79`

- :ref:`exhale_define_point__types_8hpp_1adb14739dde0c932b7cb51e05a36b31de`

- :ref:`exhale_define_point__types_8hpp_1af43a98adf9739c04096c75c7e08a647b`

- :ref:`exhale_define_point__types_8hpp_1a7c6268a1e9d1b089dd2e2b6750592bbc`

- :ref:`exhale_define_point__types_8hpp_1a1b1e1598ed368a53d803320e6997f563`

- :ref:`exhale_define_point__types_8hpp_1a3d7ddbcf0507cd540a2f1c09ad95c2a9`

- :ref:`exhale_define_point__types_8hpp_1ad597c7e204b3e6844febcdaca4725b31`

- :ref:`exhale_define_point__types_8hpp_1a3c871c32d4246ff1732b5ac3fcac2d5c`

- :ref:`exhale_define_point__types_8hpp_1af78cac98e1a68cc129fb0d354390ebec`

- :ref:`exhale_define_point__types_8hpp_1a8249def6a4b1debe242c59ca6ee00241`

- :ref:`exhale_define_point__types_8hpp_1a25e4cbf0cf97d094aa7579d84029d063`

- :ref:`exhale_define_point__types_8hpp_1a63617d463eb4165296a85eaa9a8144f2`

- :ref:`exhale_define_point__types_8hpp_1a392784fa97e01394c4755100bcb73490`

- :ref:`exhale_define_point__types_8hpp_1afa1c36f90df2559d377af82a343336db`

- :ref:`exhale_define_point__types_8hpp_1a0b18659d81a8776c235a151dda59ac1b`

- :ref:`exhale_define_point__types_8hpp_1a4035b7c13c94595ee6fb7218d6c6b521`

- :ref:`exhale_define_point__types_8hpp_1aeb015c79294f9d166d57906b4f8cf416`

- :ref:`exhale_define_point__types_8hpp_1a8f6ed80fef2eb7c0b76e11d8d243a843`


Typedefs
--------


- :ref:`exhale_typedef_namespacepcl_1a6ce3a870041fff78da76ed60146d8808`

- :ref:`exhale_typedef_namespacepcl_1a84a4b6f9dbfb63e864c14e0be832c23d`

- :ref:`exhale_typedef_namespacepcl_1a07a3fc2460ea11c24ea088f84c30187d`

- :ref:`exhale_typedef_namespacepcl_1ac8b93eb05fe1cb7db3fad46e0dec3c54`

- :ref:`exhale_typedef_namespacepcl_1a3f1f7191faa2f8789a08d44e1487219c`

- :ref:`exhale_typedef_namespacepcl_1a5341e0645dc49946eeb3662d206c66e4`

- :ref:`exhale_typedef_namespacepcl_1a846aee9dd91800b9eee1463fb01e0e04`

- :ref:`exhale_typedef_namespacepcl_1a978ebc08c71533410afd26373c7e7a3a`

- :ref:`exhale_typedef_namespacepcl_1ab4a6649fc0d06df1d72fdfdfdfb30817`

- :ref:`exhale_typedef_namespacepcl_1a1e55d3e409549c5a07af0984cdb2ff51`

- :ref:`exhale_typedef_namespacepcl_1a8385922b8842da441f7d7c672afb5eb6`

- :ref:`exhale_typedef_namespacepcl_1a38b68017e1264404c903bcb3ee3c290f`

- :ref:`exhale_typedef_namespacepcl_1a3064cde6e761536d0039ad3e4fba2cdb`

- :ref:`exhale_typedef_namespacepcl_1afaca6046b889e67242085e46c25fbe82`

