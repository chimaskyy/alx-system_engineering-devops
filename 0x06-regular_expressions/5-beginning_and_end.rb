#!/usr/bin/env ruby
# match string that start with h and end with n

regex = /^h.n$/
puts ARGV[0].scan(regex).join
