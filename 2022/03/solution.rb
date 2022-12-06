# frozen_string_literal: true

require 'set'

file = File.open('2022/03/input.txt')
file_data = file.readlines

total_a = 0

def build_set(string)
  string.split('').to_set
end

def priority(letter)
  ord = letter.ord
  case ord
  when 97..122
    ord - 96
  when 65..90
    ord - 64 + 26
  end
end

file_data.each do |line|
  line.size

  left = build_set(line[0, line.length / 2])
  right = build_set(line[line.length / 2, line.length])

  same_letter = left.intersection(right).to_a.first
  total_a += priority(same_letter)
end

puts total_a

total_b = 0

(0..file_data.size - 1).step(3) do |i|
  set_a = build_set(file_data[i].chomp)
  set_b = build_set(file_data[i + 1].chomp)
  set_c = build_set(file_data[i + 2].chomp)

  letter = set_a.intersection(set_b).intersection(set_c).to_a.first
  total_b += priority(letter)
end

puts(total_b)
