file = File.open("input.txt")
file_data = file.readlines

results_1 = []
points = {}
cards = {}

original_cards = file_data.size


file_data.each{ |l|
  l.chomp!
  
  card, game = l.split(":")
  card_id = card.split(" ")[1].to_i

  puts card_id

  winning_numbers, have = game.split("|")

  winning_numbers = winning_numbers.split(" ")
  have = have.split(" ")

  num_wins = (winning_numbers & have).size

  if num_wins >=1
    results_1 << 2**(num_wins-1)
  end

  points[card_id] = num_wins
  cards[card_id] = 1
}

cards.keys.sort.each{ |card_id|
  point = points[card_id]

  (card_id+1..card_id+point).each{ |next_card_id|
    cards[next_card_id] += cards[card_id]
  }
}

puts results_1.sum

puts cards.values.sum
