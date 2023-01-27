#!/bin/sh
echo "Running MPM"
(cd ./test_cases/mpm/; ./consol_batch.sh)
echo "Running GIMP"
(cd ./test_cases/gimp/; sh consol_batch.sh)
