
inputs = [[44, 208], [80, 1581], [65, 1050], [72, 1102]]

possible_wins=[]


def num_valid(race_time, max_distance)
  total_valid = 0
  (1..race_time-1).each{ |charge_time|
    move_time = race_time - charge_time

    total_valid += 1 if move_time * charge_time > max_distance
  }

  total_valid
end

inputs.each{ |race|
  race_time, max_distance = race

  
  possible_wins << num_valid(race_time, max_distance)
}

race_time = 44806572
max_distance = 208158110501102


puts possible_wins
puts possible_wins.inject(:*)

puts num_valid(race_time, max_distance)