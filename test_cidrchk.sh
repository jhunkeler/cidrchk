#!/bin/bash
program=./cidrchk
args="$@"

if [ -z "$args" ]; then
    echo "No CIDR range(s) defined"
    exit 1
fi

$program $args
retval=$?

case "$retval" in
    0)
        echo "On net"
    ;;
    1)
        echo "Off net"
    ;;
    2)
        echo "Module import failure detected"
    ;;
    3)
        echo "No network interfaces detected"
    ;;
    *)
        echo "Unknown failure"
    ;;
esac
