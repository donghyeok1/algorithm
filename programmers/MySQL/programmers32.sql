SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
FROM REST_INFO A
WHERE A.FAVORITES = (SELECT MAX(B.FAVORITES) FROM REST_INFO B WHERE A.FOOD_TYPE = B.FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC