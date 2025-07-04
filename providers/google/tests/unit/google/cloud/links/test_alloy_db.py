#
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
from __future__ import annotations

from airflow.providers.google.cloud.links.alloy_db import (
    AlloyDBBackupsLink,
    AlloyDBClusterLink,
    AlloyDBUsersLink,
)

TEST_LOCATION = "test-location"
TEST_CLUSTER_ID = "test-cluster-id"
TEST_PROJECT_ID = "test-project-id"
EXPECTED_ALLOY_DB_CLUSTER_LINK_NAME = "AlloyDB Cluster"
EXPECTED_ALLOY_DB_CLUSTER_LINK_KEY = "alloy_db_cluster"
EXPECTED_ALLOY_DB_CLUSTER_LINK_FORMAT_STR = (
    "/alloydb/locations/{location_id}/clusters/{cluster_id}?project={project_id}"
)
EXPECTED_ALLOY_DB_USERS_LINK_NAME = "AlloyDB Users"
EXPECTED_ALLOY_DB_USERS_LINK_KEY = "alloy_db_users"
EXPECTED_ALLOY_DB_USERS_LINK_FORMAT_STR = (
    "/alloydb/locations/{location_id}/clusters/{cluster_id}/users?project={project_id}"
)
EXPECTED_ALLOY_DB_BACKUP_LINK_NAME = "AlloyDB Backups"
EXPECTED_ALLOY_DB_BACKUP_LINK_KEY = "alloy_db_backups"
EXPECTED_ALLOY_DB_BACKUP_LINK_FORMAT_STR = "/alloydb/backups?project={project_id}"


class TestAlloyDBClusterLink:
    def test_class_attributes(self):
        assert AlloyDBClusterLink.key == EXPECTED_ALLOY_DB_CLUSTER_LINK_KEY
        assert AlloyDBClusterLink.name == EXPECTED_ALLOY_DB_CLUSTER_LINK_NAME
        assert AlloyDBClusterLink.format_str == EXPECTED_ALLOY_DB_CLUSTER_LINK_FORMAT_STR


class TestAlloyDBUsersLink:
    def test_class_attributes(self):
        assert AlloyDBUsersLink.key == EXPECTED_ALLOY_DB_USERS_LINK_KEY
        assert AlloyDBUsersLink.name == EXPECTED_ALLOY_DB_USERS_LINK_NAME
        assert AlloyDBUsersLink.format_str == EXPECTED_ALLOY_DB_USERS_LINK_FORMAT_STR


class TestAlloyDBBackupsLink:
    def test_class_attributes(self):
        assert AlloyDBBackupsLink.key == EXPECTED_ALLOY_DB_BACKUP_LINK_KEY
        assert AlloyDBBackupsLink.name == EXPECTED_ALLOY_DB_BACKUP_LINK_NAME
        assert AlloyDBBackupsLink.format_str == EXPECTED_ALLOY_DB_BACKUP_LINK_FORMAT_STR
