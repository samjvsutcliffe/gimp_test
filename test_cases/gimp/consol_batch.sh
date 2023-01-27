#! /bin/bash
python3 consol_gen.py
echo "Removing files"
rm gimp_consol/results/gimp_consol/*
echo "Running code"
~/cb-geo/mpm/build/mpm -p 8 -i ./gimp_consol/input_file.json -f ./ | tee out.txt
