#!/bin/bash
echo "########### Setting up Postgres DB ###########"

pg_restore --no-privileges --no-owner -U postgres -d postgres --clean /tmp/dump/db_dump.sql