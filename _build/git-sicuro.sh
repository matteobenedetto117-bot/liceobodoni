#!/bin/bash
# Esegue un comando git e poi sposta in .git/_to_delete/ i file .lock rimasti
# (nella cartella collegata la cancellazione non è permessa).
# Uso: bash _build/git-sicuro.sh <argomenti di git>
cd "$(dirname "$0")/.."
sposta() { mkdir -p .git/_to_delete; find .git -name '*.lock' -not -path '.git/_to_delete/*' 2>/dev/null | while read f; do mv "$f" ".git/_to_delete/$(echo "$f" | tr / _).$(date +%s%N)"; done; }
sposta
GIT_OPTIONAL_LOCKS=0 git "$@" 2> >(grep -v 'unable to unlink' >&2)
r=$?
sposta
exit $r
