#!/usr/bin/env ruby
# matches h followed by zero or 1 b, zero or 1 t followed by n
# hbt, hbtn

regex = /hb?t?n/
puts ARGV[0].scan(regex).join

