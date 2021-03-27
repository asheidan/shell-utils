#!/usr/bin/env ruby

require "json"
require "yaml"

YAML.load_stream(ARGF).each do |y|
  JSON.dump(y, STDOUT)
  puts
end
