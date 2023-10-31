#!/usr/bin/env ruby
## matches hb followed by 1 or 5 t, followed by n
## hbtn, hbttn, hbtttn

regex = /hbt+n/
puts ARGV[0].scan(regex).join

