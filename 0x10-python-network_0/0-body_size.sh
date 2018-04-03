#!/bin/bash
# Send a request to URL and show size
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
