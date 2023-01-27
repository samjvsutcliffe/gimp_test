#!/bin/bash
echo "Running MPM"
(cd ./test_cases/mpm ;./run.sh)
echo "Running GIMP"
(cd ./test_cases/gimp ;./run.sh)
