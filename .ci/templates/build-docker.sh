#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o nounset
set -o pipefail

BUILD_DATE=$(date +'%Y%m%d')

# check if local packages present
echo "BUILD_CONTEXT: ${BUILD_CONTEXT}"
# DEBUG: check to make sure we're building from proper path
printf "ls BUILD_CONTEXT: [\\n%s\\n]\\n" "$(ls "$BUILD_CONTEXT")"

# echo build command & run
# assumes dockerfile is in /repo/Dockerfile
(
set -x;
# export DOCKER_BUILDKIT=1
docker buildx create --use --name builder;
docker buildx build \
  --progress=plain \
  --platform="${PLATFORM}" \
  --file="${DOCKERFILE_PATH}" \
  --cache-from="${SOURCE_IMAGE}" \
  --build-arg SOURCE_IMAGE="${SOURCE_IMAGE}" \
  --build-arg SOURCE_TAG="${SOURCE_TAG}" \
  --build-arg BUILD_DATE="${BUILD_DATE}" \
  --build-arg GIT_COMMIT="${COMMIT_HASH}" \
  --build-arg PMI_PIP_INDEX_URL="${PMI_PIP_INDEX_URL}" \
  --tag "${REGISTRY}/${IMAGE_NAME}:${COMMIT_TAG}" \
  --tag "${REGISTRY}/${IMAGE_NAME}:${VERSION_TAG}" \
  --tag "${REGISTRY}/${IMAGE_NAME}:latest" \
  --push \
  "${BUILD_CONTEXT}"
)

### image caching is not enabled (yet?)
# --cache-to=type=registry,ref="${REGISTRY}/${IMAGE_NAME}",mode=max \
