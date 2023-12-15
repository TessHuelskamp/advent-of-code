file = File.open("input.txt")

file_data = file.readlines

maximums = {
  "red" => 12,
  "green" => 13,
  "blue" => 14
}

possible_games = []
powers = []

file_data.each{ |l|
  
  game, rounds = l.split(":")
  _, game_id = game.split(" ")
  game_id = game_id.to_i

  possible = true

  discovered_max = {
    "red" => 0,
    "green" => 0,
    "blue" => 0
  }
  
  rounds.split(";").each{ |round|
    round.split(",").each { |balls|
      num, color = balls.split(" ")
      num = num.to_i

      if num.to_i > maximums[color]
        possible = false
      end

      if num.to_i > discovered_max[color]
        discovered_max[color] = num.to_i
      end
    }
  }

  possible_games << game_id if possible

  powers << discovered_max.values.inject(:*)
}

puts "part1 ", possible_games.sum
puts "part2 ", powers.sum





