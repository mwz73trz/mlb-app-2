from django.http import response
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'home.html')

def search_player(request):
    if request.method == "GET":
        query = request.GET.get("q")
        r = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{query}%25'")
        response = r.json()['search_player_all']['queryResults']['row']
        print(response)
        player_list = []
        for player in response:
            result = {'name': player['name_display_first_last'], 'team': player['team_full'], 'id': player['player_id']}
            player_list.append(result)
    return render(request, 'search_player.html', {'players': player_list})

def player_detail(request, player_id):
    id = int(player_id['player_id'])
    player_detail = f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id={id}"
    r = requests.get(player_detail)
    response = r.json()
    content = {
        'name': response['search_player_all']['queryResults']['row']['name_display_first_last_html'],
        'number': response['search_player_all']['queryResults']['row']['jersey_number'],
        'team_full': response['search_player_all']['queryResults']['row']['team_full'],
        'position': response['search_player_all']['queryResults']['row']['position'],
        'bats': response['search_player_all']['queryResults']['row']['bats'],
        'throws': response['search_player_all']['queryResults']['row']['throws'],
        'birth_country': response['search_player_all']['queryResults']['row']['birth_country'],
        'birth_date': response['search_player_all']['queryResults']['row']['birth_date'],
        'height_feet': response['search_player_all']['queryResults']['row']['height_feet'],
        'height_inches': response['search_player_all']['queryResults']['row']['height_inches'],
        'age': response['search_player_all']['queryResults']['row']['age']
    }
    return render(request, 'player_detail.html', content)





