DB_CONTAINER_NAME=housing

docker exec $DB_CONTAINER_NAME psql -h localhost -U postgres -c "\copy (SELECT * FROM developments_coeff_geocoded)
                                TO '/home/db-geocode-housing-tpad/output/developments_coeff_geocoded.csv'
                                DELIMITER ',' CSV HEADER;"

docker exec $DB_CONTAINER_NAME psql -h localhost -U postgres -c "\copy (SELECT * FROM developments_coeff_geocoded_in_tpad)
                                TO '/home/db-geocode-housing-tpad/output/developments_coeff_geocoded_in_tpad.csv'
                                DELIMITER ',' CSV HEADER;"
