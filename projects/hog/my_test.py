from hog import *
from dice import make_test_dice


# free_bacon(0)
# free_bacon(1)
# free_bacon(2)
# free_bacon(80)
#Test of problem3
# print(take_turn(2, 0, make_test_dice(4, 5, 1)))
# print(take_turn(3, 0, make_test_dice(4, 6, 1)))
# print(take_turn(0, 2))
# print(take_turn(0, 0))

# print(swine_align(2, 4))
# print(swine_align(11, 22))
# print(swine_align(36, 24))
# print(swine_align(27, 13))
# print(swine_align(23, 22))
# print(swine_align(15, 45))
# print(swine_align(15, 0))

# Test for problem5 play()
"""
test 1
always_three = make_test_dice(3)
always = always_roll
# Play function stops at goal

s0, s1 = play(always(5), always(3), 91, 10, always_three)
print(s0,s1)

test2
import hog
always_three = hog.make_test_dice(3)
always = hog.always_roll

# Goal score is not hardwired
s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
print(s0,s1)

test3
import hog
always_three = hog.make_test_dice(3)
always_seven = hog.make_test_dice(7)

# Use strategies
# We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
strat0 = lambda score, opponent: opponent % 10
strat1 = lambda score, opponent: max((score // 10) - 4, 0)
s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
print(s0,s1)
"""
def echo(s0, s1):
    print(s0, s1)
    return echo

s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)



def count(n):
     def say(s0, s1):
         print(n, s0)
         return count(n + 1)
     return say
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=10, say=count(1))



def echo(s0, s1):
    print(s0, s1)
    return echo
strat0 = lambda score, opponent: 1 - opponent // 10
strat1 = always_roll(3)
s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)

def total(s0, s1):
     print(s0 + s1)
     return echo
def echo(s0, s1):
     print(s0, s1)
     return total
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)




def echo_0(s0, s1):
     print('*', s0)
     return echo_0
def echo_1(s0, s1):
     print('**', s1)
     return echo_1
s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1))



# f0 = announce_highest(1) # Only announce Player 1 score gains
# f1 = f0(12, 0)
# f2 = f1(12, 9)
# f3 = f2(20, 9)
# f4 = f3(20, 30)
# f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
# f6 = f5(21, 47)
# f7 = f6(21, 77)


dice = make_test_dice(4, 2, 5, 1)
averaged_dice = make_averaged(dice, 1000)
averaged_dice()

# dice = make_test_dice(1, 6)
# max_scoring_num_rolls(dice)
# print(max_scoring_num_rolls(dice))
# # problem 10 test
# print(bacon_strategy(0, 9, 8, 5))
# print(bacon_strategy(9, 0, 6, 5))
# print(bacon_strategy(50, 2, 7, 5))
# print(extra_turn(10,19))
# print(free_bacon(19))
# print(bacon_strategy(10, 19, 8, 6))

print(extra_turn_strategy(10, 19, 8, 6))
print(extra_turn_strategy(17, 36, 100, 6))