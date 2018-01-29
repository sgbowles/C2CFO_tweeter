from mlbgame import teams

def get_team_list():

    list = teams()

    size = list.__len__()

    team_name_list = []

    for team in list:
        # curTeam = team.club_full_name
        team_name_list.append(team.club_full_name)

    return team_name_list
