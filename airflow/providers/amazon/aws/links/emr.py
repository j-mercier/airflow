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

from airflow.providers.amazon.aws.links.base_aws import BASE_AWS_CONSOLE_LINK, BaseAwsLink


class EmrClusterLink(BaseAwsLink):
    """Helper class for constructing AWS EMR Cluster Link"""

    name = "EMR Cluster"
    key = "emr_cluster"
    format_str = BASE_AWS_CONSOLE_LINK + "/emr/home?region={region_name}#/clusterDetails/{job_flow_id}"


class EmrLogsLink(BaseAwsLink):
    """Helper class for constructing AWS EMR Logs Link"""

    name = "EMR Cluster Logs"
    key = "emr_logs"
    format_str = BASE_AWS_CONSOLE_LINK + "/s3/buckets/{log_uri}?region={region_name}&prefix={job_flow_id}/"
