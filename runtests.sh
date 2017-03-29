set -e
if [ "$LINT" ]; then
    flake8 github_hook tests --exclude migrations
else
    python setup.py test
fi
