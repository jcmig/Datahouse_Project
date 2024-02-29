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

    return round(score, 2)

'''
def normalizeScores(scores):
    minScore = min(applicant["score"] for applicant in scores)
    maxScore = max(applicant["score"] for applicant in scores)

    normalizedScores = []
    for applicant in scores:
        normalizedScore = (applicant["score"] - minScore) / (maxScore - minScore)
        normalizedScores.append({"name" : applicant["name"], "score" : normalizedScore})

    return normalizedScores
'''