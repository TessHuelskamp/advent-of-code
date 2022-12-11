# frozen_string_literal: true

# rubocop:disable Style/Documentation
class Monkey
  def initialize(items, eval_op, test_op, if_true, if_false)
    @items = items
    @eval_op = eval_op
    @test_op = test_op
    @if_true = if_true
    @if_false = if_false
    @total_handled = 0
  end

  # attr_reader eval_op, test_op, if_true, if_false

  def increment_total_handled
    @total_handled += @items.size
  end

  def eval_item(item)
    new_value = if @@part1
                  @eval_op.call(item) / 3
                else
                  @eval_op.call(item) % @@mod_product
                end
    next_monkey_idx = @test_op.call(new_value) ? @if_true : @if_false
    [new_value, next_monkey_idx]
  end

  def get_total_handled
    @total_handled
  end

  def clear_items
    @items.clear
  end

  def get_items
    @items
  end

  def add_item(value)
    @items << value
  end
end

class MonkeyContainer
  def initialize(rounds)
    @rounds = rounds
    @monkeys = {
      0 => Monkey.new(
        [66, 59, 64, 51],
        ->(item) { item * 3 },
        ->(item) { item.even? },
        1,
        4
      ),
      1 => Monkey.new(
        [67, 61],
        ->(item) { item * 19 },
        ->(item) { (item % 7).zero? },
        3,
        5
      ),
      2 => Monkey.new(
        [86, 93, 80, 70, 71, 81, 56],
        ->(item) { item + 2 },
        ->(item) { (item % 11).zero? },
        4,
        0
      ),
      3 => Monkey.new(
        [94],
        ->(item) { item * item },
        ->(item) { (item % 19).zero? },
        7,
        6
      ),
      4 => Monkey.new(
        [71, 92, 64],
        ->(item) { item + 8 },
        ->(item) { (item % 3).zero? },
        5,
        1
      ),
      5 => Monkey.new(
        [58, 81, 92, 75, 56],
        ->(item) { item + 6 },
        ->(item) { (item % 5).zero? },
        3,
        6
      ),
      6 => Monkey.new(
        [82, 98, 77, 94, 86, 81],
        ->(item) { item + 7 },
        ->(item) { (item % 17).zero? },
        7,
        2
      ),
      7 => Monkey.new(
        [54, 95, 70, 93, 88, 93, 63, 50],
        ->(item) { item + 4 },
        ->(item) { (item % 13).zero? },
        2,
        0
      )
    }
  end

  def play_game
    @rounds.times { round }
  end

  def answer
    @monkeys.values.map(&:get_total_handled).max(2).reduce(:*)
  end

  def round
    (0..7).each { |i| monkey_turn(i) }
  end

  def monkey_turn(idx)
    monkey = @monkeys[idx]
    monkey.increment_total_handled

    monkey.get_items.each do |item|
      new_value, next_monkey_idx = monkey.eval_item(item)
      @monkeys[next_monkey_idx].add_item(new_value)
    end

    monkey.clear_items
  end
end
# rubocop:enable Style/Documentation

@@part1 = false
@@mod_product = [2, 7, 11, 19, 3, 5, 17, 13].reduce(:*)

container = MonkeyContainer.new(@@part1 == 3 ? 20 : 10_000)

# Part 1 -  90294
# part 2 - 18170818354
container.play_game
puts container.answer
