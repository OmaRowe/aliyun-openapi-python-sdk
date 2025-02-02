# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest


class DescribeAvailableResourceRequest(RpcRequest):
    def __init__(self):
        RpcRequest.__init__(self, 'Eci', '2018-08-08', 'DescribeAvailableResource', 'eci')

    def get_ResourceOwnerAccount(self):
        return self.get_query_params().get('ResourceOwnerAccount')

    def set_ResourceOwnerAccount(self, ResourceOwnerAccount):
        self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)

    def get_OwnerAccount(self):
        return self.get_query_params().get('OwnerAccount')

    def set_OwnerAccount(self, OwnerAccount):
        self.add_query_param('OwnerAccount', OwnerAccount)

    def get_OwnerId(self):
        return self.get_query_params().get('OwnerId')

    def set_OwnerId(self, OwnerId):
        self.add_query_param('OwnerId', OwnerId)

    def get_ResourceOwnerId(self):
        return self.get_query_params().get('ResourceOwnerId')

    def set_ResourceOwnerId(self, ResourceOwnerId):
        self.add_query_param('ResourceOwnerId', ResourceOwnerId)

    def get_ZoneId(self):
        return self.get_query_params().get('ZoneId')

    def set_ZoneId(self, ZoneId):
        self.add_query_param('ZoneId', ZoneId)

    def get_DestinationResource(self):
        return self.get_query_params().get("DestinationResource")

    def set_DestinationResource(self, DestinationResource):
        if DestinationResource.get("Category") is not None:
            self.add_query_param("DestinationResource.Category", DestinationResource.get("Category"))
        if DestinationResource.get("Value") is not None:
            self.add_query_param("DestinationResource.Value", DestinationResource.get("Value"))
        if DestinationResource.get("Cores") is not None:
            self.add_query_param("DestinationResource.Cores", DestinationResource.get("Cores"))
        if DestinationResource.get("Memory") is not None:
            self.add_query_param("DestinationResource.Memory", DestinationResource.get("Memory"))

    def get_RegionId(self):
        return self.get_query_params().get("RegionId")

    def set_RegionId(self, RegionId):
        self.add_query_param("RegionId", RegionId)

    def get_SpotResource(self):
        return self.get_query_params().get("SpotResource")

    def set_SpotResource(self, SpotResource):
        if DestinationResource.get("SpotStrategy") is not None:
            self.add_query_param("SpotResource.SpotStrategy", SpotResource.get("SpotStrategy"))
        if DestinationResource.get("SpotPriceLimit") is not None:
            self.add_query_param("SpotResource.SpotPriceLimit", SpotResource.get("SpotPriceLimit"))
        if DestinationResource.get("SpotDuration") is not None:
            self.add_query_param("SpotResource.SpotDuration", SpotResource.get("SpotDuration"))




