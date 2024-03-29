import numpy as np
def calculateScore(applicant, team, attrWeights):
    # Finding the highest values for each attribute within the team
    maxAttr = {}
    for member in team:
        for attr, val in member["attributes"].items():
            if attr not in maxAttr or val > maxAttr[attr]:
                maxAttr[attr] = val

    # Calculating Score: (Applicant's Attribute Score / Highest Attribute Score in Team) * Attribute's Weightage
    score = 0
    for attr in applicant["attributes"]:
        if attr in maxAttr and attr in attrWeights:
            score += (applicant["attributes"][attr] / maxAttr[attr]) * attrWeights[attr]

    # Ensuring score is between 0 and 1
    score = max(0, min(score, 1))

    # To round score to 2 decimal places
    return round(score, 2)