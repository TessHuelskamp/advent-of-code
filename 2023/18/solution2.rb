file = File.open("input.sample.txt")
file_data = file.readlines

"""
I gathered this info from reading a bunch of reddit threads and looking at other people's code

We can find the *area* of the box by using the shoelace formula (which is the triangle sum).
The area is *NOT* the answer for us because we need to figure out the number of x,y points inside the area beacuse those correspond with a lava bucket.
We can use the Pick theorem for that.

Then, once we have the number of points in the box, we can add the length of the border to get the answer.

"""
border_length = file_data.map{|l|
  l.chomp!

  l[6,5].to_i(16)
}.sum

i, j = 0, 0
i_j_points = file_data.map{|l|
  l.chomp!

  distance = l[6,5].to_i(16)
  direction = l[11]

  # 0 means R, 1 means D, 2 means L, and 3 means U.
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


i_j_points.each{|p|
  puts "(#{p[0]}, #{p[1]})"
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
    return calc_shoelace_area(points.reverse)
  end
end

# areaOfInterior = interiorPoints + boundrayPoints/2 -1
shoelace_area = calc_shoelace_area(i_j_points)
puts "Shoelace area: #{shoelace_area}"
interiorPoints = shoelace_area - border_length/2 + 1

puts "Interior points: #{interiorPoints}"

# sample input: 952408144115
puts "Polygon Border: #{border_length}"
puts interiorPoints + border_length