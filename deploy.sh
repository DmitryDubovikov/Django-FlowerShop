#!/bin/bash

set -e

directory_path="/opt/Django-FlowerShop"
cd "$directory_path"

echo "Updating git-repo..."
git pull origin main

docker compose up -d --build

commit_hash=$(git rev-parse --short HEAD)
echo "Deploy up to $commit_hash completed!"  