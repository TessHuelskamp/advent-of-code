require 'set'

file = File.open("input.txt")
file_data = file.readlines

nodeChildren = {}
nodeSignalCount={}
flipFlopNodes={}
conjunctionNodes={}
broadcastNode={}

file_data.each{ |l|

  node, children = l.split("->")
  node.strip!
  children.strip!

  if node=='broadcaster'
    nodeType = 'b'
  else
    nodeType=node[0]
    node=node[1,10]
  end

  children = children.split(",").map{|c|
    c.strip
  }

  puts "#{node}=#{children}"

  nodeChildren[node]=children
  nodeSignalCount[node]=0
  children.each{|c|
    nodeSignalCount[c]=0
  }

  case nodeType
  when '%' # flip-flop
    flipFlopNodes[node]=:off
  when '&'
    # we set up the connections to its parent signals later
    conjunctionNodes[node]={}
  when 'b'
    broadcastNode[node]={}
  end
}

# setup conjuction nodes
nodeChildren.keys.each{|source|
  nodeChildren[source].each{|dest|
    if conjunctionNodes.include?(dest)
      conjunctionNodes[dest][source]=:low
    end
  }
}

puts "#{nodeChildren}"
puts "#{flipFlopNodes}"



# beacuse they're processed in FIFO order,
# we can hold all signals in one queue
signals=[]
i=0
pulsesSent = {
  :low => 0, :high => 0
}

until i>=1000
  signals << ["button", :low, "broadcaster"]
  i+=1

  until signals.empty?
    source, signalType, node = signals.shift

    pulsesSent[signalType] += 1

    # puts "#{source} -#{signalType}-> #{node}"

    # todo bump up signal received
    next unless nodeChildren.include?(node)
    nextPulse = :low

    if broadcastNode.include?(node)
      nextPulse = signalType
    elsif flipFlopNodes.include?(node)
      next if signalType == :high

      old = flipFlopNodes[node]
      
      if flipFlopNodes[node] == :off
        flipFlopNodes[node] = :on
        nextPulse = :high
      else
        flipFlopNodes[node] = :off
        nextPulse = :low
      end

      # puts "#{flipFlopNodes}"
      # puts "#{node}-#{old}-#{nextPulse}" 
    elsif conjunctionNodes.include?(node)
      conjunctionNodes[node][source]=signalType

      allHigh = conjunctionNodes[node].values.all?{|p| p == :high}
      nextPulse = allHigh ? :low : :high

     # puts "#{node} #{allHigh} #{nextPulse}"
    end

    nodeChildren[node].each{|dest|
      signals << [node, nextPulse, dest]
    }
  end
end

puts pulsesSent[:low] * pulsesSent[:high]