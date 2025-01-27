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
        "package-name": "apache-airflow-providers-mysql",
        "name": "MySQL",
        "description": "`MySQL <https://www.mysql.com/>`__\n",
        "state": "ready",
        "source-date-epoch": 1734535570,
        "versions": [
            "6.0.0",
            "5.7.4",
            "5.7.3",
            "5.7.2",
            "5.7.1",
            "5.7.0",
            "5.6.3",
            "5.6.2",
            "5.6.1",
            "5.6.0",
            "5.5.4",
            "5.5.3",
            "5.5.2",
            "5.5.1",
            "5.5.0",
            "5.4.0",
            "5.3.1",
            "5.3.0",
            "5.2.1",
            "5.2.0",
            "5.1.1",
            "5.1.0",
            "5.0.0",
            "4.0.2",
            "4.0.1",
            "4.0.0",
            "3.4.0",
            "3.3.0",
            "3.2.1",
            "3.2.0",
            "3.1.0",
            "3.0.0",
            "2.2.3",
            "2.2.2",
            "2.2.1",
            "2.2.0",
            "2.1.1",
            "2.1.0",
            "2.0.0",
            "1.1.0",
            "1.0.2",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "MySQL",
                "external-doc-url": "https://www.mysql.com/",
                "how-to-guide": ["/docs/apache-airflow-providers-mysql/operators.rst"],
                "logo": "/docs/integration-logos/MySQL.png",
                "tags": ["software"],
            }
        ],
        "hooks": [{"integration-name": "MySQL", "python-modules": ["airflow.providers.mysql.hooks.mysql"]}],
        "transfers": [
            {
                "source-integration-name": "Vertica",
                "target-integration-name": "MySQL",
                "python-module": "airflow.providers.mysql.transfers.vertica_to_mysql",
            },
            {
                "source-integration-name": "Amazon Simple Storage Service (S3)",
                "target-integration-name": "MySQL",
                "python-module": "airflow.providers.mysql.transfers.s3_to_mysql",
            },
            {
                "source-integration-name": "Presto",
                "target-integration-name": "MySQL",
                "python-module": "airflow.providers.mysql.transfers.presto_to_mysql",
            },
            {
                "source-integration-name": "Trino",
                "target-integration-name": "MySQL",
                "python-module": "airflow.providers.mysql.transfers.trino_to_mysql",
            },
        ],
        "connection-types": [
            {"hook-class-name": "airflow.providers.mysql.hooks.mysql.MySqlHook", "connection-type": "mysql"}
        ],
        "asset-uris": [
            {"schemes": ["mysql", "mariadb"], "handler": "airflow.providers.mysql.assets.mysql.sanitize_uri"}
        ],
        "dataset-uris": [
            {"schemes": ["mysql", "mariadb"], "handler": "airflow.providers.mysql.assets.mysql.sanitize_uri"}
        ],
        "dependencies": [
            "apache-airflow>=2.9.0",
            "apache-airflow-providers-common-sql>=1.20.0",
            "mysqlclient>=1.4.0; sys_platform != 'darwin'",
            "mysql-connector-python>=8.0.29",
            "aiomysql>=0.2.0",
        ],
        "optional-dependencies": {
            "mysql-connector-python": [],
            "amazon": ["apache-airflow-providers-amazon"],
            "openlineage": ["apache-airflow-providers-openlineage"],
            "presto": ["apache-airflow-providers-presto"],
            "trino": ["apache-airflow-providers-trino"],
            "vertica": ["apache-airflow-providers-vertica"],
        },
    }