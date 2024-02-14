#!/bin/bash

# Delete old files
rm -rf build/*

# Build translation
make gettext
sphinx-intl update -p build/gettext -l de -l en

# Build PDF files
sphinx-build -b latex source build
cd build
pdflatex stura-ordnungen.tex
