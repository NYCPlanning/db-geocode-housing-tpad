DB_CONTAINER_NAME=housing

docker kill $DB_CONTAINER_NAME
docker container prune -f;
docker volume prune -f
