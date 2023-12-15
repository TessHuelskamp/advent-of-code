


require 'set'

class String
  def is_i?
     /\d/ === self
  end

  def is_char?
    self != "." && !self.is_i?
  end

  def is_gear?
    self == "*"
  end
end


file = File.open('input.txt')
file_data = file.readlines.map { |l| l.chomp.split('') }

validNumbers = []

def get_gear_id(i, j)
  "#{i}-#{j}"
end

gearPairs = {}


(0..file_data.size-1).each {|i|
  row = file_data[i]
  skip = Set[]

  (0..row.length-1).each{|j|
    next if skip.include?(j)
    char = file_data[i][j]
    next unless char.is_i?

    end_of_num = 0
    (j..row.length-1).each{ |k|
      if file_data[i][k].is_i?
        end_of_num = k
        skip.add(k)
      else
        break
      end
    }

    number = file_data[i][j, end_of_num-j+1].join.to_i

    to_check = []
    (i-1..i+1).each{|ii|
      (j-1..end_of_num+1).each{|jj|
        to_check << [ii, jj]
      }
    }

    to_check = to_check.select{ |c|
      ii, jj = c
      (0..file_data.size-1).include?(ii) && (0..file_data[0].length-1).include?(jj)
    }

    nearChar = to_check.any?{ |c|
      ii, jj = c
      file_data[ii][jj].is_char?
    }
   
    validNumbers << number if nearChar


    # check for gear ids

    gear = to_check.select{ |c|
      ii, jj = c
      file_data[ii][jj].is_gear?
    }.first

    next if gear.nil?

    gear_id = get_gear_id(gear[0], gear[1])

    if !gearPairs.keys.include?(gear_id)
      gearPairs[gear_id] = []
    end

    gearPairs[gear_id] << number

  }

}

puts validNumbers.sum

gearPairs.values.select{|p|
  p.length == 2
}.map{ |p|
  p[0]*p[1]
}.sum

