#!/usr/bin/env ruby
# hbt, hbtn, hbn

regex = /hbt*n/
puts ARGV[0].scan(regex).join

