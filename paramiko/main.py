import json
friends = {
    'Dan': (20, 'London', 32324342), 'Maria': (20, 'Madrid', 43525222)
}

with open('friends.json', 'w') as f:
    json.dump(friends, f)

json_string = json.dumps(friends)
print(json_string)