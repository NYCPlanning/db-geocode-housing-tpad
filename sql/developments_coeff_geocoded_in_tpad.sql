CREATE TABLE developments_coeff_geocoded_in_tpad AS
SELECT *
FROM developments_coeff_geocoded
WHERE geo_message LIKE '%TPAD%'
OR geo_message_2 LIKE '%TPAD%';
