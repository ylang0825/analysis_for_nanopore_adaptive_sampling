#!/bin/bash

while true
do
mark=`ps -ef | grep ReadBouncer | grep -v grep | wc -l`
if [ $mark -ne 0 ]
then
echo 'running'
else
ReadBouncer --config target.toml &
fi
sleep 30s
done

