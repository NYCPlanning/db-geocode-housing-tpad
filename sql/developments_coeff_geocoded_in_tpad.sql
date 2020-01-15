CREATE TABLE developments_coeff_geocoded_in_tpad AS
SELECT *
FROM developments_coeff_geocoded
WHERE geo_return_code IN ('22', '23');
