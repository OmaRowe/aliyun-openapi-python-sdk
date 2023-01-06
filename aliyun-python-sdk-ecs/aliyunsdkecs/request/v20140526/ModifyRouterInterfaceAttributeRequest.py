# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkecs.endpoint import endpoint_data

class ModifyRouterInterfaceAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyRouterInterfaceAttribute')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OppositeRouterId(self): # String
		return self.get_query_params().get('OppositeRouterId')

	def set_OppositeRouterId(self, OppositeRouterId):  # String
		self.add_query_param('OppositeRouterId', OppositeRouterId)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_HealthCheckTargetIp(self): # String
		return self.get_query_params().get('HealthCheckTargetIp')

	def set_HealthCheckTargetIp(self, HealthCheckTargetIp):  # String
		self.add_query_param('HealthCheckTargetIp', HealthCheckTargetIp)
	def get_OppositeInterfaceId(self): # String
		return self.get_query_params().get('OppositeInterfaceId')

	def set_OppositeInterfaceId(self, OppositeInterfaceId):  # String
		self.add_query_param('OppositeInterfaceId', OppositeInterfaceId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RouterInterfaceId(self): # String
		return self.get_query_params().get('RouterInterfaceId')

	def set_RouterInterfaceId(self, RouterInterfaceId):  # String
		self.add_query_param('RouterInterfaceId', RouterInterfaceId)
	def get_OppositeInterfaceOwnerId(self): # Long
		return self.get_query_params().get('OppositeInterfaceOwnerId')

	def set_OppositeInterfaceOwnerId(self, OppositeInterfaceOwnerId):  # Long
		self.add_query_param('OppositeInterfaceOwnerId', OppositeInterfaceOwnerId)
	def get_HealthCheckSourceIp(self): # String
		return self.get_query_params().get('HealthCheckSourceIp')

	def set_HealthCheckSourceIp(self, HealthCheckSourceIp):  # String
		self.add_query_param('HealthCheckSourceIp', HealthCheckSourceIp)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_OppositeRouterType(self): # String
		return self.get_query_params().get('OppositeRouterType')

	def set_OppositeRouterType(self, OppositeRouterType):  # String
		self.add_query_param('OppositeRouterType', OppositeRouterType)
