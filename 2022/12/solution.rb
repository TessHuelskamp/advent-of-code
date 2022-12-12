# frozen_string_literal: true

file = File.open('2022/12/input.txt')
file_data = file.readlines.map(&:chomp!)

require 'set'

def map_char(char)
  case char
  when 'E'
    26
  when 'S'
    0
  else
    char.ord - 'a'.ord
  end
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

puts start_i, start_j, end_i, end_j

class IHateRuby
  def initialize(heights, start_i, start_j, end_i, end_j)
    @heights = heights
    @shortest_trek = 10_000_000
    @start_i = start_i
    @start_j = start_j
    @end_i = end_i
    @end_j = end_j
  end

  def get_shortest
    @shortest_trek
  end

  def start_dfs
    dfs_search(@start_i, @start_j, 0, [].to_set)
  end

  def list_neighbors(i, j)
    [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]].reject do |b|
      b[0].negative? || b[0] >= @heights.size \
      || b[1].negative? || b[1] > @heights[0].size
    end
  end

  def uniq_id(i, j)
    "#{i}-#{j}"
  end

  def dfs_search(i, j, total, seen)
    if i == @end_i && j == @end_j
      if total < @shortest_trek
        @shortest_trek = total
        puts @shortest_trek
      end
      return
    end

    total += 1

    return if total >= @shortest_trek

    seen.add(uniq_id(i, j))

    list_neighbors(i, j).each do |val|
      ii, jj = val

      next if seen.include? uniq_id(ii, jj)
      next if @heights[ii][jj] - @heights[i][j] > 1

      dfs_search(ii, jj, total, seen.dup)
    end
  end
end

my_map = IHateRuby.new(heights, start_i, start_j, end_i, end_j)
my_map.start_dfs
my_map.get_shortest
