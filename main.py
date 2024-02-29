import json
from dataset import *
from functions import *

data = json.loads(sampleData)
weightMultiplier = json.loads(weightMultiplierData)

team = data["team"]
applicants = data["applicants"]

# Determining the weight of each attribute
attrWeights = {}
for attr in team[0]["attributes"]:
    # For simplicity's sake, I took the weight of each attribute to be 1 over the total number of attributes
    attrWeights[attr] = (1 / len(team[0]["attributes"]))

    if attr in weightMultiplier["attributes"]:
        attrWeights[attr] *= weightMultiplier["attributes"][attr]

# Calculating scores
scores = []
for applicant in applicants:
    score = calculateScore(applicant, team, attrWeights)
    scores.append({
        "name" : applicant["name"],
        "score" : score
    })

outputData = {"scoredApplicants" : scores}
output = json.dumps(outputData, indent = 4)
print(output)