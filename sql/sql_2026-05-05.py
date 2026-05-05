# Combine Two Tables
# Difficulty: Medium
# Topic: SQL
# Time: O(n) | Space: O(n)
#
# Approach:
# Use a SQL JOIN to combine the records from both tables based on the specified conditions. Utilize LEFT JOIN to ensure that all entries from the first table are included, even if there is no match in the second table.
#
# Solution:

SELECT A.Id, A.Name, B.Score
FROM TableA A
LEFT JOIN TableB B ON A.Id = B.Id;
