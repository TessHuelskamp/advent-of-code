require 'set'

file = File.open("input.txt")
file_data = file.readlines

puzzles = []
puzzle = []

file_data.each{|l|
  l.chomp!
  if l== ''
    puzzles << puzzle
    puzzle = []
  else
    puzzle << l.split('')
  end
}
puzzles << puzzle

total = 0

r = puzzles.map{|p|
  value = 0

  # check rows
  (1...p.length).each { |i|
    next if value > 0
    delta = 0
    editDistance=0
    until i-1-delta < 0 || i+delta >= p.length
      rowa = p[i-1-delta].join('')
      rowb = p[i+delta].join('')


      editDistance+= DidYouMean::Levenshtein.distance(rowa, rowb)
      delta+=1
    end

    if editDistance == 1
      value = i*100
    end
  }

  # check cols
  (1...p[0].length).each {|j|
    next if value > 0

    delta = 0
    editDistance=0
    until j-1-delta < 0 || j+delta >= p[0].length
      cola, colb = [], []
      p.each{|r|
        cola << r[j-1-delta]
        colb << r[j+delta]
      }

      editDistance+= DidYouMean::Levenshtein.distance(cola.join(''), colb.join(''))
      delta+=1
    end

    if editDistance==1
      value = j
    end
  }

  # if value < 100
  #   p.each{|r|
  #     puts r.join('')
  #   }
  #   puts value
  #   puts
  # end
  
  value
  # check for row
  # check for col
}.sum

puts r