import json

with open("stats.json", "r") as f:
    data = json.load(f)

raw_all_players_data = []
all_players_data = []

team_id_to_name = {
    "788267008": "49ers",
    "788267009": "Bears",
    "788267010": "Bengals",
    "788267012": "Bills",
    "788267013": "Broncos",
    "788267014": "Browns",
    "788267015": "Buccaneers",
    "788267016": "Cardinals",
    "788267018": "Chargers",
    "788267019": "Chiefs",
    "788267020": "Colts",
    "788267021": "Commanders",
    "788267022": "Cowboys",
    "788267023": "Dolphins",
    "788267024": "Eagles",
    "788267025": "Falcons",
    "788267027": "Giants",
    "788267029": "Jaguars",
    "78826730": "Jets",
    "788267031": "Lions",
    "788267033": "Packers",
    "788267034": "Panthers",
    "788267035": "Patriots",
    "788267036": "Raiders",
    "788267037": "Rams",
    "788267038": "Ravens",
    "788267039": "Saints",
    "788267040": "Seahawks",
    "788267041": "Steelers",
    "788267042": "Texans",
    "788267042": "Titans",
    "788267044": "Vikings"


}

for reg_key, reg_value in data.get("reg", {}).items():
    for team_id, team_stats in reg_value.items():
        for player_id, player_stats in team_stats.get("player-stats", {}).items():
            if any(key in player_stats for key in ["recYds", "rushYds", "passYds"]):
                rec_yds = int(player_stats.get("recYds", "0"))
                rec_tds = int(player_stats.get("recTDs", "0"))
                rec_catches = int(player_stats.get("recCatches", "0"))

                rush_att = int(player_stats.get("rushAtt", "0"))
                rush_yds = int(player_stats.get("rushYds", "0"))
                rush_tds = int(player_stats.get("rushTds", "0"))
                rush_fum = int(player_stats.get("rushFum", "0"))

                pass_yds = int(player_stats.get("passYds", "0"))
                pass_tds = int(player_stats.get("passTDs", "0"))
                pass_ints = int(player_stats.get("passInts", "0"))

                full_name = player_stats.get("fullName", "N/A")
                team_id = str(player_stats.get("teamId", "N/A"))
                
                fantasy_score = (rec_yds * 0.1) + (rec_catches * 1) + (rec_tds * 6) + (pass_yds * 0.04) + (pass_tds * 4)  + (pass_ints * -2)+ (rush_fum * -1) + (rush_yds * 0.1) + (rush_tds * 6)
                rounded_fantasy_score = round(fantasy_score, 2)

                team_name = team_id_to_name.get(team_id, "Unknown Team")
                
                raw_player_data = {
                    "team": team_name,
                    "name": full_name,
                    "rush_att": rush_att,
                    "rush_yards": rush_yds,
                    "rush_TDs": rush_tds,
                    "fumbles": rush_fum,
                    "rec": rec_catches,
                    "rec_yards": rec_yds,
                    "rec_TDs": rec_tds,
                    "passing_yards": pass_yds,
                    "passing_TDs": pass_tds,
                    "INTs": pass_ints,
                    "fantasy_score": rounded_fantasy_score
                }

                player_name_team_score = {
                    "team": team_name,
                    "name": full_name,
                    "fantasy_score": rounded_fantasy_score
                }

                raw_all_players_data.append(raw_player_data)
                all_players_data.append(player_name_team_score)

                print(f"FullName: {full_name}, Fantasy score: {rounded_fantasy_score}, Team Name: {team_name}")
                

raw_all_players_data.sort(key=lambda x: x[team_name])

file_name = "week_8_raw_stats.json"
file_name_2 = "week_8_fantasy.json"

with open(file_name, "w") as json_file:
    json.dump(raw_all_players_data, json_file, indent=4)

print(f"JSON data has been written to {file_name}")

with open(file_name_2, "w") as json_file:
    json.dump(all_players_data, json_file, indent=4)

print(f"JSON data has been written to {file_name_2}")