import json

with open("stats.json", "r") as f:
    data = json.load(f)

with open("stats.json", "r") as f:
    stats_data = json.load(f)

raw_all_players_data = []
all_players_data = []
week_8_fantasy_scores = []
week_9_fantasy_scores = []
week_10_fantasy_scores = []
desired_weeks = ["8", "9", "10"]


def has_offensive_stats(player_stats):
    offensive_stat_keys = ["recYds", "recCatches", "recTDs", "rushAtt", "rushYds", "rushTDs", "passYds", "passTDs", "passInts", "recDrops"]
    return any(key in player_stats for key in offensive_stat_keys)

team_id_to_name = {
    "788267008": "49ers",
    "788267009": "Bears",
    "788267010": "Bengals",
    "788267011": "Bills",
    "788267012": "Bills",
    "788267013": "Browns",
    "788267014": "Broncos",
    "788267015": "Cardinals",
    "788267016": "Buccaneers",
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
    "788267030": "Jets",
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
    "788267043": "Titans",
    "788267044": "Vikings"


}

for week_key, week_value in data.get("reg", {}).items():
    if week_key not in desired_weeks:
        continue
    week_team_ids = set()

    for team_id, team_stats in week_value.items():
        for player_id, player_stats in team_stats.get("player-stats", {}).items():
            if any(key in player_stats for key in ["recYds", "rushYds", "passYds"]):
                roster_id = int(player_stats.get("rosterId", "0"))

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

                """
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
                    "fantasy_score": rounded_fantasy_score,
                    "teamID": team_id,
                    "week": week_key
                }
                """
                
                player_name_team_score = {
                    "player_id": roster_id,
                    "team_name": team_name,
                    "name": full_name,
                    f"week_{week_key}_fantasy_score": rounded_fantasy_score
                }

                # raw_all_players_data.append(raw_player_data)

                if week_key == "8":
                    week_scores = week_8_fantasy_scores
                elif week_key == "9":
                    week_scores = week_9_fantasy_scores
                elif week_key == "10":
                    week_scores = week_10_fantasy_scores

                if any([rec_yds, rec_catches, rec_tds, rush_att, rush_yds, rush_tds, pass_yds, pass_tds, pass_ints, roster_id]):
                    player_name_team_score[f"week_{week_key}_fantasy_score"] = rounded_fantasy_score
                else:
                    player_name_team_score[f"week_{week_key}_fantasy_score"] = 0.0

                week_scores.append(player_name_team_score)

                """
                for player_data in raw_all_players_data:
                    name = player_data.get("name")
                    for week_key in desired_weeks:
                        week_scores = week_8_fantasy_scores if week_key == "8" else week_9_fantasy_scores
                        if name not in [player_data_week.get("name") for player_data_week in week_scores]:
                            player_data[f"week_{week_key}_fantasy_score"] = "DNP"
                """



# file_name = "week_8_9_raw_stats.json"
file_name_8 = "week_8_fantasy.json"
file_name_9 = "week_9_fantasy.json"
file_name_10 = "week_10_fantasy.json"

"""
with open(file_name, "w") as json_file:
    json.dump(raw_all_players_data, json_file, indent=4)

print(f"JSON data has been written to {file_name}")
"""

with open(file_name_8, "w") as json_file:
    json.dump(week_8_fantasy_scores, json_file, indent=4)

print(f"JSON data has been written to {file_name_8}")


with open(file_name_9, "w") as json_file:
    json.dump(week_9_fantasy_scores, json_file, indent=4)

print(f"JSON data has been written to {file_name_9}")


with open(file_name_10, "w") as json_file:
    json.dump(week_10_fantasy_scores, json_file, indent=4)

print(f"JSON data has been written to {file_name_10}")

files = ['week_8_fantasy.json', 'week_9_fantasy.json', 'week_10_fantasy.json']

def merge_JsonFiles(filenames):
    result = {}
    
    for filename in filenames:
        with open(filename, 'r') as infile:
            data = json.load(infile)
            
            for entry in data:
                name = entry.get("name")
                player_id = entry.get("player_id")  # Use a unique identifier

                # Use a combination of name and player_id as the key
                key = (name, player_id)

                if key not in result:
                    result[key] = entry
                else:
                    result[key].update(entry)

    for key, entry in result.items():
        entry.pop('player_id', None)

    result_list = list(result.values())

    with open('combined_weeks.json', 'w') as output_file:
        json.dump(result_list, output_file, indent=4)

    print(f"JSON data has been written to combined_stats.json")

merge_JsonFiles(files)
