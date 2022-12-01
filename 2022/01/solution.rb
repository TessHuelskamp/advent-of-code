file = File.open("input.txt")
file_data = file.readlines

current_total = 0
max_total = 0

totals = [] 
file_data.each{ |l|
  l.chomp!

  if l.empty?
    totals << current_total
    current_total =0
  else
    current_total += l.to_i
  end
}

totals << current_total


puts totals.sort.last
puts totals.sort.last(3).sum
