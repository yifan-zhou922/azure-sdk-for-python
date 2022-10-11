# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Application
from ._models_py3 import ApplicationArtifact
from ._models_py3 import ApplicationDefinition
from ._models_py3 import ApplicationDefinitionListResult
from ._models_py3 import ApplicationListResult
from ._models_py3 import ApplicationPatchable
from ._models_py3 import ApplicationProviderAuthorization
from ._models_py3 import ErrorResponse
from ._models_py3 import GenericResource
from ._models_py3 import Identity
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import Plan
from ._models_py3 import PlanPatchable
from ._models_py3 import Resource
from ._models_py3 import Sku

from ._application_client_enums import ApplicationArtifactType
from ._application_client_enums import ApplicationLockLevel
from ._application_client_enums import ProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Application",
    "ApplicationArtifact",
    "ApplicationDefinition",
    "ApplicationDefinitionListResult",
    "ApplicationListResult",
    "ApplicationPatchable",
    "ApplicationProviderAuthorization",
    "ErrorResponse",
    "GenericResource",
    "Identity",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "Plan",
    "PlanPatchable",
    "Resource",
    "Sku",
    "ApplicationArtifactType",
    "ApplicationLockLevel",
    "ProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()