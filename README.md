# taskSixFunctions

This app receive a REST GET request (/function) with the following structure:
{'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}
where 'data' - a list of numbers (float, int) of undefined length, 'rule' - a list (sequence) of rules to be executed upon the 'data' list.
This service have one end-point '/function'.
