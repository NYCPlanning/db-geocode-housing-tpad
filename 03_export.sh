DB_CONTAINER_NAME=housing

docker exec $DB_CONTAINER_NAME psql -h localhost -U postgres -c "\copy (SELECT * FROM housing_geocode_tpad)
                                TO '/home/db-geocode-housing-tpad/output/housing_geocode_tpad.csv'
                                DELIMITER ',' CSV HEADER;"

docker exec $DB_CONTAINER_NAME psql -h localhost -U postgres -c "\copy (SELECT * FROM housing_geocode_tpad_errors)
                                TO '/home/db-geocode-housing-tpad/output/housing_geocode_tpad_errors.csv'
                                DELIMITER ',' CSV HEADER;"
