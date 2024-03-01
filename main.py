import json
from dataset import *
from functions import *

# Initialize JSON dataset
data = json.loads(sampleData)
weightMultiplier = json.loads(weightMultiplierData)

team = data["team"]
applicants = data["applicants"]

# Determining the weight of each attribute
attrWeights = {}
for attr in team[0]["attributes"]:
    attrWeights[attr] = (1 / len(team[0]["attributes"]))

    if attr in weightMultiplier["attributes"]:
        attrWeights[attr] *= weightMultiplier["attributes"][attr]

# Calculating scores using calculateScore in functions.py
scores = []
for applicant in applicants:
    score = calculateScore(applicant, team, attrWeights)
    scores.append({
        "name" : applicant["name"],
        "score" : score
    })

# Output compatibility scores as JSON
outputData = {"scoredApplicants" : scores}
output = json.dumps(outputData, indent = 4)
print(output)