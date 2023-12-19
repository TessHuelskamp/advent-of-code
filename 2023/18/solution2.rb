file = File.open("input.txt")
file_data = file.readlines

"""
I gathered this info from reading a bunch of reddit threads and looking at other people's code

We can find the *area* of the box by using the shoelace formula (which is the triangle sum).
The area is *NOT* the answer for us because we need to figure out the number of x,y points inside the area beacuse those correspond with a lava bucket.
We can rearrange the pick theorm with the area we have to solve for the number of dots in the polygon

Then, once we have the number of points in the box, we can add the length of the border to get the answer.
"""

i, j = 0, 0
border_length = 0
i_j_points = file_data.map{|l|
  l.chomp!

  color = l.split(" ").last
  distance = color[2,5].to_i(16)
  direction = color[7]

  border_length += distance

  case direction
  when "U", "3"
    i+=distance
  when "D", "1"
    i-=distance
  when "L", "2"
    j-=distance
  when "R", "0"
    j+=distance
  end

  [i, j]
}

def calc_shoelace_area(points)
  area = points.map.with_index{|p, i|
    i1, j1 = p
    i2, j2 = points[(i+1)%points.length]

    i1 * j2 - i2 * j1
  }.sum

  if area.positive?
    return area/2
  else
    # if the order is not given counterclockwise you need to reverse it
    calc_shoelace_area(points.reverse)
  end
end

shoelace_area = calc_shoelace_area(i_j_points)
puts "Shoelace area: #{shoelace_area}"

# original Pick theorm
# areaOfInterior = interiorPoints + boundrayPoints/2 -1
interiorPoints = shoelace_area - border_length/2 + 1

puts "# of interior points: #{interiorPoints}"

puts "Polygon Border: #{border_length}"
puts "Answer: #{interiorPoints + border_length}"
