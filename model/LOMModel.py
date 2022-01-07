import collections
import logging
import traceback
from collections import OrderedDict
from pprint import pprint
from typing import Container
from fuzzywuzzy import fuzz, process
from .Estructuras.LOM.General import General
from .Estructuras.LOM.LifeCycle import LifeCycle
from .Estructuras.LOM.MetaMEtadata import MetaMetadata
from .Estructuras.LOM.Technical import Technical
from .Estructuras.LOM.Educational import Educational
from .Estructuras.LOM.Rights import Rights
from .Estructuras.LOM.Relation import Relation
from .Estructuras.LOM.Anotation import Annotation
from .Estructuras.LOM.Classification import Classification
from .Estructuras.LOM.Accessibility import Accessibility

class LOM:

    def __init__(self, general=None, life_cycle=None, meta_metadata=None, technical=None, educational=None, rights=None,
                 relation=None, annotation=None, classification=None, accessibility=None):
        logging.basicConfig(filename='logger.log')
        self.general = general
        self.lifeCycle = life_cycle
        self.metaMetadata = meta_metadata
        self.technical = technical
        self.educational = educational
        self.rights = rights
        self.relation = relation
        self.annotation = annotation
        self.classification = classification
        self.accesibility = accessibility

    General = General()

    LifeCycle = LifeCycle()
    
    MetaMetadata = MetaMetadata()

    Technical = Technical()

    Educational = Educational()

    Rights = Rights()

    Relation = Relation()    

    Annotation = Annotation()

    Classification = Classification()

    Accessibility = Accessibility()    

    def to_xml(self):
        return f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <lom xmlns="http://ltsc.ieee.org/xsd/LOM" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ltsc.ieee.org/xsd/LOM http://ltsc.ieee.org/xsd/lomv1.0/lom.xsd">
            {self.general.to_xml() if self.general is not None else ''}
            {self.lifeCycle.to_xml() if self.lifeCycle is not None else ''}
            {self.metaMetadata.to_xml() if self.metaMetadata is not None else ''}
            {self.technical.to_xml() if self.technical is not None else ''}
            {self.educational.to_xml() if self.educational is not None else ''}
            {self.rights.to_xml() if self.rights is not None else ''}
            {self.relation.to_xml() if self.relation is not None else ''}
            {self.annotation.to_xml() if self.annotation is not None else ''}
            {self.classification.to_xml() if self.classification is not None else ''}
            {self.accesibility.to_xml() if self.accesibility is not None else ''}
        </lom>
        """

    def __dict__(self):
        return {'General': self.general.__dict__() if self.general is not None else self.General().__dict__(),
                'Life Cycle': self.lifeCycle.__dict__() if self.lifeCycle is not None else self.LifeCycle().__dict__(),
                'Meta-Metadata': self.metaMetadata.__dict__() if self.metaMetadata is not None else self.MetaMetadata().__dict__(),
                'Technical': self.technical.__dict__() if self.technical is not None else self.Technical().__dict__(),
                'Educational': self.educational.__dict__() if self.educational is not None else self.Educational().__dict__(),
                'Rights': self.rights.__dict__() if self.rights is not None else self.Rights().__dict__(),
                'Relation': self.relation.__dict__() if self.relation is not None else self.Relation().__dict__(),
                'Annotation': self.annotation.__dict__() if self.annotation is not None else self.Annotation().__dict__(),
                'Classification': self.classification.__dict__() if self.classification is not None else self.Classification().__dict__(),
                'Accessibility': self.accesibility.__dict__() if self.accesibility is not None else self.Accessibility().__dict__()}


def determine_lompad_leaf(dictionary: dict, key: str, is_lompad_exported=False):
    """
    Determine which lompad leaf should be mapped.

    :param dictionary: A Dict instance in representation of data to being parsed.
    :param key: Represents the key of LOM standard.
    :param is_lompad_exported: Check if manifest comes from lompad application.

    :return: a dict representing the object mapped.
    :except If key was not found or couldn't invoke a function (by reflection) catch an exception and prints its
    traceback.
    """
    try:
        # Search the key inside dispatch dict.
        for key1 in dispatch.keys():
            if key in key1:
                print(key1)
                try:
                    metodo = dispatch[key1]
                    ejemplo =  metodo(dict(dictionary), is_lompad_exported)
                    return ejemplo
                except Exception as e:
                    print("======>")
                    print(e)
                    oLom = LOM().MetaMetadata
                    oLom.__setattr__(key, None)
                    return oLom.__getattribute__(key)
    except KeyError as ke:
        logging.error(f' Unexpected key {key}, ignoring key, error {ke}')
    except Exception as ex:
        logging.error(f' Error: {ex}')
        print(traceback.format_exc())


def get_keywords(object_data: list):
    """
    Special case function.
    The can be many keywords inside general leaf, so this function get its value and stores it inside a list.

    :param object_data: List of OrderedDict.
    :return: extracted values.
    """
    values = []
    for value in object_data:
        if type(value) is OrderedDict and 'string' in value.keys() and '#text' in value['string'].keys():
            values.append(value['string']['#text'])
        elif type(value) is OrderedDict and '#text' in value.keys():
            values.append(value['#text'])
    return values


def map_attributes(data_original: dict, object_instance, is_lom):

    data_original=collections.OrderedDict(data_original)
    data = data_original.copy()

    """
    What a nice function, isn't it? (Just kidding).

    Extracts meaningful information from dict nodes and stores inside an object instance, inside nodes can be different
    types of information:
    - String
    - Date (as string)

    There are different ways that ExeLearning saves a string that's the why of too many ifs.

    :param data: An ordered dict which contains the information to be extracted.
    :param object_instance: An instance of Any LOM leaf class or its subclasses.
    :return: an object containing parsed information.
    """
    values_labels_dict={}

    try:
        if data is not None and not isinstance(data, list):
            attributes = object_instance.__dir__()
            
            print("===============================================================")
            # print(attributes)
            # print(object_instance)
            hijo=None
            values_labels=[]
            values_labels_dict={}
            # print(data)
            
            for key in data:
                print("padre: ", key)
                key_mapping=key.replace('lomes:', '')
                # print(key_mapping)
                if key_mapping == "keyword":
                    key_mapping="keywordd"
                key_mapping_Upper=key_mapping.capitalize()
                if isinstance(data[key], str):
                    # print("hijo1: ", data[key])
                    values_labels_dict[key]=[data[key]]
                else:
                    for childrens in data[key]:
                        dataKey=data[key]
                        for valDataKey in dataKey:
                            if isinstance(valDataKey, str):
                                contentDataKey = dataKey[valDataKey]
                                if isinstance(contentDataKey, str):
                                    # print(valDataKey)
                                    # print("HijoCollections: ", contentDataKey)
                                    values_labels_dict[valDataKey]=[contentDataKey]
                                else:
                                    aux=True
                                    auxKey=""
                                    for valContentDataKEy in contentDataKey:
                                        if isinstance(contentDataKey[valContentDataKEy], str):
                                            # print("HijoCollectionsFor: ",contentDataKey[valContentDataKEy])
                                            if aux:
                                                auxKey=contentDataKey[valContentDataKEy]
                                                values_labels_dict[contentDataKey[valContentDataKEy]]=list()
                                                aux=False
                                            else:
                                                values_labels_dict.get(auxKey).append(contentDataKey[valContentDataKEy])
                                                aux=True
                                        else:
                                            aux=True
                                            contentContentDataKey = contentDataKey[valContentDataKEy]
                                            for valueContentContetnDatakey in contentContentDataKey:
                                                # print("HijoCollectionsFor2: ",contentContentDataKey[valueContentContetnDatakey])
                                                if isinstance(contentContentDataKey[valueContentContetnDatakey], str):
                                                    if aux:
                                                        auxKey=contentContentDataKey[valueContentContetnDatakey]
                                                        values_labels_dict[contentContentDataKey[valueContentContetnDatakey]]=list()
                                                        aux=False
                                                    else:
                                                        values_labels_dict.get(auxKey).append(contentContentDataKey[valueContentContetnDatakey])
                                                        aux=True
                                                else:
                                                    auxcontentContentDataKey=contentContentDataKey[valueContentContetnDatakey]
                                                    for valAuxcontentContentDataKey in auxcontentContentDataKey:
                                                        if aux:
                                                            auxKey=auxcontentContentDataKey[valAuxcontentContentDataKey]
                                                            values_labels_dict[auxcontentContentDataKey[valAuxcontentContentDataKey]]=list()
                                                            aux=False
                                                        else:
                                                            values_labels_dict.get(auxKey).append(auxcontentContentDataKey[valAuxcontentContentDataKey])
                                                            aux=True
                            else:
                                contentDataKey = valDataKey
                                aux=True
                                auxKey=""
                                for valContentDataKEy in contentDataKey:
                                    if isinstance(contentDataKey[valContentDataKEy], str):
                                        # print("HijoCollectionsFor2: ",contentDataKey[valContentDataKEy])
                                        if aux:
                                            auxKey=contentDataKey[valContentDataKEy]
                                            values_labels_dict[contentDataKey[valContentDataKEy]]=list()
                                            aux=False
                                        else:
                                            values_labels_dict.get(auxKey).append(contentDataKey[valContentDataKEy])
                                            aux=True
                                    else:
                                        aux=True
                                        contentContentDataKey = contentDataKey[valContentDataKEy]
                                        for valueContentContetnDatakey in contentContentDataKey:
                                            # print("HijoCollectionsFor22: ",contentContentDataKey[valueContentContetnDatakey])
                                            if isinstance(contentContentDataKey[valueContentContetnDatakey], str):
                                                if aux:
                                                    auxKey=contentContentDataKey[valueContentContetnDatakey]
                                                    values_labels_dict[contentContentDataKey[valueContentContetnDatakey]]=list()
                                                    aux=False
                                                else:
                                                    values_labels_dict.get(auxKey).append(contentContentDataKey[valueContentContetnDatakey])
                                                    aux=True
                                            else:
                                                auxcontentContentDataKey=contentContentDataKey[valueContentContetnDatakey]
                                                for valAuxcontentContentDataKey in auxcontentContentDataKey:
                                                    if aux:
                                                        auxKey=auxcontentContentDataKey[valAuxcontentContentDataKey]
                                                        values_labels_dict[auxcontentContentDataKey[valAuxcontentContentDataKey]]=list()
                                                        aux=False
                                                    else:
                                                        values_labels_dict.get(auxKey).append(auxcontentContentDataKey[valAuxcontentContentDataKey])
                                                        aux=True
                        break
                # print(values_labels)
                print(values_labels_dict)
                if "@uniqueElementName" not in key_mapping:
                    children_label=object_instance.__getattribute__(key_mapping_Upper)()
                    children_label.addValues(values_labels_dict)
                    # children_label.getValues()
                    values_labels_dict={}
                    if key_mapping == "aggregationLevel":
                        key_mapping="aggregation_level"
                    # print(object_instance,": ",key_mapping)
                    object_instance.__setattr__(key_mapping, children_label)
    except Exception as e:
        print(e)
    return object_instance


def general_leaf(data: dict, is_lom):
    """
    Function to map General Leaf.

    :param data: data from manifest.
    :return: a General class instance. 
    """             
    general_object = map_attributes(data, LOM.General, is_lom)
    return general_object.__dict__(), general_object


def life_cycle_leaf(data: dict, is_lom):
    """
        Function to map Life Cycle Leaf.

        :param data: data from manifest.
        :return: a LifeCycle class instance.
        """
    general_object = map_attributes(data, LOM.LifeCycle, is_lom)

    return general_object.__dict__(), general_object


def meta_metadata_leaf(data: dict, is_lom):
    """
        Function to map Meta MetaData Leaf.

        :param data: data from manifest.
        :return: a MetaMetaData class instance.
        """
    general_object = map_attributes(data, LOM.MetaMetadata, is_lom)

    return general_object.__dict__(), general_object


def technical_leaf(data: dict, is_lom):
    """
        Function to map Technical Leaf.

        :param data: data from manifest.
        :return: a Technical class instance.
        """
    technical_object = map_attributes(data, LOM.Technical, is_lom)
    return technical_object.__dict__(), technical_object


def educational_leaf(data: dict, is_lom):
    """
        Function to map Educational Leaf.

        :param data: data from manifest.
        :return: a Educational class instance.
        """
    educational_object = map_attributes(data, LOM.Educational, is_lom)

    return educational_object.__dict__(), educational_object


def rights_leaf(data: dict, is_lom):
    """
        Function to map Rights Leaf.

        :param data: data from manifest.
        :return: a Rights class instance.
        """
    rights_object = map_attributes(data, LOM.Rights, is_lom)

    return rights_object.__dict__(), rights_object


def relation_leaf(data: dict, is_lom):
    """
        Function to map Relation Leaf.

        :param data: data from manifest.
        :return: a Relation class instance.
        """
    relation_object = map_attributes(data, LOM.Relation, is_lom)
    resource = map_attributes(data['resource'], LOM.Relation.Resource(), is_lom)

    if 'resource' in data.keys():
        if 'identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['identifier'], LOM.Relation.Resource.Identifier(), is_lom)
        elif 'Identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['Identifier'], LOM.Relation.Resource.Identifier(), is_lom)
        else:
            identifier=None

    resource.identifier = identifier
    relation_object.resource = resource

    return relation_object.__dict__(), relation_object


def annotation_leaf(data: dict, is_lom):
    """
        Function to map Annotation Leaf.

        :param data: data from manifest.
        :return: a Annotation class instance.
        """
    annotation_object = map_attributes(data, LOM.Annotation, is_lom)

    return annotation_object.__dict__(), annotation_object


def classification_leaf(data: dict, is_lom):
    """
        Function to map Classification Leaf.

        :param data: data from manifest.
        :return: a Classification class instance.
        """
    classification_object = map_attributes(data, LOM.Classification, is_lom)

    taxon_path = map_attributes(data.get('taxonPath') if data.get('taxonPath') is not None else
                                data.get('taxonPath'), classification_object.TaxonPath(), is_lom)

    taxon = None
    if data.get('taxonPath') is not None and data.get('taxonPath').get('taxon') is not None:
        taxon = map_attributes(data.get('taxonPath').get('taxon')[0]
                               if type(data.get('taxonPath').get('taxon')) is list else
                               data.get('taxonPath').get('taxon'), classification_object.TaxonPath.Taxon(),
                               is_lom)

    elif data.get('taxonPath') is not None and data.get('taxonPath').get('taxon') is not None:
        taxon = map_attributes(data.get('taxonPath').get('taxon')[0]
                               if type(data.get('taxonPath').get('taxon')) is list else
                               data.get('taxonPath').get('taxon'), classification_object.TaxonPath.Taxon(),
                               is_lom)

    classification_object.taxon_path = taxon_path
    classification_object.taxon_path.taxon = taxon

    return classification_object.__dict__(), classification_object


def accessibility_leaf(data: dict, is_lom):
    accessibility_object = map_attributes(data, LOM.Accessibility, is_lom)
    api, features, hazard, control = None, None, None, None

    if data.get('accessibilityAPI') is not None:
        api = map_attributes(data.get('accessibilityAPI'), LOM.Accessibility.AccessibilityAPI(), is_lom)
    elif data.get('accessibilityApi') is not None:
        api = map_attributes(data.get('accessibilityApi'), LOM.Accessibility.AccessibilityAPI(), is_lom)

    if data.get('accessibilityfeatures') is not None:
        features = map_attributes(data.get('accessibilityfeatures'), LOM.Accessibility.AccessibilityFeatures(), is_lom)
    elif data.get('accessibilityFeatures') is not None:
        features = map_attributes(data.get('accessibilityFeatures'), LOM.Accessibility.AccessibilityFeatures(), is_lom)

    if data.get('accessibilityhazard') is not None:
        hazard = map_attributes(data.get('accessibilityhazard'), LOM.Accessibility.AccessibilityHazard(), is_lom)
    elif data.get('accessibilityHazard') is not None:
        hazard = map_attributes(data.get('accessibilityHazard'), LOM.Accessibility.AccessibilityHazard(), is_lom)

    if data.get('accessibilitycontrol') is not None:
        control = map_attributes(data.get('accessibilitycontrol'), LOM.Accessibility.AccessibilityControl(), is_lom)
    elif data.get('accessibilityControl') is not None:
        control = map_attributes(data.get('accessibilityControl'), LOM.Accessibility.AccessibilityControl(), is_lom)



    accessibility_object.accessibility_api = api
    accessibility_object.accessibility_features = features
    accessibility_object.accessibility_hazard = hazard
    accessibility_object.accessibility_control = control


    return accessibility_object.__dict__(), accessibility_object


dispatch = {
    'general': general_leaf, 'lifeCycle': life_cycle_leaf, 'metaMetadata': meta_metadata_leaf,
    'technical': technical_leaf, 'educational': educational_leaf,
    'rights': rights_leaf, 'relation': relation_leaf, 'annotation': annotation_leaf,
    'classification': classification_leaf, 'accesibility': accessibility_leaf
}

dispatch_update = {
    'general': general_leaf, 'lifeCycle': life_cycle_leaf, 'metaMetadata': meta_metadata_leaf,
    'technical': technical_leaf, 'educational': educational_leaf,
    'rights': rights_leaf, 'relation': relation_leaf, 'annotation': annotation_leaf,
    'classification': classification_leaf, 'accesibility': accessibility_leaf
}


def update_leaf(leaf, model, data):
    print('UPDATE')
    import json
    data_as_dict = json.loads(data)
    metodo = dispatch_update.get(leaf)
    data = data_as_dict.copy()

    for key in data_as_dict.keys():
        components = str(key).lower().split(' ')
        components = components[0] + ''.join(x.title() for x in components[1:])
        data[components] = data.pop(key)

    model.__setattr__(leaf, metodo(data, True)[1])

    return model
