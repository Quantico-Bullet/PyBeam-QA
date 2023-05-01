#!/bin/bash
echo "----- Converting Qt resources to python files -----"
mkdir py_ui
echo
for file in qt_ui/*.ui
    do
        base_name=$(basename -- ${file})
        echo "converting ui file: ${base_name} --> ${base_name%.*}_ui.py"
        pyside6-uic "${file}" -o "py_ui/${base_name%.*}_ui.py" 
    done
    
for file in qt_ui/*.qrc
    do
        base_name=$(basename -- ${file})
        echo "converting resource file: ${base_name} --> ${base_name%.*}_rc.py"
        pyside6-rcc "${file}" -o "py_ui/${base_name%.*}_rc.py"
    done
