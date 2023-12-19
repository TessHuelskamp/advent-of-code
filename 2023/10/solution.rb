file = File.open("input.txt")
file_data = file.readlines

def maze_id(i, j)
  "#{i}-#{j}"
end

def maze_tupel_id(ij)
  "#{ij[0]}-#{ij[1]}"
end

maze = []
starting_i, starting_j = 0, 0

file_data.each_with_index{|l, i|
  l.chomp!
  maze << l.split('')

  next unless l.include?("S")
  starting_i = i
  starting_j = l.index("S")

}

# by inspection my maze goes down and right
distances = {}


distances[maze_id(starting_i,starting_j)] = 0

next_a_i, next_a_j, incoming_a_direction = starting_i+1, starting_j, "down"
next_b_i, next_b_j, incoming_b_direction = starting_i, starting_j+1, "right"

def possible_moves(i, j, pipe)
  case pipe
  when "|"
    return [[i-1, j], [i+1, j]]
  when "-"
    return [[i, j-1], [i, j+1]]
  when "F"
    return [[i+1, j], [i, j+1]]
  when "L"
    return [[i-1, j], [i, j+1]]
  when '7'
    return [[i+1, j], [i, j-1]]
  when 'J'
    return [[i-1, j], [i, j-1]]
  end
end


distance = 1

until distances.include?(maze_id(next_a_i,next_a_j))
  distances[maze_id(next_a_i,next_a_j)] = distance
  distance += 1

  current_pipe = maze[next_a_i][next_a_j]

  puts "(#{next_a_i}, #{next_a_j}) #{current_pipe} in:#{incoming_a_direction}"

  move_x, move_y = possible_moves(next_a_i, next_a_j, current_pipe)

  if distances.include?(maze_tupel_id(move_x))
    next_a_i, next_a_j = move_y
  else
    next_a_i, next_a_j = move_x
  end


end

puts "(#{next_a_i}, #{next_a_j})"
puts distances.include?(maze_id(next_a_i,next_a_j))
puts distances

puts distances.max_by{|k, v| v}[1]/2 +1

# https://en.wikipedia.org/wiki/Point_in_polygon
enclosed_values = 0
(1..maze.length-1).each{|i|
  maze_crosses = 0

  (1..maze.length-1).each{|j|
    maze_value = maze[i][j]
    
    if distances.include?(maze_id(i, j))
      maze_crosses+=1 if "|JL".include?(maze_value)
    else
      enclosed_values += 1 if maze_crosses%2 == 1
    end
  }
}

puts enclosed_values