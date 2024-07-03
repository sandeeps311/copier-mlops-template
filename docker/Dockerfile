ARG SOURCE_IMAGE=python
ARG SOURCE_TAG=3.10-slim
FROM "${SOURCE_IMAGE}:${SOURCE_TAG}"

# Labels
ARG BUILD_DATE
ARG GIT_COMMIT
ARG VERSION
ENV BUILD_DATE=${BUILD_DATE}
ENV GIT_COMMIT=${GIT_COMMIT}
ENV VERSION=${VERSION}
LABEL maintainer="PMI"
# hadolint ignore=DL3053
LABEL build-date="${BUILD_DATE}"
# hadolint ignore=DL3055
LABEL git-commit="${GIT_COMMIT}"
# hadolint ignore=DL3056
LABEL version="${VERSION}"
LABEL description="Image for testing CI pipelines"

# Don't use PIP_EXTRA_INDEX_URL because it is found/used by default by pip
ARG PMI_PIP_INDEX_URL

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# install dependencies
ARG DEBIAN_FRONTEND=noninteractive
# hadolint ignore=DL3015,DL3008
RUN apt-get update -yq --fix-missing \
 && apt-get install -yq --no-install-recommends --reinstall \
    curl \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --quiet --no-cache-dir opencensus-ext-azure \
 && python3 -m pip cache purge
#  && python3 -m pip install --quiet --no-cache-dir -r /home/requirements.txt \
#  && python3 -m pip install --quiet --no-cache-dir --no-deps --index-url="${PMI_PIP_INDEX_URL}" \
#     "pmi-dtsc-common-test" \


COPY ./src /src
CMD ["python", "/src/main.py"]
