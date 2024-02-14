#!/bin/bash

# Delete old files
rm -rf build/*

# Build translation
make gettext
sphinx-intl update -p build/gettext -l de -l en

# Build HTML files
sphinx-build -b html -D language=de source build
sphinx-build -b html -D language=en source build/en
