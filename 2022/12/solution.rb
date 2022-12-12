# frozen_string_literal: true

file = File.open('2022/12/input.txt')
file_data = file.readlines.map(&:chomp!)

require 'set'

def map_char(char)
  case char
  when 'E'
    char = 'a'
  when 'S'
    char = 'z'
  end

  char.ord - 'a'.ord
end

start_i = 0
start_j = 0
end_i = 0
end_j = 0

heights = file_data.reject(&:nil?).map.with_index do |line, i|
  line.split('').each.with_index do |char, j|
    case char
    when 'S'
      start_i = i
      start_j = j
    when 'E'
      end_i = i
      end_j = j
    end
  end

  line.split('').map { |c| map_char(c) }
end

class IHateRuby
  def initialize(heights, start_i, start_j, end_i, end_j)
    @heights = heights
    @start_i = start_i
    @start_j = start_j
    @end_i = end_i
    @end_j = end_j

    @shortest_path_cache = []
    @heights.size.times do
      row = []
      @heights[0].size.times { row << 100_000 }
      @shortest_path_cache << row
    end
  end

  def shortest
    @shortest_path_cache[@end_i][@end_j]
  end

  def list_neighbors(i, j)
    [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].reject do |b|
      b[0].negative? || b[0] >= @heights.size \
      || b[1].negative? || b[1] > @heights[0].size
    end
  end

  def traverse
    # heap?
    to_visit = [[@start_i, @start_j, 0]]
    to_visit_set = [[@start_i, @start_j, 0]].to_set

    while to_visit.size.positive?
      i, j, cost = to_visit.first
      to_visit.delete_at(0)
      #   puts "#{i} #{j} #{cost}, #{to_visit.take(10)}" if rand(0..1000).zero?

      next if @shortest_path_cache[i][j] <= cost

      @shortest_path_cache[i][j] = cost

      list_neighbors(i, j).each do |val|
        ii, jj = val

        next if @shortest_path_cache[ii][jj].nil?
        next if @shortest_path_cache[ii][jj] <= cost
        next if @heights[ii][jj] - @heights[i][j] > 1
        next if to_visit_set.include?([ii, jj, cost + 1])

        to_visit_set.add([ii, jj, cost + 1])
        to_visit << [ii, jj, cost + 1]
      end
    end
  end

  def print_map
    @shortest_path_cache.each do |line|
      puts line.join(',')
    end
  end
end

# puts heights.size * heights[0].size
my_map = IHateRuby.new(heights, start_i, start_j, end_i, end_j)
my_map.traverse
# my_map.print_map

puts my_map.shortest

# too high = 1128
# too high 352, 351
