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

import uuid
from datetime import datetime

import pytest

from airflow.callbacks.callback_requests import (
    DagCallbackRequest,
    TaskCallbackRequest,
)
from airflow.models.dag import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils import timezone
from airflow.utils.state import State, TaskInstanceState

pytestmark = pytest.mark.db_test


class TestCallbackRequest:
    @pytest.mark.parametrize(
        "input,request_class",
        [
            (
                None,  # to be generated when test is run
                TaskCallbackRequest,
            ),
            (
                DagCallbackRequest(
                    filepath="filepath",
                    dag_id="fake_dag",
                    run_id="fake_run",
                    is_failure_callback=False,
                    bundle_name="testing",
                    bundle_version=None,
                ),
                DagCallbackRequest,
            ),
        ],
    )
    def test_from_json(self, input, request_class):
        if input is None:
            ti = TaskInstance(
                task=BashOperator(
                    task_id="test",
                    bash_command="true",
                    start_date=datetime.now(),
                    dag=DAG(dag_id="id", schedule=None),
                ),
                run_id="fake_run",
                state=State.RUNNING,
                dag_version_id=uuid.uuid4(),
            )
            ti.start_date = timezone.utcnow()

            input = TaskCallbackRequest(
                filepath="filepath", ti=ti, bundle_name="testing", bundle_version=None
            )
        json_str = input.to_json()
        result = request_class.from_json(json_str)
        assert result == input

    def test_taskcallback_to_json_with_start_date_and_end_date(self, session, create_task_instance):
        ti = create_task_instance()
        ti.start_date = timezone.utcnow()
        ti.end_date = timezone.utcnow()
        session.merge(ti)
        session.flush()
        input = TaskCallbackRequest(filepath="filepath", ti=ti, bundle_name="testing", bundle_version=None)
        json_str = input.to_json()
        result = TaskCallbackRequest.from_json(json_str)
        assert input == result

    @pytest.mark.parametrize(
        "task_callback_type,expected_is_failure",
        [
            (None, True),
            (TaskInstanceState.FAILED, True),
            (TaskInstanceState.UP_FOR_RETRY, True),
            (TaskInstanceState.UPSTREAM_FAILED, True),
            (TaskInstanceState.SUCCESS, False),
            (TaskInstanceState.RUNNING, False),
        ],
    )
    def test_is_failure_callback_property(
        self, task_callback_type, expected_is_failure, create_task_instance
    ):
        """Test is_failure_callback property with different task callback types"""
        ti = create_task_instance()

        request = TaskCallbackRequest(
            filepath="filepath",
            ti=ti,
            bundle_name="testing",
            bundle_version=None,
            task_callback_type=task_callback_type,
        )

        assert request.is_failure_callback == expected_is_failure
