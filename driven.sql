select * from driven;
SELECT  "id","place","mag"
FROM driven
ORDER BY 
    "mag" DESC
LIMIT 10;
SELECT 
    "id",
    "place",
    "depth_km"
FROM 
    driven
ORDER BY 
    "depth_km" DESC
LIMIT 10;
SELECT 
    "id",
    "place",
    "mag",
    "depth_km"
FROM 
    driven
WHERE 
    "depth_km" < 50
    AND "mag" > 7.5
ORDER BY 
    "mag" DESC;
SELECT 
    "place",
    AVG("depth_km") AS avg_depth_km
FROM 
    driven
GROUP BY 
    "place"
ORDER BY 
    avg_depth_km DESC;
SELECT 
    "magType",
    AVG("mag") AS avg_magnitude
FROM 
    driven
GROUP BY 
    "magType"
ORDER BY 
    avg_magnitude DESC;
