#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: Please provide a destination as a command line parameter."
    exit 1
fi

docker build -t gpw-reports . &&
docker save gpw-reports | bzip2 | pv | ssh $1 '
    docker load
    docker service rm gpw-reports
    docker service create \
        --name gpw-reports \
        --secret gpw-reports-smtp-config \
        -e GPW_REPORTS_SMTP_CONFIG_FILE=/run/secrets/gpw-reports-smtp-config \
        -e GPW_REPORTS_MAILING_LIST_FILE=/app/mailing-list/mailing-list.json \
        --mount type=volume,src=gpw-reports-data,dst=/app/data \
        --mount type=volume,src=gpw-reports-mailing-list,dst=/app/mailing-list \
        --read-only \
        gpw-reports \
'
