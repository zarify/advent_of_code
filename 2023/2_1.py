import re
cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('2_1.txt') as f:
    games = f.read().strip().split('\n')
    total = 0
    for game in games:
        game_id, game_data = game.split(':')
        game_id = int(game_id.split()[1])
        game_data = game_data.strip().split(';')
        invalid = False
        for gd in game_data:
            reds = re.search(r'(\d+) red', gd)
            greens = re.search(r'(\d+) green', gd)
            blues = re.search(r'(\d+) blue', gd)
            reds = int(reds.group(1)) if reds else 0
            greens = int(greens.group(1)) if greens else 0
            blues = int(blues.group(1)) if blues else 0
            if reds > cubes['red'] or greens > cubes['green'] or blues > cubes['blue']:
                invalid = True
                break
        if not invalid:
            total += game_id
    print(total)