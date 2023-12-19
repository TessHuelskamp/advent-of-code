file = File.open("input.txt")
file_data = file.readlines

ruleset = {}
toProcess = []
accepted = []
rejected = []

firstWorkflow = "in"
processParts = false

file_data.each{|l|
  l.chomp!
  l.chomp!("}")

  if l == ""
    processParts = true
    next
  end

  if processParts
    _, l = l.split("{")
    part = {}
    l.split(",").each{|p|
        feature, value = p.split("=")
        part[feature] = value.to_i
    }

    toProcess << [firstWorkflow, part]

  else
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

    ruleset[ruleName] = rules
  end
}

puts ruleset

until toProcess.empty?
  ruleName, part = toProcess.shift
  result = ''

  puts ruleName

  ruleset[ruleName].each {|r|
    if r.length == 1
      result = r.first
    else
      feature, comparison, value, destination = r

      if comparison == "<"
        result = destination if part[feature] < value
      else
        result = destination if part[feature] > value
      end
    end

    break if result.length > 0
  }

  case result
  when 'A'
    accepted << part
  when 'R'
    rejected << part
  else
    toProcess << [result, part]
  end

end

puts accepted.map{|p|
  "xmas".split("").map{ |c|
    p[c]
  }.sum
}.sum