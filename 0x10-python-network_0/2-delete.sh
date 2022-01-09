#!/bin/bash
# script that send a DELETE request to url passed as 1st arg
curl -sX "DELETE" "$1"
