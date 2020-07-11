# python 操作json
# json.dump
# json.load
import json

numbers = [1, 2, 3, 4, 5, 6, 12, 34]
fileName = 'demo.json'
with open(fileName, 'w') as hd:
    json.dump(numbers, hd)

print("操作完成")

# json.load demo
fileName = 'demo.json'
with open(fileName) as djhs:
    nuns = json.load(djhs)
    print(nuns)
