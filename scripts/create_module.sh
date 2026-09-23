#!/usr/bin/env bash

set -eou pipefail
IFS=$'\n'
set -o allexport

# shellcheck source=/dev/null
[ -f .env ] && source ../.env

set +o allexport

DIRECTORIES="${*:-}"

for DIRECTORY_NAME in "${DIRECTORIES[@]}"; do 
	
	[[ "$DIRECTORY_NAME" == "" ]] && echo "Necessário fornecer uma variável ou um array de variaveis" && exit 1

	DIRECTORY="$MODULE_PATH""$DIRECTORY_NAME"
	mkdir -p "$DIRECTORY" 
	touch "$DIRECTORY"/"$DIRECTORY_NAME"{_controller,_service,_repository}.py
	touch "$DIRECTORY"/__init__.py
done

exit 0

