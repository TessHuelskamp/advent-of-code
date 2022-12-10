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
  elsif diff_x.abs == 2 && diff_y.abs == 2
    tail_x = (tail_x + head_x) / 2
    tail_y = (tail_y + head_y) / 2
  elsif diff_x.abs == 2
    tail_x = (tail_x + head_x) / 2
    tail_y = head_y
  elsif diff_y.abs == 2
    tail_y = (tail_y + head_y) / 2
    tail_x = head_x
  else
    puts 'no'
    puts "#{head_x}, #{head_y}, #{tail_x}, #{tail_y}"
    exit
  end

  [tail_x, tail_y]
end
# rubocop:enable Metrics/CyclomaticComplexity
# rubocop:enable Metrics/MethodLength
# rubocop:enable Metrics/PerceivedComplexity
# rubocop:enable Metrics/AbcSize

loc = {
  head: [0, 0],
  one: [0, 0],
  two: [0, 0],
  three: [0, 0],
  four: [0, 0],
  five: [0, 0],
  six: [0, 0],
  seven: [0, 0],
  eight: [0, 0],
  nine: [0, 0]
}

location_one = Set[]
location_nine = Set[]
location_one.add('0-0')
location_nine.add('0-0')

moves.split('').each do |move|
  # puts "#{move}----"
  case move
  when 'L'
    loc[:head][0] -= 1
  when 'R'
    loc[:head][0] += 1
  when 'U'
    loc[:head][1] += 1
  when 'D'
    loc[:head][1] -= 1
  end

  loc[:one][0], loc[:one][1] = move_tail(loc[:head][0],
                                         loc[:head][1],
                                         loc[:one][0],
                                         loc[:one][1])

  loc[:two][0], loc[:two][1] = move_tail(loc[:one][0],
                                         loc[:one][1],
                                         loc[:two][0],
                                         loc[:two][1])

  loc[:three][0], loc[:three][1] = move_tail(loc[:two][0],
                                             loc[:two][1],
                                             loc[:three][0],
                                             loc[:three][1])

  loc[:four][0], loc[:four][1] = move_tail(loc[:three][0],
                                           loc[:three][1],
                                           loc[:four][0],
                                           loc[:four][1])

  loc[:five][0], loc[:five][1] = move_tail(loc[:four][0],
                                           loc[:four][1],
                                           loc[:five][0],
                                           loc[:five][1])

  loc[:six][0], loc[:six][1] = move_tail(loc[:five][0],
                                         loc[:five][1],
                                         loc[:six][0],
                                         loc[:six][1])

  loc[:seven][0], loc[:seven][1] = move_tail(loc[:six][0],
                                             loc[:six][1],
                                             loc[:seven][0],
                                             loc[:seven][1])

  loc[:eight][0], loc[:eight][1] = move_tail(loc[:seven][0],
                                             loc[:seven][1],
                                             loc[:eight][0],
                                             loc[:eight][1])

  loc[:nine][0], loc[:nine][1] = move_tail(loc[:eight][0],
                                           loc[:eight][1],
                                           loc[:nine][0],
                                           loc[:nine][1])
  # puts "H #{head_x}, #{head_y}"
  # puts "T #{tail_x}, #{tail_y}"
  # puts "T'#{tail_x}, #{tail_y}"

  location_one.add("#{loc[:one][0]}-#{loc[:one][1]}")
  location_nine.add("#{loc[:nine][0]}-#{loc[:nine][1]}")
end

# 5883
puts location_one.size
puts location_nine.size
