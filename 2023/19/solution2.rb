file = File.open("input.txt")
file_data = file.readlines

$ruleset = {}

file_data.each{|l|
  l.chomp!
  l.chomp!("}")

  break if l ==""

  ruleName, rule = l.split("{")

  rules = rule.split(",").map{ |r|
    if r.include?(">")
      something, destination = r.split(":")
      feature, value = something.split(">")
      [feature, ">", value.to_i, destination]
    elsif r.include?("<")
      something, destination = r.split(":")
      feature, value = something.split("<")
      [feature, "<", value.to_i, destination]
    else
      [r]
    end
  }

  $ruleset[ruleName] = rules
}

def split(range, val)
  [range.select{|x| x <= val}, range.select{|x| val < x}]
end

def countNumAccepted(instruction, ranges)
  if instruction == "R"
    return 0
  elsif instruction == "A"
    return ranges.values.map{|x| x.length}.inject(:*)
  end

  rules = $ruleset[instruction]

  total = 0
  rules.each{|rule|
    if rule.length == 1
      total += countNumAccepted(rule.first, ranges)
      break
    end

    feature, comparison, value, destination = rule
    
    valueOffset = if comparison == "<"
      -1
    else
      0
    end

    left, right = split(ranges[feature], value+valueOffset)

    if comparison == "<"
      newRange = ranges.clone
      newRange[feature] = left
      ranges[feature] = right
    else  # >
      newRange = ranges.clone
      newRange[feature] = right
      ranges[feature] = left
    end

    total += countNumAccepted(destination, newRange)
  }

  return total
end


startingRanges = {
  'x' => (1..4000).to_a,
  'm' => (1..4000).to_a,
  'a' => (1..4000).to_a,
  's' => (1..4000).to_a,
}

puts countNumAccepted("in", startingRanges)