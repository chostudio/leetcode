-- Last updated: 9/11/2025, 12:31:14 PM
# Write your MySQL query statement below
SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC