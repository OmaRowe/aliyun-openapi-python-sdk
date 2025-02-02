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
from aliyunsdkcams.endpoint import endpoint_data

class AddChatappPhoneNumberRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'AddChatappPhoneNumber')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PreValidateId(self): # String
		return self.get_body_params().get('PreValidateId')

	def set_PreValidateId(self, PreValidateId):  # String
		self.add_body_params('PreValidateId', PreValidateId)
	def get_VerifiedName(self): # String
		return self.get_body_params().get('VerifiedName')

	def set_VerifiedName(self, VerifiedName):  # String
		self.add_body_params('VerifiedName', VerifiedName)
	def get_PhoneNumber(self): # String
		return self.get_body_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_body_params('PhoneNumber', PhoneNumber)
	def get_Cc(self): # String
		return self.get_body_params().get('Cc')

	def set_Cc(self, Cc):  # String
		self.add_body_params('Cc', Cc)
	def get_CustSpaceId(self): # String
		return self.get_body_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_body_params('CustSpaceId', CustSpaceId)
