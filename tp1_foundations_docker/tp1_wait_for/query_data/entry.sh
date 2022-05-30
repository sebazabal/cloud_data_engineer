#!/bin/sh

echo "wait"
sleep 10

exec "$@"

echo "execute reporting script"