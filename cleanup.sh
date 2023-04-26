#!/bin/bash

rm -r webapp/app/migrations/*
rm -f webapp/db.sqlite3
rm -rf .git

touch webapp/app/migrations/__init__.py
