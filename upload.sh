#!/bin/zsh
# Pelican Auto Uploader v0.0.1
# author: CHANN

cd output;
tar -cf auto.tar CNAME upload.sh .git/;
mv auto.tar ..;
cd ..;
rm -rf output;
mkdir output;
pelican -s pelicanconf.py;
mv auto.tar output/;
cd output;
tar -xf auto.tar;
rm auto.tar;
git add .;
git commit -m "New post added from upload.sh";
git push origin master;
cd ..;
