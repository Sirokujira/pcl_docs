Introduction

This repostitory contains scripts and files for generating API documenations automatically. We are using
•Doxygen: http://www.stack.nl/~dimitri/doxygen/
•Breathe: https://github.com/michaeljones/breathe
•Exhale: https://github.com/svenevs/exhale
•Sphinx: http://www.sphinx-doc.org/en/stable/
•ReadTheDocs: https://readthedocs.org/

Why ?

https://github.com/PointCloudLibrary/pcl/issues/2864
...


How it works ?
1. Clone the PointCloudLibrary repository.
2. Run Doxygen to generate .xml files.
3. Run make_source.py to generate .rst files from .xml files.
4. Run Sphinx with Breathe exntension to generate .html files.
•Github will send a signal to ReadTheDocs when the PointCloudLibrary repository has a update. 
 Therefore, step 2-5 will be ran on ReadTheDocs automatically. 
 The API documentation will be available at: https://pcl.readthedocs.org

Generate on local for testing
```cmd
$ conda env create -f environment.yml
$ conda activate pcl-docs
$ make html
```

Contact

Please feel free to contact to the author (t753github@gmail.com) if you have a question.
