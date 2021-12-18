#!/bin/bash
set -e

# Set up MongoDB admin user
# MONGO_INITDB_ROOT_USERNAME & MONGO_INITDB_ROOT_PASSWORD is the config for db admin.
# Create an write/read dbUser / dbPwd
# dbUser & dbPwd is the config for db user.

echo "
    > > > Checking admin user exists
    "
if [ -n "${MONGO_INITDB_ROOT_USERNAME:-}" ] && [ -n "${MONGO_INITDB_ROOT_PASSWORD:-}" ]; then
    <<EOF
db.createUser({
        user: "admin",
        pwd: "password",
        roles:[
            {
                role: "readWrite",
                db:   "mydatabase"
            }
        ]
    }
);
EOF
else
    echo "MONGO_INITDB_ROOT_USERNAME or MONGO_INITDB_ROOT_PASSWORD are missing. Failed to create admin user"
    exit 403
fi
echo "
    > > > Trying to create database and users
    "
if [ -n "${dbUser:-}" ] && [ -n "${dbPwd:-}" ]; then
    mongo -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD <<EOF
db=db.getSiblingDB('users');
use users;
db.createUser({
  user:  $dbUser,
  pwd: $dbPwd,
  roles: [{
    role: 'readWrite',
    db: 'users'
  }]
});
EOF
else
    echo "dbUser and dbPwd must be provided. Failed to create User."
    exit 403
fi
