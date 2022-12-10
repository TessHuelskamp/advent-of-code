# frozen_string_literal: true

file = File.open('2022/10/input.txt')
file_data = file.readlines.map(&:chomp!)

clock = 1
register = 1
signal_strength = 0
idx = 0
to_add = 0
holding = false
drawing = ''

cycles = [20, 60, 100, 140, 180, 220]

while clock < 240 + 1

  signal_strength += clock * register if cycles.include?(clock)

  drawing_idx = (clock - 1) % 40

  drawing += if drawing_idx - 1 == register || drawing_idx == register || drawing_idx + 1 == register
               '#'
             else
               '.'
             end

  unless to_add.zero?
    register += to_add
    to_add = 0
  end

  # current_instruction = if holding
  #                         '--'
  #                       else
  #                         file_data[idx]
  #                       end

  # puts "[#{clock}] #{register} #{holding} #{to_add} #{idx}-#{current_instruction}"

  # check if still adding
  if holding
    clock += 1
    holding = false
    next
  end

  instruction = file_data[idx]
  idx += 1

  if ['noop', ''].include?(instruction)
    clock += 1
    next
  end

  if instruction.nil?
    clock += 1
    next
  end

  to_add = instruction.split(' ').last.to_i
  clock += 1
  holding = true

end

# 11220
puts signal_strength

rows = drawing.scan(/.{40}/)
rows.each { |r| puts r }
# BZPAJELK
