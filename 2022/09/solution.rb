# frozen_string_literal: true

require 'set'

file_data = File.open('2022/09/input.txt', chomp: true).readlines

moves = file_data.flat_map do |l|
  move, count = l.split(' ')
  move * count.to_i
end.join('')

# rubocop:disable Metrics/CyclomaticComplexity
# rubocop:disable Metrics/MethodLength
# rubocop:disable Metrics/PerceivedComplexity
# rubocop:disable Metrics/AbcSize
def move_tail(head_x, head_y, tail_x, tail_y)
  diff_x = tail_x - head_x
  diff_y = tail_y - head_y

  if diff_x.abs + diff_y.abs <= 1 \
      || (diff_x.abs == 1 && diff_y.abs == 1)
    return [tail_x, tail_y]
  end

  if diff_x.zero?
    tail_y = (tail_y + head_y) / 2
  elsif diff_y.zero?
    tail_x = (tail_x + head_x) / 2
  elsif diff_x.abs == 2
    tail_x = (tail_x + head_x) / 2
    tail_y = head_y
  elsif diff_y.abs == 2
    tail_y = (tail_y + head_y) / 2
    tail_x = head_x
  else
    puts 'no'
    exit
  end

  [tail_x, tail_y]
end
# rubocop:enable Metrics/CyclomaticComplexity
# rubocop:enable Metrics/MethodLength
# rubocop:enable Metrics/PerceivedComplexity
# rubocop:enable Metrics/AbcSize

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

location_one = Set[]
location_one.add("#{tail_x}-#{tail_y}")

moves.split('').each do |move|
  # puts "#{move}----"
  case move
  when 'L'
    head_x -= 1
  when 'R'
    head_x += 1
  when 'U'
    head_y += 1
  when 'D'
    head_y -= 1
  end

  tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)

  # puts "H #{head_x}, #{head_y}"
  # puts "T #{tail_x}, #{tail_y}"
  # puts "T'#{tail_x}, #{tail_y}"

  location_one.add("#{tail_x}-#{tail_y}")
end

# 5883
puts location_one.size
