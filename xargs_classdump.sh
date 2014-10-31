#!/usr/bin/env sh
dump=`sw_vers -productVersion`
mkdir ~/Desktop/$dump/$1
mkdir ~/Desktop/$dump/$1/PrivateHeaders
class-dump /System/Library/PrivateFrameworks/$1 -H -o ~/Desktop/$dump/$1/PrivateHeaders/ 
