#!/bin/bash
set -x #debug

usage() {
    cat <<EOF
$(basename $0) [-h] [-d=dir] [ file1 ... file_n ]

Downloads the annotations for the gene names contained in files from RVS.
EOF
}

opts() {
    DIR='.'
    for opt; do
        case "$opt" in
            -h)
                usage
                ;;
            -d=*)
                DIR=${opt##-d=}
                ;;
            *)
                FILES+="$opt"
                ;;
        esac
    done
    [ ${#FILES[@]} -eq 0 ] && FILES+="-"
}

download_gene() {
    local GENE=$1
    curl -LO "https://rvs.u.hpc.mssm.edu/rest/frequency/gene/$GENE"
}

main() {

    opts "$@"

    pushd $DIR
    for f in "${FILES[@]}"; do
        cat "$f" | while read gene; do
                     download_gene $gene
        done
    done
    popd
}

main "$@"
