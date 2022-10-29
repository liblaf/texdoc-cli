#!/usr/bin/bash
set -o errexit
set -o nounset
set -o pipefail

function _exec() {
  echo -e -n "\033[1;94m"
  echo -n "${@}"
  echo -e "\033[0m"
  "${@}"
}

REPO_HOME="$(realpath --canonicalize-missing "${0}/../..")"
_exec cd "${REPO_HOME}"
_exec sudo apt install libffi7
_exec poetry run build
mkdir --parents "${HOME}/.local/bin"
_exec cp "${REPO_HOME}/dist/texdoc-cli" "${HOME}/.local/bin"
