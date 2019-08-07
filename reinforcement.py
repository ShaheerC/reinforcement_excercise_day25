ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

tiers = {'gold': 3, 'silver': 2, 'bronze': 1}

def total_ballots(ballots):
    total_points = {}
    for x in ballots:
        for medal, player in x.items():
            if player not in total_points:
                total_points[player] = tiers[medal]
            else:
                total_points[player] += tiers[medal]
    return total_points

def winner(total_points):
    top_player = ''
    top_points = 0
    for player, points in total_points.items():
        if points > top_points:
            top_points = points
            top_player = player
    return(f'{top_player} has won with a total of {top_points} points.')

total_points = total_ballots(ballots)
print(total_points)
print(winner(total_points))