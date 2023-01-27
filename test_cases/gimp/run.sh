#! /bin/sh
echo "Removing files"
rm gimp_consol/results/gimp_consol/*
mpm -i ./gimp_consol/input_file.json -f ./ | tee out.txt
