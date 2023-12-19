require 'set'

file = File.open("input.txt")
file_data = file.readlines

$board = file_data.map{ |l|
  l.chomp!
  l.split('')
}

# board.each{|l|
#   puts l.join('')
# }

def nextDirections(direction, cell)
  leftArrow = {
    :right => :down, :down => :right,
    :left => :up, :up => :left
  }

  rightArrow = {
    :right => :up, :up => :right,
    :down => :left, :left => :down
  }

  case cell
  when "."
    [direction]
  when "\\"
    [leftArrow[direction]]
  when "/"
    [rightArrow[direction]]
  when "-"
    if direction==:right || direction == :left
      [direction]
    else
      [:right, :left]
    end
  when "|"
    if direction==:up || direction == :down
      [direction]
    else
      [:up, :down]
    end
  else
    puts "oh no: #{direction} #{cell}"
    raise Exception
  end

end

def runBoard(i, j, direction)
  # to account for the fact that light can go up and down,
  # we include a direction to our nodes that we'll tease out at the end
  toVisit=[[i, j, direction]]
  seen=Set[]

  until toVisit.empty?
    currentTuple = toVisit.shift
    seen.add(currentTuple)

    # puts "#{currentTuple}"

    i, j, direction = currentTuple
    cell = $board[i][j]

    nextDirections(direction, cell).each{|nextDirection|
      nextI = i
      nextJ = j
      case nextDirection
      when :up
        nextI-=1
      when :down
        nextI+=1
      when :right
        nextJ+=1
      when :left
        nextJ -=1
      end

      if nextI <0 || nextI >=$board.length \
        || nextJ <0 || nextJ >=$board[0].length
        next
      end

      nextTuple = [nextI, nextJ, nextDirection]

      toVisit << nextTuple unless seen.include?(nextTuple)
    }
  end

  seen.map{|s| "#{s[0]}-#{s[1]}"}.uniq.length
end

def part2
  possibleInputs = []

  (0...$board.length).each{|i|
    possibleInputs << [i, 0, :right]
    possibleInputs << [i, $board[0].length-1, :left]
  }

  (0...$board[0].length).each {|j|
    possibleInputs << [0, j, :down]
    possibleInputs << [$board.length-1, j, :up]
  }

  possibleInputs.map{|input|
    runBoard(*input)
  }.max
end


puts "part 1: #{runBoard(0, 0, :right)}"
puts "part 2: #{part2}"
