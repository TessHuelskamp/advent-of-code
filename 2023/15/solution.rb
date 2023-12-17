file = File.open("input.txt")
file_data = file.readlines

instructions = file_data[0].chomp.split(',')


def hash(line)
  value = 0
  line.split('').each{|c|
    value += c.ord
    value*=17
    value%=256
  }
  value
end

part1 = instructions.map{|l| hash(l)}.sum
puts part1

# part2
lenses = {}
(0...256).each{|i|
  lenses[i]=[]
}

instructions.each{|l|
  minus = l.include?("-")

  lensID=''
  if minus
    lensID = l.split('-').first
  else
    lensID = l.split('=').first
  end
  hashID = hash(lensID)

  # find index
  idx = -1
  lenses[hashID].each_with_index{|v, i|
    idx = i if v[0] == lensID
  }

  if minus
    lenses[hashID].delete_at(idx) if idx>=0
  else
    focalLength = l.split("=").last.to_i

    if idx >= 0
      lenses[hashID][idx][1]=focalLength
     else
      lenses[hashID] << [lensID, focalLength]
     end
  end
}

puts lenses.map{ |k, v|
  v.map.with_index{ |l, i|
    (k+1) * (i+1) * l[1]
  }.sum
}.sum