#!/bin/sh

set -x

window_class=$1
shift 1

executable=$1

i3-msg -q -- "[class=\"${window_class}\"]" focus || (test -e "${executable}" && i3-msg -q -- exec "$@")
