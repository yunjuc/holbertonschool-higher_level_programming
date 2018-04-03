#!/bin/bash
# Display all HTTP methods the server accept
curl -sI "$1" | grep Allow | cut -c8-
