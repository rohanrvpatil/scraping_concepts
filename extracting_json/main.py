from src import generate_json, export_json
import json


results=[]

#storing all products in results
#5000 is used since there are 4870 search results for the term 'dog'
# 100 can be tested with different values
for offset in range(0,5000,40):
    for product in generate_json(offset):
        results.append(product)
        
# generating json file        
with open("./files/response_data.json", "w") as f:
    json.dump(results, f)

#converting json to xlsx
export_json()

