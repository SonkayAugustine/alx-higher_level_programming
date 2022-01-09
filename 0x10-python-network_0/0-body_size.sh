#!/bin/bash
# a script that takes in a url, sends a request to that url
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
