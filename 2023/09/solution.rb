file = File.open("input.txt")
file_data = file.readlines


def figureThingOut(nums)
  values = {0 => nums}
  i = 0

  until values[i].all?(&:zero?)
    previousRow=values[i] 

    newRow = (1...previousRow.length).map{|j|
      previousRow[j] - previousRow[j-1]
    }

    i+=1
    values[i]=newRow
  end

  # add a zero to the last row
  values[i] << 0

  # subtract back in the numbers
  until i.zero?
    #values[i-1] << values[i][-1] + values[i-1][-1]
    x = values[i-1][0] - values[i][0] 
    
    values[i-1].unshift(x)
    i-=1
  end

  # (0...values.length).each{ |j|
  #   puts "#{values[j]}"
  # }
  # puts

  # values[0][-1]
  values[0][0]
end

puts file_data.map{|l|
  l.chomp!

  figureThingOut(l.split(" ").map{|i| i.to_i})
}.sum
