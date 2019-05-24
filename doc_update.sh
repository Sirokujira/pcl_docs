#!/bin/sh
source ~/.bashrc
conda activate pcl-docs

cd $(cd $(dirname $0) && pwd)

make html
git add _build -f
git add api -f
git commit -m "auto update(daily build)"
git push origin master

