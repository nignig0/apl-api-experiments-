from datetime import datetime
from pickle import FALSE
import requests
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#app that gets the fixtures for a certain gameweek and creates events for them on google calendar

api_key='key'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

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
        "summary": f"Match between {home} and {away}",
        
        "description": "This a description",
        "start": {
            "dateTime": res['kickoff_time'],
        },
        "end": {
            "dateTime": res['kickoff_time'],
        },
        })
    return fixtures

fix = getFixtures(1)

def main():
    flow = InstalledAppFlow.from_client_secrets_file("creds.json", SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials = creds)
    try:
        for fixture in fix:
            response = service.events().insert(calendarId="primary", body = fixture).execute()
    except Exception as e:
        return e.message

main()


