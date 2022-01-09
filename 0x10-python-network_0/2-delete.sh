#!/bin/bash
# script that send a DELETE request to url passed as 1st arg &
# displays resopnse
curl -sX "DELETE" "$1"
