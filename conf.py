# -*- coding: utf-8 -*-
#
# pcl documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 31 16:25:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import inspect
import os
import pkg_resources
import six
import sys
import subprocess
import cmake
import platform
from subprocess import call

def run_doxygen(folder):
    """Run the doxygen make command in the designated folder"""

    try:
        # wait()?
        if platform.system() == "Windows":
            # Windows
            # retcode = subprocess.call("rmdir pcl", shell=True)
            # call(['git', 'clone', 'https://github.com/PointCloudLibrary/pcl'])
            # retcode = subprocess.call("git clone https://github.com/PointCloudLibrary/pcl", shell=True)
            retcode = subprocess.call("git clone https://github.com/PointCloudLibrary/pcl -b pcl-1.9.1 --depth 1", shell=True)
            # git pull
            retcode = subprocess.call("pushd \"%s/pcl\" && git pull && popd" % folder, shell=True)
            # make build folder
            retcode = subprocess.call("pushd \"%s/pcl\" && mkdir build && popd" % folder, shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # patch
            retcode = subprocess.call("patch -d %s/pcl -f -p1 < diff.patch" % (folder), shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # doc generate makefile in build folder
            retcode = subprocess.call("pushd \"%s/pcl/build\" && %s/cmake .. -DDOXYGEN_USE_SHORT_NAMES=OFF -DSPHINX_HTML_FILE_SUFFIX=php -DWITH_DOCS=ON -DWITH_TUTORIALS=ON && popd" % (folder, cmake.CMAKE_BIN_DIR), shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # make doc
            retcode = subprocess.call("pushd \"%s/pcl/build\" && %s/cmake --build . -- doc tutorials advanced && popd" % (folder, cmake.CMAKE_BIN_DIR), shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            retcode = subprocess.call("doxygen %s/pcl/build/doc/doxygen/doxyfile" % (folder), shell=True)
        else:
            # Linux
            retcode = subprocess.call("rm -rf pcl", shell=True)
            # retcode = subprocess.call("git clone https://github.com/PointCloudLibrary/pcl", shell=True)
            retcode = subprocess.call("git clone https://github.com/PointCloudLibrary/pcl -b pcl-1.9.1 --depth 1", shell=True)

            # git pull
            retcode = subprocess.call("cd ./pcl && git pull; cd -", shell=True)
            # folder check
            # retcode = subprocess.call("ls", shell=True)

            # make build folder
            retcode = subprocess.call("cd ./pcl; mkdir -p build; cd -", shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # patch
            retcode = subprocess.call("cd ./pcl; patch -f -p1 < ../diff.patch; cd -", shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # doc generate makefile in build folder
            # retcode = subprocess.call("cd %s/pcl/build; %s/cmake .. -DWITH_OPENGL:BOOL=OFF -DWITH_VTK:BOOL=OFF -DBUILD_visualization:BOOL=OFF -DDOXYGEN_USE_SHORT_NAMES=OFF -DSPHINX_HTML_FILE_SUFFIX=php -DWITH_DOCS=ON -DWITH_TUTORIALS=ON; cd -" % (folder, cmake.CMAKE_BIN_DIR), shell=True)
            retcode = subprocess.call("cd %s/pcl/build; %s/cmake .. -DWITH_OPENGL:BOOL=OFF -DWITH_VTK:BOOL=OFF -DBUILD_visualization:BOOL=OFF -DDOXYGEN_USE_SHORT_NAMES=OFF -DSPHINX_HTML_FILE_SUFFIX=php -DWITH_DOCS=ON -DWITH_TUTORIALS=ON > /dev/null 2>&1; cd -" % (folder, cmake.CMAKE_BIN_DIR), shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            # make doc
            retcode = subprocess.call("cd %s/pcl/build; %s/cmake --build . -- doc tutorials advanced > /dev/null 2>&1; cd -" % (folder, cmake.CMAKE_BIN_DIR), shell=True)
            if retcode < 0:
                sys.stderr.write("doxygen terminated by signal %s" % (-retcode))

            retcode = subprocess.call("doxygen %s/pcl/build/doc/doxygen/doxyfile > /dev/null 2>&1" % (folder), shell=True)

        # generate xml files in doxyfile
        # call(['doxygen', './doxyfiles/Developer_Doxyfile'])
        # retcode = subprocess.call("doxygen %s/pcl/build/doc/doxygen/doxyfile" % (folder), shell=True)
        # call(['doxygen', os.path.join(os.getcwd(), 'pcl/build/doc/doxygen/doxyfile')])

    except OSError as e:
        sys.stderr.write("doxygen execution failed: %s" % e)

# use setup.py file?
def generate_doxygen_xml(app):
    """Run the doxygen make commands if we're on the ReadTheDocs server"""

    read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

    if read_the_docs_build:
        # generate documents(contains API documents)
        print("--- read the docs build ---")
        # build read the docs hosting server.(timeout error)
        # remove read the docs cache data
        retcode = subprocess.call("rm -rf pcl", shell=True)
        # set conda module paths
        rootpath = '/home/docs/checkouts/readthedocs.org/user_builds/pcl-docs/conda/latest'
        os.environ["EIGEN_INCLUDE_DIR"] = os.path.join(rootpath, 'include/eigen3')
        os.environ["EIGEN3_INCLUDE_DIR"] = os.path.join(rootpath, 'include/eigen3')
        os.environ["EIGEN_ROOT"] = os.path.join(rootpath, 'include/eigen3')
        os.environ["FLANN_ROOT"] = rootpath
        os.environ["FLANN_INCLUDE_DIRS"] = os.path.join(rootpath, 'include/flann')
        os.environ["FLANN_LIBRARY"] = os.path.join(rootpath, 'lib')
        os.environ["BOOST_ROOT"] = rootpath
        os.environ["QHULL_ROOT"] = rootpath
        os.environ["VTK_DIR"] = rootpath
        os.environ["GLEW_ROOT"] = rootpath
        retcode = subprocess.call("export CMAKE_PREFIX_PATH=$CMAKE_PREFIX_PATH:/home/docs/checkouts/readthedocs.org/user_builds/pcl-docs/checkouts/latest/pcl/cmake/Modules", shell=True)
        run_doxygen(".")
        # generate documents(not generate API documents)
        # print("--- read the docs build(without API document) ---")
        # retcode = subprocess.call("git clone https://github.com/PointCloudLibrary/pcl -b pcl-1.9.1 --depth 1", shell=True)
        # # build local pc.(git contains _build/html folder)
        # # print("--- read the docs build(using _build folder files.) ---")
        pass

# Running on Read the Docs
# https://breathe.readthedocs.io/en/latest/readthedocs.html
def setup(app):

    # Add hook for building doxygen xml when needed
    app.connect("builder-inited", generate_doxygen_xml)


read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
if not read_the_docs_build:
    print("--- not read the docs ---")
    run_doxygen(".")


# make source(generate rst from source code.)
# call(['python', './make_source.py', './pcl', './api'])
# call(['python', os.path.join(os.getcwd(), 'make_source.py'), os.path.join(os.getcwd(), 'pcl'), os.path.join(os.getcwd(), 'api')])

# breathe_projects = { "myproject" : "./user_doxygen_out/xml/" }
breathe_projects = { "myproject" : "./pcl/build/doc/doxygen/xml/" }
# breathe_projects = { "myproject" : os.path.join(os.getcwd(), 'pcl/build/doc/doxygen/xml/') }
breathe_default_project = "myproject"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    # "containmentFolder":     os.path.join(os.getcwd(), 'api'),
    "containmentFolder":     './api',
    "rootFileName":          "index.rst",
    "rootFileTitle":         "Library API",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    # "exhaleExecutesDoxygen": True,
    # "exhaleDoxygenStdin":    "INPUT = os.path.join(os.getcwd(), 'pcl')
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.imgmath', 'sphinx.ext.todo']
# generate API documentation(api rst generate local build)
# extensions = ['sphinx.ext.imgmath', 'sphinx.ext.todo', 'breathe']
# generate API rst files before upload.
# extensions = ['sphinx.ext.imgmath', 'sphinx.ext.todo', 'breathe', 'exhale']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Only add spelling extension if it is available. We don't know if it is installed as we don't want
# to put it in the setup.py file as a dependency as we don't want Breathe to be dependent on it as
# people should be able to use Breathe without 'spelling'. There might be a better way to handle
# this.
try:
    import sphinxcontrib.spelling
    extensions.append('sphinxcontrib.spelling')
except ImportError:
    pass


# Configuration for spelling extension
spelling_word_list_filename='spelling_wordlist.txt'
spelling_lang='en_US'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pcl'
copyright = u'2019, open perception foundation'
author = u'open perception foundation'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.9'
# The full version, including alpha/beta/rc tags
release = u'1.9.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None
# language = 'en'
# language = 'ja'
# NG : not support multiarray
# language = ['en', '.ja']
# locale_dirs = ['locale']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['.build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Napoleon settings
napoleon_use_ivar = True
napoleon_include_special_with_doc = True

# Options for HTML output
# -----------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if not on_rtd:
    html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_style = 'css/modified_theme.css'

if on_rtd:
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/modified_theme.css',
        ],
    }

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'pcldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pcl.tex', u'pcl Documentation',
     u'open perception foundation', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, u'pcl', u'pcl Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pcl', u'pcl Documentation',
     author, 'pcl', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}


def _import_object_from_name(module_name, fullname):
    obj = sys.modules.get(module_name)
    if obj is None:
        return None
    for comp in fullname.split('.'):
        obj = getattr(obj, comp)
    return obj


def linkcode_resolve(domain, info):
    if domain != 'py' or not info['module']:
        return None

    rtd_version = os.environ.get('READTHEDOCS_VERSION')
    if rtd_version == 'latest':
        tag = 'master'
    else:
        tag = 'v{}'.format(__version__)
    repo_root_dir = os.path.realpath('..')

    # Import the object from module path
    obj = _import_object_from_name(info['module'], info['fullname'])

    # Get the source file name and line number at which obj is defined.
    try:
        filename = inspect.getsourcefile(obj)
    except TypeError:
        # obj is not a module, class, function, ..etc.
        return None

    # inspect can return None for cython objects
    if filename is None:
        return None

    # Get the source line number
    _, linenum = inspect.getsourcelines(obj)
    assert isinstance(linenum, six.integer_types)

    filename = os.path.realpath(filename)
    if not filename.startswith(repo_root_dir):
        return None
    relpath = os.path.relpath(filename, repo_root_dir)

    return 'https://github.com/PointCloudLibrary/pcl/blob/{}/{}#L{}'.format(
        tag, relpath, linenum)
