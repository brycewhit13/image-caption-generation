#!/usr/bin/env bash
## Format all code directories in the repostitory using black.

for DIR in */; do
    DIRNAME=$(basename "$DIR")
    echo "==> $DIRNAME <=="
    (cd $DIR && black *.py)
done

echo "Format complete."