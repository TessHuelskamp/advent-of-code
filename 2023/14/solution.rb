file = File.open("input.txt")
file_data = file.readlines

$mirror = file_data.map{|l|
  l.chomp!
  l.split('')
}

def generateRockString(og_string, reverse=false)
  if reverse
    og_string.reverse!
  end

  sorted_string = og_string.split("#").map{|s|
    # '.' becomes before 'O' in sort
    s.split('').sort.reverse.join('')
  }.join('#')

  # join removes the last #s but not the first ones
  corrected_string = sorted_string.ljust(og_string.length, '#')

  if reverse
    corrected_string.reverse!
  end
  corrected_string
end


def move_updown(north=true)
  (0...$mirror[0].length).each{|j|
    # turn each col into a string, manipulate it, then put it back
    column_string = (0...$mirror.length).to_a.map{|i|
      $mirror[i][j]
    }.join('')

    reverse = !north
    newString = generateRockString(column_string, reverse)

    (0...$mirror.length).each{|i|
      $mirror[i][j] = newString[i]
    }
  }
end

def move_rightleft(west=true)
  (0...$mirror.length).each{|i|
    row_string = $mirror[i].join('')

    reverse = !west
    newString = generateRockString(row_string, reverse)

    (0...$mirror[0].length).each{|j|
      $mirror[i][j] = newString[j]
    }
  }
end

def cycle()
  move_updown(north=true)
  move_rightleft(west=true)
  move_updown(north=false)
  move_rightleft(west=false)
end

def calculateLoad
  (0...$mirror.length).map{|i|
    rockCost = $mirror.length-i
    $mirror[i].count{|c| c=="O"} * rockCost
  }.sum
end

def prettyprint
  $mirror.each{|l|
    puts "#{l.join("")}"
  }
  puts
end

def boardState
  $mirror.map{|row|
    row.join('')
  }.join('-')
end


def figureOutLastLoad
  goal=1000000000
  previousStates={}
  i=0
  cycleSize=0
  until i==goal
    cycle()
    i+=1

    currentState = boardState

    if previousStates.include?(currentState)
      puts "previous", previousStates[currentState]
      puts "now", i
      cycleSize=i-previousStates[currentState]
      break
    else
      previousStates[currentState]=i
    end
  end

  # bump up i in cycle sizes to get close to number
  numBumps = (goal-i-2*cycleSize)/cycleSize

  i+=numBumps*cycleSize

  until i==goal
    cycle()
    i+=1
  end


end
  

figureOutLastLoad


puts calculateLoad