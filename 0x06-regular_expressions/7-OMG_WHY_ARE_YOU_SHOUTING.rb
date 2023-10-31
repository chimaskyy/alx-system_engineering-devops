#!/usr/bin/env ruby
# match capslock

regex = /[A-Z]/
puts ARGV[0].scan(regex).join
