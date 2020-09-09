#!/bin/bash
source venv/bin/activate

workspace_root="${BASH_SOURCE%/*}/../backend"
cd "$workspace_root" || exit

flake8 . --count --show-source --statistics --exclude=venv

verbose=false
for arg in "$@"; do
  if [ "$arg" == "-s" ]; then
    verbose=true
    break
  fi
done

if [ "$verbose" = true ]; then
  pytest -v -s --cov --cov-config=.coveragerc --cov-report=xml
else
  pytest -v --cov --cov-config=.coveragerc --cov-report=xml
fi

for arg in "$@"; do
  if [ "$arg" == "-u" ]; then
    echo "Uploading coverage"
    curl --request POST --user brucknem:P663UMlRrdjINlPYHtkaOh2IeRC5muKJ --form "report=@coverage.xml" "http://marcelbruckner.spdns.de:8080/api/projects/workstation-monitor-backend/external-analysis/session/auto-create/report?format=Cobertura&partition=Unit%20Tests&message=Unit%20Test%20Coverage"
    break
  fi
done
