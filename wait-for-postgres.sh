#!/bin/sh
# wait-for-postgres.sh


echo "#######################"
echo "Waiting for postgres"
echo "#######################"

set -e

host="$1"
shift
cmd="$@"

echo "Waiting for postgres"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

# echo "End Waiting for postgres"