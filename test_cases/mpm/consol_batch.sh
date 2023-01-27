#! /bin/bash
python3 consol_gen.py
echo "Removing files"
rm mpm_consol/results/mpm_consol/*
echo "Running code"
~/cb-geo/mpm/build/mpm -p 8 -i ./mpm_consol/input_file.json -f ./ | tee out.txt
