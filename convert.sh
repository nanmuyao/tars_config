#!/bin/sh
for file in *.mp3
do
  afconvert -f caff -d aac $file
  rm -rf $file
done

