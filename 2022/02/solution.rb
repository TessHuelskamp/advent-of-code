# frozen_string_literal: true

file = File.open('input.txt')
file_data = file.readlines

values = {
  A: :rock,
  B: :paper,
  C: :scissors,
  X: :rock,
  Y: :paper,
  Z: :scissors
}

points = {
  rock: 1,
  paper: 2,
  scissors: 3
}

def score(opp, me)
  if opp == me
    3
  elsif me == :rock && opp == :scissors
    6
  elsif me == :paper && opp == :rock
    6
  elsif me == :scissors && opp == :paper
    6
  else
    0
  end
end

total_a = 0

file_data.each do |l|
  l.chomp!

  them, me = l.split(' ')

  their_move = values[them.to_sym]
  my_move = values[me.to_sym]

  total_a += points[my_move]
  total_a += score(their_move, my_move)
end

puts total_a

result = {
  X: :lose,
  Y: :draw,
  Z: :win
}

def should_play(their_move, my_result)
  win_move = {
    rock: :paper,
    paper: :scissors,
    scissors: :rock
  }

  lose_move = {
    paper: :rock,
    scissors: :paper,
    rock: :scissors
  }

  case my_result
  when :draw
    their_move
  when :win
    win_move[their_move]
  when :lose
    lose_move[their_move]
  else
    raise Exception('no again')
  end
end

def game_result(result)
  case result
  when :draw
    3
  when :win
    6
  when :lose
    0
  else
    raise Exception('no')
  end
end

total_b = 0

file_data.each do |l|
  them, me = l.split(' ')
  their_move = values[them.to_sym]
  my_result = result[me.to_sym]

  my_move = should_play(their_move, my_result)

  puts(their_move, my_result, my_move, points[my_move], game_result(my_result))

  total_b += game_result(my_result)
  total_b += points[my_move]
end

puts total_b
