#!/usr/bin/env ruby
# match 10 digit number

regex = /^\d{10,10}$/
puts ARGV[0].scan(regex).join
