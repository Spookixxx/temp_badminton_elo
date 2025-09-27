import math

def calc_expected_score(rA, rB):
    expected_score = 1 / (1 + math.pow(10,((rB - rA)/300)))
    return expected_score

def calc_sets_won_by_A(sets_played, set1, set2, set3):
    sA = 0
    error = 0
    set1_scores, set2_scores, set3_scores = [[0,0],[0,0],[0,0]]
    set1_scores = set1.split(":")
    print(set1.split(":"))
    if int(set1_scores[0]) > int(set1_scores[1]):
        sA += 1

    if sets_played >= 2:
        set2_scores = set2.split(":")
        if int(set2_scores[0]) > int(set2_scores[1]):
            sA += 1

    if sets_played >= 3:
        set3_scores = set3.split(":")
        if int(set3_scores[0]) > int(set3_scores[1]):
            sA += 1

    if sets_played == 1 and sA == 1:
        sA = 2

    if sA == 3:
        error = 1
    
    return sA, set1_scores, set2_scores, set3_scores, error

def calculate_point_diff(set1_scores, set2_scores, set3_scores):
    playerA_total = int(set1_scores[0]) + int(set2_scores[0]) + int(set3_scores[0])
    playerB_total = int(set1_scores[1]) + int(set2_scores[1]) + int(set3_scores[1])
    point_diff = playerB_total - playerA_total
    return point_diff

def calculate_k(sA, point_diff):
    if sA == 2 and point_diff > 0: # if player A wins but overall player B gets more points, there shouldn't be any multiplier for dominancy
        k = 30
    else:
        c = 0.05 # difference in points are max about 30%
        k = 30  * (1 + c*math.log(1 + abs(point_diff)))

    return k

def rA_change(sA, expected_score, k): # the elo change for Player A - can be negative
    if sA == 2:
        performed_score = 1
    else:
        performed_score = 0
    
    elo_change = k * (performed_score - expected_score)

    if elo_change > 0:
        elo_change = math.floor(elo_change)
    else:
        elo_change = math.ceil(elo_change)

    return elo_change

def update_player_elo(a_ELO, b_ELO, no_of_sets_played, set1, set2, set3):
    expected_score = calc_expected_score(a_ELO, b_ELO)
    sA, set1_scores, set2_scores, set3_scores, error = calc_sets_won_by_A(no_of_sets_played, set1, set2, set3)
    point_difference = calculate_point_diff(set1_scores, set2_scores, set3_scores)
    k = calculate_k(sA, point_difference)
    change_in_elo = rA_change(sA, expected_score, k)
    player_A_new_elo = a_ELO + change_in_elo
    player_B_new_elo = b_ELO - change_in_elo
    return player_A_new_elo, player_B_new_elo, change_in_elo, error
