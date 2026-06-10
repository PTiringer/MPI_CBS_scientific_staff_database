#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh MPI_CBS_scientific_staff_database/ .
  rm -rfv MPI_CBS_scientific_staff_database
fi
