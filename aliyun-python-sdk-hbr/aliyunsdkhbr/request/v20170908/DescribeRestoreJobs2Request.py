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
from aliyunsdkhbr.endpoint import endpoint_data

class DescribeRestoreJobs2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeRestoreJobs2')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Filterss(self): # RepeatList
		return self.get_query_params().get('Filters')

	def set_Filterss(self, Filters):  # RepeatList
		for depth1 in range(len(Filters)):
			if Filters[depth1].get('Values') is not None:
				for depth2 in range(len(Filters[depth1].get('Values'))):
					self.add_query_param('Filters.' + str(depth1 + 1) + '.Values.' + str(depth2 + 1), Filters[depth1].get('Values')[depth2])
			if Filters[depth1].get('Key') is not None:
				self.add_query_param('Filters.' + str(depth1 + 1) + '.Key', Filters[depth1].get('Key'))
			if Filters[depth1].get('Operator') is not None:
				self.add_query_param('Filters.' + str(depth1 + 1) + '.Operator', Filters[depth1].get('Operator'))
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_RestoreType(self): # String
		return self.get_query_params().get('RestoreType')

	def set_RestoreType(self, RestoreType):  # String
		self.add_query_param('RestoreType', RestoreType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
