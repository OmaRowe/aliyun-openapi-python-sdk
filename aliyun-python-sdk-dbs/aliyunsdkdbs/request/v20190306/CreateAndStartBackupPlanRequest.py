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
from aliyunsdkdbs.endpoint import endpoint_data

class CreateAndStartBackupPlanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dbs', '2019-03-06', 'CreateAndStartBackupPlan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DatabaseType(self): # String
		return self.get_query_params().get('DatabaseType')

	def set_DatabaseType(self, DatabaseType):  # String
		self.add_query_param('DatabaseType', DatabaseType)
	def get_BackupGatewayId(self): # Long
		return self.get_query_params().get('BackupGatewayId')

	def set_BackupGatewayId(self, BackupGatewayId):  # Long
		self.add_query_param('BackupGatewayId', BackupGatewayId)
	def get_SourceEndpointUserName(self): # String
		return self.get_query_params().get('SourceEndpointUserName')

	def set_SourceEndpointUserName(self, SourceEndpointUserName):  # String
		self.add_query_param('SourceEndpointUserName', SourceEndpointUserName)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_DatabaseRegion(self): # String
		return self.get_query_params().get('DatabaseRegion')

	def set_DatabaseRegion(self, DatabaseRegion):  # String
		self.add_query_param('DatabaseRegion', DatabaseRegion)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_BackupStartTime(self): # String
		return self.get_query_params().get('BackupStartTime')

	def set_BackupStartTime(self, BackupStartTime):  # String
		self.add_query_param('BackupStartTime', BackupStartTime)
	def get_SourceEndpointIP(self): # String
		return self.get_query_params().get('SourceEndpointIP')

	def set_SourceEndpointIP(self, SourceEndpointIP):  # String
		self.add_query_param('SourceEndpointIP', SourceEndpointIP)
	def get_CrossRoleName(self): # String
		return self.get_query_params().get('CrossRoleName')

	def set_CrossRoleName(self, CrossRoleName):  # String
		self.add_query_param('CrossRoleName', CrossRoleName)
	def get_BackupStorageType(self): # String
		return self.get_query_params().get('BackupStorageType')

	def set_BackupStorageType(self, BackupStorageType):  # String
		self.add_query_param('BackupStorageType', BackupStorageType)
	def get_DuplicationArchivePeriod(self): # Integer
		return self.get_query_params().get('DuplicationArchivePeriod')

	def set_DuplicationArchivePeriod(self, DuplicationArchivePeriod):  # Integer
		self.add_query_param('DuplicationArchivePeriod', DuplicationArchivePeriod)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_BackupLogIntervalSeconds(self): # Integer
		return self.get_query_params().get('BackupLogIntervalSeconds')

	def set_BackupLogIntervalSeconds(self, BackupLogIntervalSeconds):  # Integer
		self.add_query_param('BackupLogIntervalSeconds', BackupLogIntervalSeconds)
	def get_FromApp(self): # String
		return self.get_query_params().get('FromApp')

	def set_FromApp(self, FromApp):  # String
		self.add_query_param('FromApp', FromApp)
	def get_SourceEndpointPassword(self): # String
		return self.get_query_params().get('SourceEndpointPassword')

	def set_SourceEndpointPassword(self, SourceEndpointPassword):  # String
		self.add_query_param('SourceEndpointPassword', SourceEndpointPassword)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_BackupMethod(self): # String
		return self.get_query_params().get('BackupMethod')

	def set_BackupMethod(self, BackupMethod):  # String
		self.add_query_param('BackupMethod', BackupMethod)
	def get_BackupRetentionPeriod(self): # Integer
		return self.get_query_params().get('BackupRetentionPeriod')

	def set_BackupRetentionPeriod(self, BackupRetentionPeriod):  # Integer
		self.add_query_param('BackupRetentionPeriod', BackupRetentionPeriod)
	def get_BackupPeriod(self): # String
		return self.get_query_params().get('BackupPeriod')

	def set_BackupPeriod(self, BackupPeriod):  # String
		self.add_query_param('BackupPeriod', BackupPeriod)
	def get_BackupSpeedLimit(self): # Long
		return self.get_query_params().get('BackupSpeedLimit')

	def set_BackupSpeedLimit(self, BackupSpeedLimit):  # Long
		self.add_query_param('BackupSpeedLimit', BackupSpeedLimit)
	def get_SourceEndpointInstanceType(self): # String
		return self.get_query_params().get('SourceEndpointInstanceType')

	def set_SourceEndpointInstanceType(self, SourceEndpointInstanceType):  # String
		self.add_query_param('SourceEndpointInstanceType', SourceEndpointInstanceType)
	def get_BackupPlanName(self): # String
		return self.get_query_params().get('BackupPlanName')

	def set_BackupPlanName(self, BackupPlanName):  # String
		self.add_query_param('BackupPlanName', BackupPlanName)
	def get_OSSBucketName(self): # String
		return self.get_query_params().get('OSSBucketName')

	def set_OSSBucketName(self, OSSBucketName):  # String
		self.add_query_param('OSSBucketName', OSSBucketName)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_SourceEndpointRegion(self): # String
		return self.get_query_params().get('SourceEndpointRegion')

	def set_SourceEndpointRegion(self, SourceEndpointRegion):  # String
		self.add_query_param('SourceEndpointRegion', SourceEndpointRegion)
	def get_SourceEndpointInstanceID(self): # String
		return self.get_query_params().get('SourceEndpointInstanceID')

	def set_SourceEndpointInstanceID(self, SourceEndpointInstanceID):  # String
		self.add_query_param('SourceEndpointInstanceID', SourceEndpointInstanceID)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BackupPlanId(self): # String
		return self.get_query_params().get('BackupPlanId')

	def set_BackupPlanId(self, BackupPlanId):  # String
		self.add_query_param('BackupPlanId', BackupPlanId)
	def get_InstanceClass(self): # String
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self, InstanceClass):  # String
		self.add_query_param('InstanceClass', InstanceClass)
	def get_SourceEndpointDatabaseName(self): # String
		return self.get_query_params().get('SourceEndpointDatabaseName')

	def set_SourceEndpointDatabaseName(self, SourceEndpointDatabaseName):  # String
		self.add_query_param('SourceEndpointDatabaseName', SourceEndpointDatabaseName)
	def get_DuplicationInfrequentAccessPeriod(self): # Integer
		return self.get_query_params().get('DuplicationInfrequentAccessPeriod')

	def set_DuplicationInfrequentAccessPeriod(self, DuplicationInfrequentAccessPeriod):  # Integer
		self.add_query_param('DuplicationInfrequentAccessPeriod', DuplicationInfrequentAccessPeriod)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_EnableBackupLog(self): # Boolean
		return self.get_query_params().get('EnableBackupLog')

	def set_EnableBackupLog(self, EnableBackupLog):  # Boolean
		self.add_query_param('EnableBackupLog', EnableBackupLog)
	def get_CrossAliyunId(self): # String
		return self.get_query_params().get('CrossAliyunId')

	def set_CrossAliyunId(self, CrossAliyunId):  # String
		self.add_query_param('CrossAliyunId', CrossAliyunId)
	def get_BackupObjects(self): # String
		return self.get_query_params().get('BackupObjects')

	def set_BackupObjects(self, BackupObjects):  # String
		self.add_query_param('BackupObjects', BackupObjects)
	def get_BackupRateLimit(self): # Long
		return self.get_query_params().get('BackupRateLimit')

	def set_BackupRateLimit(self, BackupRateLimit):  # Long
		self.add_query_param('BackupRateLimit', BackupRateLimit)
	def get_UsedTime(self): # Integer
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self, UsedTime):  # Integer
		self.add_query_param('UsedTime', UsedTime)
	def get_SourceEndpointPort(self): # Integer
		return self.get_query_params().get('SourceEndpointPort')

	def set_SourceEndpointPort(self, SourceEndpointPort):  # Integer
		self.add_query_param('SourceEndpointPort', SourceEndpointPort)
	def get_StorageRegion(self): # String
		return self.get_query_params().get('StorageRegion')

	def set_StorageRegion(self, StorageRegion):  # String
		self.add_query_param('StorageRegion', StorageRegion)
	def get_SourceEndpointOracleSID(self): # String
		return self.get_query_params().get('SourceEndpointOracleSID')

	def set_SourceEndpointOracleSID(self, SourceEndpointOracleSID):  # String
		self.add_query_param('SourceEndpointOracleSID', SourceEndpointOracleSID)
	def get_BackupStrategyType(self): # String
		return self.get_query_params().get('BackupStrategyType')

	def set_BackupStrategyType(self, BackupStrategyType):  # String
		self.add_query_param('BackupStrategyType', BackupStrategyType)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
