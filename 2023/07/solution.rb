file = File.open("input.txt")
file_data = file.readlines

# ORDERING = "23456789TJQKA"
ORDERING = "J23456789TQKA"

class String
  def hand_type
    #counts = self.split('').each_with_object(Hash.new(0)) { |c,counts| counts[c] += 1 }.values.sort

    counts = self.split('').each_with_object(Hash.new(0)) { |c,counts| counts[c] += 1 }

    if counts.include?("J")
      joker_count = counts.delete("J")

      if joker_count == 5
        # fixing just this specific case
        counts["J"] = 5
      else
        highest_card = counts.max_by{|k, v| v}[0]

        counts[highest_card] += joker_count
      end
    end

    counts = counts.values.sort

    if counts == [5] # five of a kind
      return 7
    elsif counts == [1, 4] # four of a kind
      return 6
    elsif counts == [2, 3] # full house
      return 5
    elsif counts == [1, 1, 3] # three of a kind
      return 4
    elsif counts == [1, 2, 2] # two pair
      return 3
    elsif counts == [1, 1, 1, 2] # one pair
      return 2
    elsif counts == [1, 1, 1, 1, 1] # high card
      return 1
    else
      puts self, counts
      exit
    end
  end

  def <=>(other)
    if self.hand_type > other.hand_type
      return 1
    elsif self.hand_type < other.hand_type
      return -1
    end
    
    # compare by cards
    self.split('').each_with_index {|c, i|
      other_c = other[i]
      
      if ORDERING.index(c) > ORDERING.index(other_c)
        return 1
      elsif ORDERING.index(c) < ORDERING.index(other_c)
        return -1
      end

    }

    return 0
  end
end

bets = {}


file_data.each{|l|
  l.chomp!

  hand, rank = l.split(" ")

  bets[hand] = rank.to_i
}

puts bets

ranked_hands = bets.keys.sort

total = ranked_hands.each_with_index.map{ | hand, index|
  bets[hand] * (index+1)
}.sum

puts total

