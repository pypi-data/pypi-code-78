from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.arm.base_resource_check import BaseResourceCheck

class AzureManagedDiscEncryption(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Azure managed disk have encryption enabled"
        id = "CKV_AZURE_2"
        supported_resources = ['Microsoft.Compute/disks']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "properties" in conf:
            if "encryptionSettings" in conf["properties"]:
                if "enabled" in conf["properties"]["encryptionSettings"]:
                    if str(conf["properties"]["encryptionSettings"]["enabled"]).lower() == "true":
                        return CheckResult.PASSED
        return CheckResult.FAILED

check = AzureManagedDiscEncryption()
