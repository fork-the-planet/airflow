# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-standard",
        "name": "Standard",
        "description": "Airflow Standard Provider\n",
        "state": "ready",
        "source-date-epoch": 1734536895,
        "versions": ["0.0.3", "0.0.2", "0.0.1"],
        "integrations": [
            {
                "integration-name": "Standard",
                "external-doc-url": "https://airflow.apache.org/",
                "tags": ["apache"],
                "how-to-guide": [
                    "/docs/apache-airflow-providers-standard/operators/bash.rst",
                    "/docs/apache-airflow-providers-standard/operators/python.rst",
                    "/docs/apache-airflow-providers-standard/operators/datetime.rst",
                ],
            }
        ],
        "operators": [
            {
                "integration-name": "Standard",
                "python-modules": [
                    "airflow.providers.standard.operators.datetime",
                    "airflow.providers.standard.operators.weekday",
                    "airflow.providers.standard.operators.bash",
                    "airflow.providers.standard.operators.python",
                    "airflow.providers.standard.operators.generic_transfer",
                    "airflow.providers.standard.operators.trigger_dagrun",
                    "airflow.providers.standard.operators.latest_only",
                ],
            }
        ],
        "sensors": [
            {
                "integration-name": "Standard",
                "python-modules": [
                    "airflow.providers.standard.sensors.date_time",
                    "airflow.providers.standard.sensors.time_delta",
                    "airflow.providers.standard.sensors.time",
                    "airflow.providers.standard.sensors.weekday",
                    "airflow.providers.standard.sensors.bash",
                    "airflow.providers.standard.sensors.python",
                    "airflow.providers.standard.sensors.filesystem",
                    "airflow.providers.standard.sensors.external_task",
                ],
            }
        ],
        "hooks": [
            {
                "integration-name": "Standard",
                "python-modules": [
                    "airflow.providers.standard.hooks.filesystem",
                    "airflow.providers.standard.hooks.package_index",
                    "airflow.providers.standard.hooks.subprocess",
                ],
            }
        ],
        "triggers": [
            {
                "integration-name": "Standard",
                "python-modules": [
                    "airflow.providers.standard.triggers.external_task",
                    "airflow.providers.standard.triggers.file",
                    "airflow.providers.standard.triggers.temporal",
                ],
            }
        ],
        "config": {
            "standard": {
                "description": "Options for the standard provider operators.",
                "options": {
                    "venv_install_method": {
                        "description": "Which python tooling should be used to install the virtual environment.\n\nThe following options are available:\n- ``auto``: Automatically select, use ``uv`` if available, otherwise use ``pip``.\n- ``pip``: Use pip to install the virtual environment.\n- ``uv``: Use uv to install the virtual environment. Must be available in environment PATH.\n",
                        "version_added": None,
                        "type": "string",
                        "example": "uv",
                        "default": "auto",
                    }
                },
            }
        },
        "dependencies": ["apache-airflow>=2.9.0", "apache-airflow-providers-common-sql>=1.20.0"],
    }