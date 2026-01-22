import requests
import pandas as pd

# Cấu hình
API_KEY = "RGAPI-YOUR-KEY-HERE" # Thay key của bạn vào đây
SUMMONER_NAME = "YourName"
TAG_LINE = "YourTag" # Ví dụ: VN1
REGION = "asia" # Khu vực cho trận đấu

# 1. Lấy PUUID (ID định danh người chơi)
url_puuid = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{SUMMONER_NAME}/{TAG_LINE}?api_key={API_KEY}"
response = requests.get(url_puuid)
puuid = response.json()['puuid']

# 2. Lấy danh sách ID các trận đấu gần nhất
url_matches = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}"
match_ids = requests.get(url_matches).json()

# 3. Lấy chi tiết từng trận đấu
match_details = []
for m_id in match_ids:
    url_detail = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{m_id}?api_key={API_KEY}"
    detail = requests.get(url_detail).json()
    # Ở đây bạn có thể bóc tách JSON theo nhu cầu
    match_details.append(detail['info'])

# 4. Lưu thành file CSV để Power BI đọc
df = pd.DataFrame(match_details)
df.to_csv('lol_matches.csv', index=False)
