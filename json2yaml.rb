#!/usr/bin/env ruby

require "json"
require "yaml"

YAML.dump(JSON.load(ARGF), STDOUT)
