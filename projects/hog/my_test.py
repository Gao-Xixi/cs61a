from hog import play, always_roll, both, announce_lead_changes, say_scores,announce_highest
from dice import make_test_dice

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

def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

f0 = announce_highest(1) # Only announce Player 1 score gains
f1 = f0(12, 0)
f2 = f1(12, 9)
f3 = f2(20, 9)
f4 = f3(20, 30)
f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
f6 = f5(21, 47)
f7 = f6(21, 77)