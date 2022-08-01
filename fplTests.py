import requests


#app that gets the fixtures for a certain gameweek 


def getTeamById(id):
    targetTeam = None
    teams = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()["teams"]
    for team in teams:
        if(team['id'] == id):
            targetTeam = team
            break
    return targetTeam['name']

def getFixtures(GW):
    fixtures = []
    params = {'event': f'{GW}'}
    response = requests.get('https://fantasy.premierleague.com/api/fixtures/', params=params).json()
    for res in response:
        home = getTeamById(res['team_h'])
        away = getTeamById(res['team_a'])  
        fixtures.append({
        "summary": f"Match between {home} and {away} starting at {res['kickoff_time']} "
        
        })
    return fixtures

fix = getFixtures(1)

print(fix)



