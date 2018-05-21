#!/usr/bin/env bash

source venv

case "$1" in
    build)
    rm -rf build
    rm -rf metacmd.egg-*
    rm -rf dist

    python setup.py bdist_wheel
    ;;

    test_upload)
    twine upload -r pypitest dist/*
    ;;

    upload)
    twine upload -r pypi dist/*
    ;;
    *)
        echo "./deploy.sh [build, test_upload, upload]"
    ;;
esac