import numpy as np
def calculateScore(applicant, team, attrWeights):
    numAttr = len(team[0]["attributes"])

    maxAttr = {}
    for member in team:
        for attr, val in member["attributes"].items():
            if attr not in maxAttr or val > maxAttr[attr]:
                maxAttr[attr] = val

    score = 0
    for attr in applicant["attributes"]:
        if attr in maxAttr and attr in attrWeights:
            score += (applicant["attributes"][attr] / maxAttr[attr]) * attrWeights[attr]

    return round(score, 2)

