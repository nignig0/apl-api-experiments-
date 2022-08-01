from datetime import datetime
from pickle import FALSE
import requests
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#app that gets the fixtures for a certain gameweek and sends to your email


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

def main():
    pass

main()


