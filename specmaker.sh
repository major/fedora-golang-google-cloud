#!/bin/bash
# Generate spec files for submodules in Google's Cloud Go package.
set -x

for SUBMODULE in $(ls -d */ | sed 's/\/$//'); do 
    GIT_TAG=$(git tag | sort --version-sort -r | grep $SUBMODULE | head -n 1)
    if [ -z $GIT_TAG ]; then
        continue
    fi

    VERSION=$(echo $GIT_TAG | sed 's/[a-z0-9]*\/v//')
    GIT_TAG_SPEC=$(echo $GIT_TAG | sed "s/$VERSION/%{version}/")
    echo -e "$SUBMODULE: \t$GIT_TAG_SPEC ($VERSION)"

    export VERSION SUBMODULE

    mkdir -vp specs
    envsubst < ../template.spec > ../specs/golang-google-cloud-$SUBMODULE.spec
done
