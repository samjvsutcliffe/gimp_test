#! /bin/sh
python3 consol_gen.py
echo "Removing files"
rm mpm_consol/results/mpm_consol/*
echo "Running code"
mpm -i ./mpm_consol/input_file.json -f ./ | tee out.txt
