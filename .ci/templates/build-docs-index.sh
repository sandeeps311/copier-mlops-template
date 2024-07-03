#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o nounset
set -o pipefail

echo "Running in $(pwd)..."

for dir in $(/usr/bin/find . -maxdepth 1 -type d); do
  echo "$dir"
  if [[ -f "$dir/index.html" ]]; then
    echo "Removing $dir/index.html"
    rm "$dir/index.html"
  fi

  if [[ "$dir" == "." ]]; then
    echo "Building root index.html"
    tree -dv "$dir" -H "." -L 1 --noreport --charset utf-8 -o "$dir/index.html"

    # Relabel directory name
    sed -i "s|<title>Directory Tree</title><p>|<title>Data Science Documentation</title><p>|g"  "$dir/index.html"
    sed -i "s|<h1>Directory Tree</h1><p>|<h1>Data Science Documentation</h1><p>|g"  "$dir/index.html"
    sed -i "s|>.</a><br>|>Packages</a><br>|g" "$dir/index.html"
  else
    echo "Building $dir/index.html"
    tree -dvr "$dir" -H "." -L 1 --noreport --charset utf-8 -o "$dir/index.html"

    # Relabel directory name
    sed -i "s|<title>Directory Tree</title><p>|<title>${dir:2}</title><p>|g" "$dir/index.html"
    sed -i "s|<h1>Directory Tree</h1><p>|<h1>${dir:2}</h1><p>|g" "$dir/index.html"
    sed -i "s|>.</a><br>|>Versions</a><br>|g" "$dir/index.html"
    # Insert back to Documentation homepage above <hr>
    sed -i "s|<hr>|<br>\n<a href=\"..\">Back to dsdocs</a><br>\n<hr>|g" "$dir/index.html"
  fi
done;
