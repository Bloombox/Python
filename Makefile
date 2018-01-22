
#
## Bloombox: Python API Client
#

ENV_PATH ?= .env
VERBOSE ?= no

ifeq ($(VERBOSE),yes)
CP_FLAGS ?= v
RM_FLAGS ?= v
else
CP_FLAGS ?=
RM_FLAGS ?=
endif

all: env build

env: submodules $(ENV_PATH)

distclean: clean clean-schema
	@echo "Cleaning environment..."
	@rm -fr$(RM_FLAGS) $(ENV_PATH)

clean-schema:
	@echo "Cleaning embedded schema..."
	@rm -fr$(RM_FLAGS) bloombox/schema/*
	@$(MAKE) -C schema clean

clean:
	@echo "Cleaning PYC files..."
	@find . -name '*.py[c,o]' -delete

$(ENV_PATH):
	@echo "Setting up environment..."
	@mkdir -p $(ENV_PATH)
	@virtualenv $(ENV_PATH)
	@$(ENV_PATH)/bin/pip install -r requirements.txt
	@echo "Environment ready."

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

bloombox/schema/__init__.py:
	@echo "Installing Schema..."
	@mkdir -p bloombox/schema bloombox/services
	@cd schema/languages/python && cp -fr$(CP_FLAGS) ./* ../../../bloombox/schema/
	@cd schema/languages/pygrpc && cp -fr$(CP_FLAGS) ./* ../../../bloombox/services/

embedded-schema: schema/languages/python bloombox/schema/__init__.py
	@echo "Embedded schema ready."

build: embedded-schema
	@echo "Build would happen now."

interactive: all
	@$(ENV_PATH)/bin/python

