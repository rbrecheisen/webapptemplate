#!/bin/bash

# install: brew install minio/stable/minio
minio server /tmp/minio/data --console-address :9090
