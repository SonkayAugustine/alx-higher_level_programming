#!/bin/bash
# script that takes a url and displays all http methods server the accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
