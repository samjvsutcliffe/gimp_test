#! /bin/sh
echo "Removing files"
rm mpm_consol/results/mpm_consol/*
mpm -i ./mpm_consol/input_file.json -f ./ | tee out.txt
