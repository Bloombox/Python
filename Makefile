
#
## Bloombox: Python API Client
#

ENV_PATH ?= .env
VERBOSE ?= no
VERSION ?= 0.0.1
SERVICES ?= checkin:v1beta1 devices:v1beta1 menu:v1beta1 shop:v1 telemetry:v1beta3
SERVICE_NAMES ?= $(foreach svc,$(SERVICES),$(firstword $(subst :, ,$(svc))))

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
	@rm -fr$(RM_FLAGS) bloombox/services/descriptor.py

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

bloombox/services/descriptor.py:
	@echo "Installing services..."
	@for service in $(SERVICE_NAMES); do \
		echo "- Installing '$$service'..."; \
		mkdir -p bloombox/services/$$service; \
		cp -fr$(CP_FLAGS) schema/languages/pygrpc/$$services/* bloombox/services/$$service; done
	@echo "# -*- coding: utf-8 -*-" > bloombox/services/descriptor.py
	@echo "" >> bloombox/services/descriptor.py
	@echo "all_services = \"$(SERVICES)\"" >> bloombox/services/descriptor.py
	@echo "" >> bloombox/services/descriptor.py

embedded-schema: schema/languages/python bloombox/schema/__init__.py bloombox/services/descriptor.py
	@echo "Embedded schema ready."

build: embedded-schema
	@echo "Build would happen now."

interactive: all
	@$(ENV_PATH)/bin/python

