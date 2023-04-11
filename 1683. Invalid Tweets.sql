# Write your MySQL query statement below
select tweet_id
FROM Tweets
WHERE CHARACTER_LENGTH(content)>15;
