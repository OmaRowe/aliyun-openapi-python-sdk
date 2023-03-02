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
from aliyunsdkltl.endpoint import endpoint_data

class UploadMPCoSPhaseTextInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ltl', '2019-05-10', 'UploadMPCoSPhaseTextInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PhaseData(self): # String
		return self.get_query_params().get('PhaseData')

	def set_PhaseData(self, PhaseData):  # String
		self.add_query_param('PhaseData', PhaseData)
	def get_PhaseId(self): # String
		return self.get_query_params().get('PhaseId')

	def set_PhaseId(self, PhaseId):  # String
		self.add_query_param('PhaseId', PhaseId)
	def get_ApiVersion(self): # String
		return self.get_query_params().get('ApiVersion')

	def set_ApiVersion(self, ApiVersion):  # String
		self.add_query_param('ApiVersion', ApiVersion)
	def get_BizChainId(self): # String
		return self.get_query_params().get('BizChainId')

	def set_BizChainId(self, BizChainId):  # String
		self.add_query_param('BizChainId', BizChainId)
	def get_DataKey(self): # String
		return self.get_query_params().get('DataKey')

	def set_DataKey(self, DataKey):  # String
		self.add_query_param('DataKey', DataKey)
	def get_DataSeq(self): # String
		return self.get_query_params().get('DataSeq')

	def set_DataSeq(self, DataSeq):  # String
		self.add_query_param('DataSeq', DataSeq)
	def get_PhaseGroupId(self): # String
		return self.get_query_params().get('PhaseGroupId')

	def set_PhaseGroupId(self, PhaseGroupId):  # String
		self.add_query_param('PhaseGroupId', PhaseGroupId)
	def get_RelatedDataList(self): # Json
		return self.get_query_params().get('RelatedDataList')

	def set_RelatedDataList(self, RelatedDataList):  # Json
		self.add_query_param('RelatedDataList', RelatedDataList)
