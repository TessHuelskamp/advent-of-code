require 'set'
DELIM = ":"

class String
  def to_ii
    self.split(DELIM).first.to_i
  end

  def to_jj
    self.split(DELIM).last.to_i
  end
end

def idx(i, j)
  "#{i}#{DELIM}#{j}"
end

file = File.open("input.txt")
file_data = file.readlines

"""
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
"""

$border = Set[]
$cells = Set[]

i, j = 0, 0

$border.add(idx(i, j))
$cells.add(idx(i, j))

file_data.each{|l|
  l.chomp!
  direction, number, _ = l.split(" ")
  number = number.to_i

  (1..number).each {
    case direction
    when "U"
      i-=1
    when "D"
      i+=1
    when "L"
      j-=1
    when "R"
      j+=1
    end

    $border.add(idx(i, j))
    $cells.add(idx(i, j))
  }
}

$is = $border.map{|c| c.to_ii}
$js = $border.map{|c| c.to_jj}

def prettyPrint(width)
  maxj = [$js.min-1+width, $js.max+1].min
  (($is.min-1)..($is.max+1)).each{|i|
    puts (($js.min-1)..(maxj)).map{|j|
      c = if $border.include?(idx(i, j))
        "#"
      elsif $cells.include?(idx(i,j))
        "x"
      else
        "."
      end

      c
    }.join('')
  }
end

def flood_fill(i, j)
  toVisit = [[i, j]]

  until toVisit.empty?
    i, j = toVisit.shift
    next if $cells.include?(idx(i, j))

    $cells.add(idx(i, j))
    [[i-1, j], [i+1, j], [i, j-1], [i, j+1]].each{ |p|
      toVisit << p unless $border.include?(idx(p[0], p[1])) || $cells.include?(idx(p[0], p[1]))
    }
  end
end

puts "#{$is.min},#{$is.max} #{$js.min},#{$js.max}"


# ray and flood fill
# I added extra padding to the ray algo to ensure we start /outside/ of the box
(($is.min-1)..($is.max+1)).each{|i|
  inBox = 0
  (($js.min-1)..($js.max+1)).each{|j|
    
    isBorder = $border.include?(idx(i,j))
    prevIsBorder = $border.include?(idx(i,j-1))

    # We only traverse a border when the left and right cells differ
    # Also - to make sure it's not an edge, we need the border to look like this
    """
    ..#..
    ..###
    ....#
    
    and not this
    ..#..#
    ..####
    we also need to figure out plain walls
    .#.
    .#.
    .#.
    """

    if prevIsBorder && !isBorder
      # this could be better... it could be worse tho
      if !$border.include?(idx(i,j-2)) # wall
        inBox += 1
      else
        # figure out if current thing is up or down
        isTop = $border.include?(idx(i-1,j-1))

        lastBorder = false
        prevIsTop = false
        jj = j-2
        until lastBorder
          if $border.include?(idx(i,jj-1))
            jj-=1
          else
            prevIsTop = $border.include?(idx(i-1,jj))
            lastBorder = jj
          end
        end

        inBox += 1 if prevIsTop ^ isTop
      end
    end

    if inBox%2==1
      flood_fill(i, j) unless $border.include?(idx(i, j))
    end
  }
}

prettyPrint(150)


puts "Part 1: #{$cells.length}"