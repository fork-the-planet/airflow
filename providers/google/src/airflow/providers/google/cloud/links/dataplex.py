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
"""This module contains Google Dataplex links."""

from __future__ import annotations

from airflow.providers.google.cloud.links.base import BaseGoogleLink

DATAPLEX_BASE_LINK = "/dataplex/process/tasks"
DATAPLEX_TASK_LINK = DATAPLEX_BASE_LINK + "/{lake_id}.{task_id};location={region}/jobs?project={project_id}"
DATAPLEX_TASKS_LINK = DATAPLEX_BASE_LINK + "?project={project_id}&qLake={lake_id}.{region}"

DATAPLEX_LAKE_LINK = "/dataplex/lakes/{lake_id};location={region}?project={project_id}"
DATAPLEX_CATALOG_ENTRY_GROUPS_LINK = "/dataplex/catalog/entry-groups?project={project_id}"
DATAPLEX_CATALOG_ENTRY_GROUP_LINK = (
    "/dataplex/projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}?project={project_id}"
)
DATAPLEX_CATALOG_ENTRY_TYPE_LINK = (
    "/dataplex/projects/{project_id}/locations/{location}/entryTypes/{entry_type_id}?project={project_id}"
)
DATAPLEX_CATALOG_ENTRY_TYPES_LINK = "/dataplex/catalog/entry-types?project={project_id}"
DATAPLEX_CATALOG_ASPECT_TYPE_LINK = (
    "/dataplex/projects/{project_id}/locations/{location}/aspectTypes/{aspect_type_id}?project={project_id}"
)
DATAPLEX_CATALOG_ASPECT_TYPES_LINK = "/dataplex/catalog/aspect-types?project={project_id}"
DATAPLEX_CATALOG_ENTRY_LINK = "/dataplex/dp-entries/projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}?project={project_id}"


class DataplexTaskLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Task link."""

    name = "Dataplex Task"
    key = "task_conf"
    format_str = DATAPLEX_TASK_LINK


class DataplexTasksLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Tasks link."""

    name = "Dataplex Tasks"
    key = "tasks_conf"
    format_str = DATAPLEX_TASKS_LINK


class DataplexLakeLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Lake link."""

    name = "Dataplex Lake"
    key = "dataplex_lake_key"
    format_str = DATAPLEX_LAKE_LINK


class DataplexCatalogEntryGroupLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog EntryGroup link."""

    name = "Dataplex Catalog EntryGroup"
    key = "dataplex_catalog_entry_group_key"
    format_str = DATAPLEX_CATALOG_ENTRY_GROUP_LINK


class DataplexCatalogEntryGroupsLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog EntryGroups link."""

    name = "Dataplex Catalog EntryGroups"
    key = "dataplex_catalog_entry_groups_key"
    format_str = DATAPLEX_CATALOG_ENTRY_GROUPS_LINK


class DataplexCatalogEntryTypeLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog EntryType link."""

    name = "Dataplex Catalog EntryType"
    key = "dataplex_catalog_entry_type_key"
    format_str = DATAPLEX_CATALOG_ENTRY_TYPE_LINK


class DataplexCatalogEntryTypesLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog EntryTypes link."""

    name = "Dataplex Catalog EntryTypes"
    key = "dataplex_catalog_entry_types_key"
    format_str = DATAPLEX_CATALOG_ENTRY_TYPES_LINK


class DataplexCatalogAspectTypeLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog AspectType link."""

    name = "Dataplex Catalog AspectType"
    key = "dataplex_catalog_aspect_type_key"
    format_str = DATAPLEX_CATALOG_ASPECT_TYPE_LINK


class DataplexCatalogAspectTypesLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog AspectTypes link."""

    name = "Dataplex Catalog AspectTypes"
    key = "dataplex_catalog_aspect_types_key"
    format_str = DATAPLEX_CATALOG_ASPECT_TYPES_LINK


class DataplexCatalogEntryLink(BaseGoogleLink):
    """Helper class for constructing Dataplex Catalog Entry link."""

    name = "Dataplex Catalog Entry"
    key = "dataplex_catalog_entry_key"
    format_str = DATAPLEX_CATALOG_ENTRY_LINK
