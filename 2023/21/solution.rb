file = File.open("input.txt")
file_data = file.readlines


starting_i, starting_j = 0, 0
$garden = file_data.map.with_index{|l, i|
  l.chomp!

  if l.include?('S')
    starting_i = i
    starting_j = l.index('S')
  end
  l.split('')
}

def getCell(i, j)
  gardenLength = $garden.length
  gardenWidth = $garden[0].length

  i %=gardenLength
  j %=gardenWidth

  [i, j]
end




def nextSteps(i, j)
  [[i-1, j], [i+1, j], [i, j-1], [i, j+1]].select{|p| 
    i, j = getCell(*p)

    $garden[i][j] != "#"
  }
end

currentOptions = [[starting_i, starting_j]]

s=0
until s==500
  nextOptions = []

  currentOptions.each{|p|
    nextOptions += nextSteps(*p)
  }

  currentOptions = nextOptions.uniq
  s+=1

  puts "#{s} #{currentOptions.length}"
end

# currentOptions.each{|o|
#   puts "#{o}"
# }

def prettyprint
  width = [$garden[0].length, 90].min
  (0...$garden.length).each {|i|
    puts (0..width).map{ |j|
      if currentOptions.include?([i, j])
        "O"
      else
        $garden[i][j]
      end
    }.join('')

  }
end

#puts currentOptions.length