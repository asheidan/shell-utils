#!/bin/bash

set -e

chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

render_delay=10000

function browser() {
    "${chrome}" \
        --headless --disable-gpu --dump-dom \
        --virtual-time-budget=$render_delay \
        "$1"
}

browser $*