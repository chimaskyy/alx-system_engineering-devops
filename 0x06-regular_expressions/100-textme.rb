#!/usr/bin/env ruby
# match capslock

regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
puts ARGV[0].scan(regex).join(",")
