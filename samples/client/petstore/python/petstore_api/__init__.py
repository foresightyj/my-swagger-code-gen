# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.additional_properties_class import AdditionalPropertiesClass
from .models.animal import Animal
from .models.animal_farm import AnimalFarm
from .models.api_response import ApiResponse
from .models.array_of_array_of_number_only import ArrayOfArrayOfNumberOnly
from .models.array_of_number_only import ArrayOfNumberOnly
from .models.array_test import ArrayTest
from .models.capitalization import Capitalization
from .models.category import Category
from .models.class_model import ClassModel
from .models.client import Client
from .models.enum_arrays import EnumArrays
from .models.enum_class import EnumClass
from .models.enum_test import EnumTest
from .models.format_test import FormatTest
from .models.has_only_read_only import HasOnlyReadOnly
from .models.list import List
from .models.map_test import MapTest
from .models.mixed_properties_and_additional_properties_class import MixedPropertiesAndAdditionalPropertiesClass
from .models.model_200_response import Model200Response
from .models.model_return import ModelReturn
from .models.name import Name
from .models.number_only import NumberOnly
from .models.order import Order
from .models.outer_boolean import OuterBoolean
from .models.outer_composite import OuterComposite
from .models.outer_enum import OuterEnum
from .models.outer_number import OuterNumber
from .models.outer_string import OuterString
from .models.pet import Pet
from .models.read_only_first import ReadOnlyFirst
from .models.special_model_name import SpecialModelName
from .models.tag import Tag
from .models.user import User
from .models.cat import Cat
from .models.dog import Dog

# import apis into sdk package
from .apis.fake_api import FakeApi
from .apis.pet_api import PetApi
from .apis.store_api import StoreApi
from .apis.user_api import UserApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
