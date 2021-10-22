#!/bin/sh

set -x

i3-msg -q -- "[class=\"$1\"]" focus || (test -e "$2" && i3-msg -q exec "$2")
