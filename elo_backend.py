"elo calculations"
import math

set1_scores, set2_scores, set3_scores = [[0,0],[0,0],[0,0]]
sA = 0

rA = int(input("Player A's rating: \n"))
rB = int(input("Player B's rating: \n"))

sets_played = int(input("How many sets were played? (Enter 1, 2 or 3):\n"))

set1 = input("Enter Set 1 score (in the format a:b eg. 21:19): \n")
set1_scores = set1.split(":")
if int(set1_scores[0]) > int(set1_scores[1]):
    sA += 1

if sets_played >= 2:
    set2 = input("Enter Set 2 score (in the format a:b eg. 21:19): \n")
    set2_scores = set2.split(":")
    if int(set2_scores[0]) > int(set2_scores[1]):
        sA += 1

if sets_played >= 3:
    set3 = input("Enter Set 3 score (in the format a:b eg. 21:19): \n")
    set3_scores = set3.split(":")
    if int(set3_scores[0]) > int(set3_scores[1]):
        sA += 1

playerA_total = int(set1_scores[0]) + int(set2_scores[0]) + int(set3_scores[0])
playerB_total = int(set1_scores[1]) + int(set2_scores[1]) + int(set3_scores[1])

point_diff = playerB_total - playerA_total


c = 0.07 # difference in points are max about 30%
k = 30  #* (1 + c*math.log(1 + abs(point_diff)))

expected_score = 1 / (1 + math.pow(10,((rB - rA)/200)))

if sets_played == 1 and sA == 1:
    sA = 2

if sA == 2 and point_diff > 0: # if player A wins but overall player B gets more points, there shouldn't be any multiplier for dominancy
    k = 30
print("multiplier:",(1 + c*math.log(1 + abs(point_diff))))

def rA_change(sA, expected_score): # the elo change for Player A - can be negative
    if sA == 2:
        performed_score = 1
    else:
        performed_score = 0

    elo_change = round(k * (performed_score - expected_score))

    return elo_change

A_elo_change = rA_change(sA, expected_score)

print("Elo Change:",A_elo_change)

player_A_new_elo = rA + A_elo_change
player_B_new_elo = rB - A_elo_change

print("Player A new elo:",player_A_new_elo,"\nPlayer B new elo:",player_B_new_elo)