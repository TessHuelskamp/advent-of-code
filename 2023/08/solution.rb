file = File.open("input.txt")
file_data = file.readlines
$route = "LRRLRRLRRLRRRLRRLRRRLRRLRRRLRLRLLRLRLRRLLLRLRLRRRLRRLRLRRRLRRLRRLRRLLLRRLRRRLRRRLRLLRRLRLLRRLRRRLRRLRLRRRLRLRLRRLRLRRRLLRRRLLRRRLRLRRRLRRLLRRLRRRLRRLRRLLRRLRRLRRRLLLRRRLRRLRRLRRLRLRRRLRRLLLLRLRRLRRRLRLLRRLRLLRRLRRRLRRRLRRRLLRRLRRLRRLRRRLRRLRRRLLRLRRRLRRRLRRRLLRRRLRRLRRRR"

$nodes = {}

file_data.each{ |l|
  source, destinations = l.chomp.split("=")

  puts (destinations)

  source = source[0,3]
  left=destinations[2, 3]
  right=destinations[7, 3]

  $nodes[source] = [left, right]
}

steps = 0
current_node = "AAA"

puts $nodes

while current_node != "ZZZ"
  direction = $route[steps % $route.length]

  previous_node = current_node
  
  case direction
  when "L"
    current_node = $nodes[current_node][0]
  when "R"
    current_node = $nodes[current_node][1]
  end

  steps+=1
end

puts steps

# Part 2
def find_shortest_route(current_node)
  steps = 0
  until current_node[-1] == "Z"
    direction = $route[steps % $route.length]
    
    case direction
    when "L"
      current_node = $nodes[current_node][0]
    when "R"
      current_node = $nodes[current_node][1]
    end
  
    steps+=1
  end
  
  steps
end


starting_nodes = $nodes.keys.filter{|n| n[-1]=="A"}
shortest_routes = starting_nodes.map{|n| find_shortest_route(n)}

puts shortest_routes.inject(:lcm)

