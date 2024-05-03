HOST = root@new.prfx.xyz

all: sync-all build run

client: sync-client build run-client

server: sync-server build run-server

build:
	ssh $(HOST) "cd /root/bunker/; docker compose build"

run-client:
	ssh $(HOST) "cd /root/bunker/; docker compose down front; docker compose up -d front"

run-server:
	ssh $(HOST) "cd /root/bunker/; docker compose down api; docker compose up -d api"

run-all:
	ssh $(HOST) "cd /root/bunker/; docker compose down; docker compose up -d"

sync-client:
	rsync -tvr --exclude 'venv' --exclude '**/node_modules' --delete ./client/ $(HOST):/root/bunker/client/

sync-server:
	rsync -tvr --exclude 'venv' --exclude '**/node_modules' --delete ./server/ $(HOST):/root/bunker/server/

sync-all:
	rsync -tvr --exclude 'venv' --exclude '**/node_modules' --delete ./ $(HOST):/root/bunker/