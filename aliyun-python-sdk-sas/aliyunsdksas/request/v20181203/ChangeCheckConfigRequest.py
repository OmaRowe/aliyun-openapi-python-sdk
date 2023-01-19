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

class ChangeCheckConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ChangeCheckConfig')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StandardIdss(self): # RepeatList
		return self.get_query_params().get('StandardIds')

	def set_StandardIdss(self, StandardIds):  # RepeatList
		for depth1 in range(len(StandardIds)):
			self.add_query_param('StandardIds.' + str(depth1 + 1), StandardIds[depth1])
	def get_CycleDayss(self): # RepeatList
		return self.get_query_params().get('CycleDays')

	def set_CycleDayss(self, CycleDays):  # RepeatList
		for depth1 in range(len(CycleDays)):
			self.add_query_param('CycleDays.' + str(depth1 + 1), CycleDays[depth1])
	def get_StartTime(self): # Integer
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Integer
		self.add_query_param('StartTime', StartTime)
	def get_EndTime(self): # Integer
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Integer
		self.add_query_param('EndTime', EndTime)
