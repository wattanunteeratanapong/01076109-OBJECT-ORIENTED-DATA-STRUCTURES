# Chapter : 9 - item : 5 - Premier League Score

# สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด
# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***
# [ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]
# ตัวอย่าง
# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }
# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68

# Test Case 1
# Enter Input : Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
# == results ==
# ['Manchester United', {'points': 95}, {'gd': 68}]
# ['Arsenal', {'points': 80}, {'gd': 69}]
# ['Chelsea', {'points': 74}, {'gd': 69}]

# Test Case 2
# Enter Input : Manchester City,30,8,0,67,20/Liverpool,34,2,2,118,29/Leicester City,22,8,8,98,29
# == results ==
# ['Liverpool', {'points': 104}, {'gd': 89}]
# ['Manchester City', {'points': 90}, {'gd': 47}]
# ['Leicester City', {'points': 74}, {'gd': 69}]

# Test Case 3
# Enter Input : Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,30,0,8,87,39
# == results ==
# ['Arsenal', {'points': 98}, {'gd': 48}]
# ['Manchester City', {'points': 92}, {'gd': 82}]
# ['Liverpool', {'points': 80}, {'gd': 89}]

# Test Case 4
# Enter Input : Manchester United,30,8,0,67,20/New Castle United,34,2,2,118,36/Leicester City,34,2,2,108,21
# == results ==
# ['Leicester City', {'points': 104}, {'gd': 87}]
# ['New Castle United', {'points': 104}, {'gd': 82}]
# ['Manchester United', {'points': 90}, {'gd': 47}]

# Test Case 5
# Enter Input : Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,28,2,8,87,39
# == results ==
# ['Manchester City', {'points': 92}, {'gd': 82}]
# ['Arsenal', {'points': 92}, {'gd': 48}]
# ['Liverpool', {'points': 80}, {'gd': 89}]

# Test Case 6
# Enter Input : Chelsea,35,3,0,102,20/Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,28,2,8,87,39
# == results ==
# ['Chelsea', {'points': 105}, {'gd': 82}]
# ['Manchester City', {'points': 92}, {'gd': 82}]
# ['Arsenal', {'points': 92}, {'gd': 48}]
# ['Liverpool', {'points': 80}, {'gd': 89}]

# Test Case 7
# Enter Input : Wolverhampton,4,2,1,8,8/Liverpool,5,1,1,17,15/Chelsea,3,1,3,16,9/Leicester City,5,2,0,17,9/Arsenal,4,3,0,9,7/Manchester City,3,1,2,9,8/Manchester United,2,3,1,9,13/Souththampton,4,2,1,14,12/Tottenham Hotspur,4,1,2,18,9/Everton,4,2,1,15,11/Aston Villa,4,2,0,15,9
# == results ==
# ['Liverpool', {'points': 16}, {'gd': 2}]
# ['Leicester City', {'points': 15}, {'gd': 8}]
# ['Tottenham Hotspur', {'points': 14}, {'gd': 9}]
# ['Everton', {'points': 13}, {'gd': 4}]
# ['Souththampton', {'points': 13}, {'gd': 2}]
# ['Wolverhampton', {'points': 13}, {'gd': 0}]
# ['Chelsea', {'points': 12}, {'gd': 7}]
# ['Aston Villa', {'points': 12}, {'gd': 6}]
# ['Arsenal', {'points': 12}, {'gd': 2}]
# ['Manchester City', {'points': 11}, {'gd': 1}]
# ['Manchester United', {'points': 7}, {'gd': -4}]

def calculate_points_and_gd(team):
    wins = int(team['wins'])
    draws = int(team['draws'])
    scored = int(team['scored'])
    conceded = int(team['conceded'])
    
    points = wins * 3 + draws * 1 
    gd = scored - conceded  
    
    return points, gd

def sort_teams(teams):
    for i in range(len(teams)):
        for j in range(0, len(teams) - i - 1):
            points_j, gd_j = teams[j]['points'], teams[j]['gd']
            points_j1, gd_j1 = teams[j+1]['points'], teams[j+1]['gd']
            
            if points_j < points_j1 or (points_j == points_j1 and gd_j < gd_j1):
                teams[j], teams[j + 1] = teams[j + 1], teams[j]
    return teams

input_data = input("Enter Input : ")
print("== results ==")

teams_data = input_data.split('/')
teams = []

for team_data in teams_data:
    name, wins, loss, draws, scored, conceded = team_data.split(',')
    team = {
        "name": name,
        "wins": wins,
        "loss": loss,
        "draws": draws,
        "scored": scored,
        "conceded": conceded
    }
    points, gd = calculate_points_and_gd(team)
    team['points'] = points
    team['gd'] = gd
    teams.append(team)

sorted_teams = sort_teams(teams)

for team in sorted_teams:
    print(f"['{team['name']}', {{'points': {team['points']}}}, {{'gd': {team['gd']}}}]")
