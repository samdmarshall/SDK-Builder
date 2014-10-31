#!/usr/bin/env sh
dump=`sw_vers -productVersion`
mkdir ~/Desktop/$dump
ls /System/Library/PrivateFrameworks/ | xargs -L 1 ./xargs_classdump.sh