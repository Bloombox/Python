
#
## Bloombox: Python API Client
#

VERBOSE ?= no
TESTS ?= yes
COVERAGE ?= yes
VERSION ?= 0.0.1
SERVICES ?= checkin:v1beta1 devices:v1beta1 menu:v1beta1 shop:v1 telemetry:v1beta3

ENV_PATH ?= .env
BUILDBOT ?= no

SERVICE_NAMES ?= $(foreach svc,$(SERVICES),$(firstword $(subst :, ,$(svc))))

BASE_TEST_FLAGS = --no-byte-compile \
		--traverse-namespace \
		--with-xunit --xunit-file=build/tests.xml --xunit-testsuite-name=bloombox

COVERAGE_FLAGS = --with-coverage \
                --cover-package=bloombox \
                --cover-branches \
                --cover-html --cover-html-dir=build/coverage-html \
                --cover-xml --cover-xml-file=build/coverage.xml

TEST_FLAGS ?=

ifeq ($(BUILDBOT),yes)
PIP ?= pip
PYTHON ?= python
ENVPYTHON ?= python
NOSE ?= nosetests
else
PIP ?= $(ENV_PATH)/bin/pip
PYTHON ?= $(shell which python2.7)
ENVPYTHON ?= $(ENV_PATH)/bin/python
NOSE ?= $(ENV_PATH)/bin/nosetests
endif

ifeq ($(COVERAGE),yes)
TEST_FLAGS += $(COVERAGE_FLAGS)
endif

ifeq ($(VERBOSE),yes)
CP_FLAGS ?= v
RM_FLAGS ?= v
TEST_FLAGS += -v
else
CP_FLAGS ?=
RM_FLAGS ?=
endif

_TEST_FLAGS = $(BASE_TEST_FLAGS) $(TEST_FLAGS)

PYTHON_BUILD_TARGETS ?= build build_py
PYTHON_DIST_TARGETS ?= sdist bdist bdist_dumb bdist_egg bdist_wheel
PYTHON_TARGETS ?= $(PYTHON_BUILD_TARGETS) $(PYTHON_DIST_TARGETS)
SCHEMA_PATH ?= src/bloombox/schema

all: env build test
	@echo "Done."

install: install-egg-info install-lib
	@echo "Installation done."

env: $(ENV_PATH)

clean-schema:
	@echo "Cleaning embedded schema..."
	@rm -fr$(RM_FLAGS) $(SCHEMA_PATH)/*
	@$(MAKE) -C schema clean

clean:
	@echo "Cleaning PYC files..."
	@find . -name '*.py[c,o]' -delete
	@echo "Cleaning build..."
	@rm -fr$(RM_FLAGS) build dist

distclean: clean
	@echo "Cleaning environment..."
	@rm -fr$(RM_FLAGS) $(ENV_PATH)

ifneq ($(BUILDBOT),yes)
$(ENV_PATH):
	@echo "Setting up environment..."
	@mkdir -p $(ENV_PATH)
	@virtualenv $(ENV_PATH) -p $(PYTHON)
	@$(PIP) install -r requirements.txt
	@echo "Environment ready."
else
$(ENV_PATH):
	@echo "Setting up environment for CI..."
	@mkdir -p $(ENV_PATH)
	@$(PIP) install -r requirements.txt
	@echo "Environment ready."
endif

submodules:
	@echo "Fetching submodules..."
	@git submodule update --init --recursive

update-schema: submodules
	@echo "Updating schema..."
	@git submodule update --init --remote

sync-schema: update-schema clean-schema embedded-schema
	@echo "Sync done."

schema/languages/python:
	@echo "Building schema..."
	@$(MAKE) -C schema LANGUAGES="python pygrpc"

$(SCHEMA_PATH)/__init__.py:
	@echo "Installing Schema..."
	@mkdir -p $(SCHEMA_PATH) $(SCHEMA_PATH)/services
	@cd schema/languages/python && cp -fr$(CP_FLAGS) ./* ../../../$(SCHEMA_PATH)/

$(SCHEMA_PATH)/services/descriptor.py:
	@echo "Installing services..."
	@for service in $(SERVICE_NAMES); do \
		echo "- Installing '$$service'..."; \
		mkdir -p $(SCHEMA_PATH)/services/$$service; \
		cp -fr$(CP_FLAGS) schema/languages/pygrpc/$$service/* $(SCHEMA_PATH)/services/$$service; done

embedded-schema: schema/languages/python $(SCHEMA_PATH)/__init__.py $(SCHEMA_PATH)/services/descriptor.py
	@echo "Fixing up modules..."
	@cd $(SCHEMA_PATH)/services && for directory in `find -s -x . -type d | xargs`; do touch $$directory/__init__.py; done
	@echo "Embedded schema ready."

build:
	@$(ENVPYTHON) setup.py $(PYTHON_TARGETS)

ifeq ($(TESTS),yes)
test: build
	@echo "Running testsuite..."
	@$(NOSE) $(_TEST_FLAGS) bloombox_tests
else
test:
	@echo "Skipping testsuite."
endif

install-egg-info:
	@echo "Installing egg info..."
	@$(ENVPYTHON) setup.py install_egg_info

install-lib:
	@echo "Installing library..."
	@$(ENVPYTHON) setup.py install_lib

interactive: all
	@PYTHONPATH=src $(ENVPYTHON) -B

