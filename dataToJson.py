from openpyxl import load_workbook
import json
wb2 = load_workbook('Votes2.xlsx')

ws = wb2.active

data = []

for i in range(5,56):
    state = dict()
    state['name'] = str(ws["A" + str(i)])
    state['population'] = str(ws["B" + str(i)])
    state['seats'] = str(ws["C" + str(i)])
    state['TCJ'] = str(ws["E" + str(i)])
    state['TBJ'] = str(ws["F" + str(i)])
    state['CTJ'] = str(ws["G" + str(i)])
    state['CJT'] = str(ws["H" + str(i)])
    state['JTC'] = str(ws["I" + str(i)])
    state['JCT'] = str(ws["J" + str(i)])
    data.append(state)

with open('votes.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


