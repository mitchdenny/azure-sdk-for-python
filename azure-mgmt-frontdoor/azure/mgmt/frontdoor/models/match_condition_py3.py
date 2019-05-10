# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MatchCondition(Model):
    """Define a match condition.

    All required parameters must be populated in order to send to Azure.

    :param match_variable: Required. Request variable to compare with.
     Possible values include: 'RemoteAddr', 'RequestMethod', 'QueryString',
     'PostArgs', 'RequestUri', 'RequestHeader', 'RequestBody', 'Cookies'
    :type match_variable: str or ~azure.mgmt.frontdoor.models.MatchVariable
    :param selector: Match against a specific key from the QueryString,
     PostArgs, RequestHeader or Cookies variables. Default is null.
    :type selector: str
    :param operator: Required. Comparison type to use for matching with the
     variable value. Possible values include: 'Any', 'IPMatch', 'GeoMatch',
     'Equal', 'Contains', 'LessThan', 'GreaterThan', 'LessThanOrEqual',
     'GreaterThanOrEqual', 'BeginsWith', 'EndsWith', 'RegEx'
    :type operator: str or ~azure.mgmt.frontdoor.models.Operator
    :param negate_condition: Describes if the result of this condition should
     be negated.
    :type negate_condition: bool
    :param match_value: Required. List of possible match values.
    :type match_value: list[str]
    :param transforms: List of transforms.
    :type transforms: list[str or ~azure.mgmt.frontdoor.models.TransformType]
    """

    _validation = {
        'match_variable': {'required': True},
        'operator': {'required': True},
        'match_value': {'required': True},
    }

    _attribute_map = {
        'match_variable': {'key': 'matchVariable', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'negate_condition': {'key': 'negateCondition', 'type': 'bool'},
        'match_value': {'key': 'matchValue', 'type': '[str]'},
        'transforms': {'key': 'transforms', 'type': '[str]'},
    }

    def __init__(self, *, match_variable, operator, match_value, selector: str=None, negate_condition: bool=None, transforms=None, **kwargs) -> None:
        super(MatchCondition, self).__init__(**kwargs)
        self.match_variable = match_variable
        self.selector = selector
        self.operator = operator
        self.negate_condition = negate_condition
        self.match_value = match_value
        self.transforms = transforms
