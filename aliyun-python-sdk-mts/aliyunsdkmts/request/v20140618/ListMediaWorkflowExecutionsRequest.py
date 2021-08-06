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
from aliyunsdkmts.endpoint import endpoint_data

class ListMediaWorkflowExecutionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'ListMediaWorkflowExecutions','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_NextPageToken(self): # String
		return self.get_query_params().get('NextPageToken')

	def set_NextPageToken(self, NextPageToken):  # String
		self.add_query_param('NextPageToken', NextPageToken)
	def get_MediaWorkflowId(self): # String
		return self.get_query_params().get('MediaWorkflowId')

	def set_MediaWorkflowId(self, MediaWorkflowId):  # String
		self.add_query_param('MediaWorkflowId', MediaWorkflowId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_MaximumPageSize(self): # Long
		return self.get_query_params().get('MaximumPageSize')

	def set_MaximumPageSize(self, MaximumPageSize):  # Long
		self.add_query_param('MaximumPageSize', MaximumPageSize)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_MediaWorkflowName(self): # String
		return self.get_query_params().get('MediaWorkflowName')

	def set_MediaWorkflowName(self, MediaWorkflowName):  # String
		self.add_query_param('MediaWorkflowName', MediaWorkflowName)
	def get_InputFileURL(self): # String
		return self.get_query_params().get('InputFileURL')

	def set_InputFileURL(self, InputFileURL):  # String
		self.add_query_param('InputFileURL', InputFileURL)
