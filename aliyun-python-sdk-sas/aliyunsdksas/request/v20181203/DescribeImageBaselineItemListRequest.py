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
from aliyunsdksas.endpoint import endpoint_data

class DescribeImageBaselineItemListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageBaselineItemList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BaselineClassKey(self): # String
		return self.get_query_params().get('BaselineClassKey')

	def set_BaselineClassKey(self, BaselineClassKey):  # String
		self.add_query_param('BaselineClassKey', BaselineClassKey)
	def get_ScanRanges(self): # RepeatList
		return self.get_query_params().get('ScanRange')

	def set_ScanRanges(self, ScanRange):  # RepeatList
		for depth1 in range(len(ScanRange)):
			self.add_query_param('ScanRange.' + str(depth1 + 1), ScanRange[depth1])
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ImageUuid(self): # String
		return self.get_query_params().get('ImageUuid')

	def set_ImageUuid(self, ImageUuid):  # String
		self.add_query_param('ImageUuid', ImageUuid)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_BaselineNameKey(self): # String
		return self.get_query_params().get('BaselineNameKey')

	def set_BaselineNameKey(self, BaselineNameKey):  # String
		self.add_query_param('BaselineNameKey', BaselineNameKey)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_Uuidss(self): # RepeatList
		return self.get_query_params().get('Uuids')

	def set_Uuidss(self, Uuids):  # RepeatList
		for depth1 in range(len(Uuids)):
			self.add_query_param('Uuids.' + str(depth1 + 1), Uuids[depth1])
