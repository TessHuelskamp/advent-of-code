require 'set'

file = File.open("input.txt")
file_data = file.readlines

def idx(i, j)
  "#{i}-#{j}"
end

def get_i(idx)
  idx.split('-').first.to_i
end
def get_j(idx)
  idx.split('-').last.to_i
end


universe = []
emptyCols, emptyRows = Set[], Set[]

file_data.each_with_index{|l, i|
  l.chomp!
  universe << l.split('')
  emptyRows.add(i) unless l.include?("#")
}

(0...universe[0].length).each { |i|
  col = universe.map{ |l| l[i] }.join('')

  emptyCols.add(i) unless col.include?("#")
}

planets = []

(0...universe.length).each { |i|
  (0...universe[0].length).each { |j|
    planets << idx(i,j) if universe[i][j] == "#"
  }
}

res = planets.combination(2).map{|p|
  i0, i1 = get_i(p[0]), get_i(p[1])
  if i0 > i1
    i0, i1 = i1, i0
  end

  j0, j1 = get_j(p[0]), get_j(p[1])
  if j0 > j1
    j0, j1 = j1, j0
  end

  num_col_gaps_walked = (j0..j1).select{|j| emptyCols.include?(j)}.length
  num_row_gaps_walked = (i0..i1).select{|i| emptyRows.include?(i)}.length
  

  # puts "(#{p[0]} #{p[1]})"
  # puts "#{i1 - i0}+#{num_col_gaps_walked}, #{j1-j0}+#{num_row_gaps_walked}"

  (i1-i0)  + (j1-j0) + (num_col_gaps_walked + num_row_gaps_walked) * (1000000-1)
}.sum


# too high
puts res