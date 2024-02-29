Datahouse Take Home Project - Compatibility Predictor

An application to determine an applicant's compatibility with the Datahouse team.

For the project, I created a small set of data containing attributes and their weightage - higher weight = more desirable attribute, less weight = less desirable attribute.

Using these attribute weights, I determined an applicant's score by taking the value of each of their attributes divided by the highest value of said attribute found within the team,
and then multiplied this resulting value by the attribute's weight.

Finally, I rounded each applicant's scores to 2 decimal places before outputting the resulting data in JSON.

