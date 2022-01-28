# 3 4 atletika 4x100m_valtofutas

# − Az elért helyezés „3”
# − A helyezést elérő sportoló vagy csapat esetén sportolók száma „4”
# − A sportág neve „atletika”
# − A versenyszám neve „4x100m_valtofutas”

class Statistic:
    def __init__(self: any, placement: int, members: int, sport_name: str, sport_category: str):
        self.placement = int(placement)
        self.members = int(members)
        self.sport_name = sport_name
        self.sport_category = sport_category

with open('helsinki.txt') as f:
    data = [i.strip().split() for i in f.readlines()]

data = list(map(lambda x: Statistic(x[0], x[1], x[2], x[3]), data))

print(f"3. feladat:\nPontszerző helyezések száma: {len(data)}")

score = {1: 0, 2: 0, 3: 0}
sports = {}
total_score = 0
points = {
    1: 7,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
}
most_members = 0
most_sport = any

for i in data:
    if i.placement in points:
        total_score += points[i.placement]
        if i.members > most_members:
            most_members = i.members
            most_sport = i
        if i.placement in score:
            score[i.placement] += 1
            if i.sport_name in sports:
                sports[i.sport_name] += 1
            else: sports[i.sport_name] = 0

print(f"4. feladat:\nArany: {score[1]}\nEzüst: {score[2]}\nBronz: {score[3]}")
print(f"5. feladat:\nOlimpiai pontok száma: {total_score}")

biggest = 0
biggest_name = None

for i, e in sports.items():
    if e > biggest:
        biggest = e
        biggest_name = i

print(f"6. feladat:\n{biggest_name.capitalize()} sportágban szereztek több érmet")

with open("helsinki2.txt", "w") as f:
    for i in data:
        _sport = "kajak-kenu" if i.sport_name == "kajakkenu" else i.sport_name
        f.write(f"{i.placement} {i.members} {points[i.placement]} {_sport} {i.sport_category}\n")

i = most_sport

print(f"8. feladat:\nHelyezés: {i.placement}\nSportág: {i.sport_name}\nVersenyszám: {i.sport_category}\nSportolók száma: {i.members}")