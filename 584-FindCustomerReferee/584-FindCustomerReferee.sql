-- Last updated: 9/11/2025, 12:31:41 PM
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE NOT referee_id =2
OR referee_id is null