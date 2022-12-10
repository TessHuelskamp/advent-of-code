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

locations = {
  head: [0, 0],
  one: [0, 0]
}

location_one = Set[]
location_one.add('0-0')

moves.split('').each do |move|
  # puts "#{move}----"
  case move
  when 'L'
    locations[:head][0] -= 1
  when 'R'
    locations[:head][0] += 1
  when 'U'
    locations[:head][1] += 1
  when 'D'
    locations[:head][1] -= 1
  end

  locations[:one][0], locations[:one][1] = move_tail(locations[:head][0], locations[:head][1], locations[:one][0],
                                                     locations[:one][1])

  # puts "H #{head_x}, #{head_y}"
  # puts "T #{tail_x}, #{tail_y}"
  # puts "T'#{tail_x}, #{tail_y}"

  location_one.add("#{locations[:one][0]}-#{locations[:one][1]}")
end

# 5883
puts location_one.size
