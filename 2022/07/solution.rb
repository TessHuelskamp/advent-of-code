# frozen_string_literal: true

# rubocop:disable Style/GlobalVars
# rubocop:disable Metrics/MethodLength

file = File.open('2022/07/input.txt')
file_data = file.readlines

file_system = { '/' => {} }
path = []

file_data.each do |line|
  line.chomp!
  commands = line.split(' ')

  if line.include? '$'

    # commands
    _, command, arg = commands
    case command
    when 'ls'
      # do nothing
    when 'cd'
      if arg == '..'
        path.pop
      else
        path.push(arg)
      end
    end
  else
    # the result of ls
    current_dir = file_system.dig(*path)
    arg1, arg2 = commands

    current_dir[arg2] = if arg1 == 'dir'
                          {}
                        else
                          arg1
                        end

  end
end

# Convert the existing fs into a thing DFS

$total_small_bois = 0
$directory_sizes = []

def dfs_search(file_system, path)
  current_dir = file_system.dig(*path)

  directory_total = 0

  current_dir.each_key do |sub_dir|
    value = current_dir[sub_dir]

    directory_total += if value.is_a?(Hash)
                         dfs_search(file_system, path.dup.push(sub_dir))
                       else
                         value.to_i
                       end
  end

  $total_small_bois += directory_total if directory_total <= 100_000
  $directory_sizes << directory_total

  directory_total
end

full_total = dfs_search(file_system, ['/'])

puts "size of all the small bois #{$total_small_bois}"

unused_space = 70_000_000 - full_total
to_delete = 30_000_000 - unused_space
puts "needed to clear up #{to_delete}"

smallest_delete = $directory_sizes.select { |n| n > to_delete }.min

puts "smallest delete is #{smallest_delete}"

# rubocop:enable Style/GlobalVars
# rubocop:enable Metrics/MethodLength
