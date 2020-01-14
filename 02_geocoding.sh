DB_CONTAINER_NAME=housing

docker run -it --rm\
            --network=host\
            -v `pwd`:/home/db-geocode-housing-tpad\
            -w /home/db-geocode-housing-tpad\
            --env-file .env\
            sptkl/docker-geosupport:19d bash -c "pip3 install -r python/requirements.txt; python3 python/geocoding.py"

            docker exec $DB_CONTAINER_NAME psql -U postgres -h localhost -f sql/create_housing_geocode_tpad.sql
            docker exec $DB_CONTAINER_NAME psql -U postgres -h localhost -f sql/housing_geocode_tpad_errors.sql
