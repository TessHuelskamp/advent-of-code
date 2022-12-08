# frozen_string_literal: true

require 'set'

file = File.open('2022/08/input.txt')
file_data = file.readlines.map { |l| l.chomp.split('').map(&:to_i) }

visible = Set[]

height = file_data.size
width = file_data.size

# right to left
# left to right
# top to bottom
# bottom to top

(0..height - 1).each do |i|
  largest_seen = -1
  (0..width - 1).each do |j|
    tree = file_data[i][j]

    if tree > largest_seen
      visible.add("#{i}-#{j}")
      largest_seen = tree
    end

    next if tree == 9
  end

  largest_seen = -1
  (width - 1).downto(0).each do |j|
    tree = file_data[i][j]
    if tree > largest_seen
      visible.add("#{i}-#{j}")
      largest_seen = tree
    end

    next if tree == 9
  end
end

# copy but swap i and j

(0..height - 1).each do |j|
  largest_seen = -1
  (0..width - 1).each do |i|
    tree = file_data[i][j]

    if tree > largest_seen
      visible.add("#{i}-#{j}")
      largest_seen = tree
    end

    next if tree == 9
  end

  largest_seen = -1
  (width - 1).downto(0).each do |i|
    tree = file_data[i][j]
    if tree > largest_seen
      visible.add("#{i}-#{j}")
      largest_seen = tree
    end

    next if tree == 9
  end
end

puts visible.size

largest_viewing_score = 0

def viewing_score(trees, i, j)
  return 0 if i.zero? || j.zero? || i == 99 - 1 || j == 99 - 1

  total = 1

  tree_size = trees[i][j]

  (i + 1..99 - 1).each do |ii|
    if trees[ii][j] >= tree_size
      total *= i - ii
      break
    end

    total *= i - ii if ii == 99 - 1
  end

  (i - 1).downto(0).each do |ii|
    if trees[ii][j] >= tree_size
      total *= i - ii
      break
    end

    total *= i - ii if ii == 0
  end

  (j + 1..99 - 1).each do |jj|
    if trees[i][jj] >= tree_size
      total *= j - jj
      break
    end

    total *= j - jj if jj == 99 - 1
  end

  (j - 1).downto(0).each do |jj|
    if trees[i][jj] >= tree_size
      total *= j - jj
      break
    end

    total *= j - jj if jj == 0
  end

  total.abs
end

(1..height - 1 - 1).each do |i|
  (1..width - 1 - 1).each do |j|
    largest_viewing_score = [largest_viewing_score, viewing_score(file_data, i, j)].max
  end
end

puts largest_viewing_score
# wrong 2160
# 4224
