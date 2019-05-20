Introduction

This repostitory contains scripts and files for generating API documenations automatically. We are using
•Doxygen: http://www.stack.nl/~dimitri/doxygen/
•Breathe: https://github.com/michaeljones/breathe
•Sphinx: http://www.sphinx-doc.org/en/stable/
•ReadTheDocs: https://readthedocs.org/

Why ?

...

How it works ?
1.Clone the PointCloudLibrary repository.
2.Run Doxygen to generate .xml files.
3.Run make_source.py to generate .rst files from .xml files.
4.Run Sphinx with Breathe exntension to generate .html files.
•Github will send a signal to ReadTheDocs when the PointCloudLibrary repository has a update. 
 Therefore, step 2-5 will be ran on ReadTheDocs automatically. 
 The API documentation will be available at: https://pcl.readthedocs.org

Run on local for testing
conda env create -f environment.yml
conda activate pcl-docs
make html

Contact

Please feel free to contact to the author (...@...) if you have a question.
