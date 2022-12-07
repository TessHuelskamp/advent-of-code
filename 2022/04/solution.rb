# frozen_string_literal: true

# lol
require 'set'

file = File.open('2022/04/input.txt')
file_data = file.readlines

def any_fully_contain?(left, right)
  left = (left[0].to_i..left[1].to_i).to_set
  right = (right[0].to_i..right[1].to_i).to_set

  left.subset?(right) || right.subset?(left)
end

def any_intersect?(left, right)
  left = (left[0].to_i..left[1].to_i).to_set
  right = (right[0].to_i..right[1].to_i).to_set

  left.intersect?(right)
end

total_a = 0
total_b = 0

file_data.each do |line|
  line.chomp!

  left, right = line.split(',')

  total_a += 1 if any_fully_contain?(left.split('-'), right.split('-'))
  total_b += 1 if any_intersect?(left.split('-'), right.split('-'))
end

puts total_a
puts total_b
