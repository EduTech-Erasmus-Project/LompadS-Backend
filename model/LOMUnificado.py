import collections
import logging
import traceback
from collections import OrderedDict
from pprint import pprint
from typing import Container
from fuzzywuzzy import fuzz, process


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

    class General:
        identifier = None
        title = None
        language = None
        description = None
        keywordd = None
        coverage = None
        structure = None
        aggregation_level = None

        def __init__(self, identifier=None, title='', language='', description='', keywordd=None, coverage='',
                     structure='', aggregation_level=''):
            self.identifier = identifier
            self.title = title
            self.language = language
            self.description = description
            self.keywordd = keywordd
            self.coverage = coverage
            self.structure = structure
            self.aggregation_level = aggregation_level

        class Identifier:
            catalog = []
            entry = []

            def __init__(self, catalog=[], entry=[]):
                self.catalog = catalog
                self.entry = entry
            
            def addValues(self,atributes):
                self.catalog=atributes.get('lomes:catalog')
                self.entry=atributes.get('lomes:entry')
                    
            def getValues(self):
                print("Catalog: ", self.catalog)
                print("Entry: ", self.entry)

            def to_xml(self):
                return f"""<identifier>
                <catalog>{self.catalog}</catalog>
                <entry>{self.entry}</entry>
                </identifier>"""

            def __dict__(self):
                return {'Catalog': self.catalog, 'Entry': self.entry}

        class Title:
            language=[]
            title=[]

            def __init__(self, language=[], title=[]):
                self.language = language
                self.title = title
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')
                self.title=atributes.get('#text')
                    
            def getValues(self):
                print("Languaje: ", self.language)
                print("Title: ", self.title)

            def to_xml(self):
                return f"""<title>
                <string language="{self.language}">{self.title}</string>
                </title>"""

            def __dict__(self):
                return {'Languaje': self.language, 'Tittle': self.title}
        
        class Language:
            language=[]

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                    self.language=atributes.get('language')
                    
            def getValues(self):
                print("Languaje: ", self.language)
            

            def to_xml(self):
                return f"""<language>{self.language}</language>"""

            def __dict__(self):
                return {'Languaje': self.language}
        
        class Description:

            language=[]
            description=[]

            def __init__(self, language=[], description=[]):
                self.language = language
                self.description = description
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')
                self.description=atributes.get('#text')
                    
            def getValues(self):
                print("Languaje: ", self.language)
                print("Description: ", self.description)

            def to_xml(self):
                return f"""<description>
                <string language="{self.language}">{self.description}</string>
                </description>"""

            def __dict__(self):
                return {'Languaje': self.language, 'Description: ': self.description}
        
        class Keywordd:

            language=[]
            keywordd=[]

            def __init__(self, language=[], keywordd=[]):
                self.language = language
                self.keywordd = keywordd
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')
                self.keywordd=atributes.get('#text')
            def getValues(self):
                print("Languaje: ", self.language)
                print("Keyword: ", self.keywordd)

            def to_xml(self):
                return f"""<string  language="{self.language}">{self.keywordd}</string>"""

            def __dict__(self):
                return {'Languaje': self.language, 'Keyword: ': self.keywordd}
        
        class Aggregationlevel:

            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                for i in range(len(atributes)):
                    if i%2==0:
                        self.source.append(atributes[i])
                    else:
                        self.value.append(atributes[i])
                    
            def getValues(self):
                print("Source: ", self.source)
                print("Value: ", self.value)

            def to_xml(self):
                return f"""<aggregationLevel>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </aggregationLevel>"""

            def __dict__(self):
                return {'Source': self.source, 'Value: ': self.value}

        def get_keyword(self):
            if type(self.keywordd) is list:
                elements = []
                for element in self.keywordd:
                    elements.append(f'{element},')
                return elements
            else:
                return self.keywordd

        def get_xml_keywords(self):
            if type(self.keywordd) is list:
                content = ""
                for key in self.keywordd:
                    content += f"""<string language="en">{key}</string>\n"""
                return content
            else:
                return self.keywordd
        
        class Coverage:

            language=[]
            coverage=[]

            def __init__(self, language=[], coverage=[]):
                self.language = language
                self.coverage = coverage
            
            def addValues(self,atributes):
                for i in range(len(atributes)):
                    if i%2==0:
                        self.language.append(atributes[i])
                    else:
                        self.coverage.append(atributes[i])
                    
            def getValues(self):
                print("Language: ", self.language)
                print("Coverage: ", self.coverage)

            def to_xml(self):
                return f"""<coverage>
                <string language="{self.language}">{self.coverage}</string>
                </coverage>"""

            def __dict__(self):
                return {'Language': self.language, 'Coverage: ': self.coverage}
        
        class Structure:
            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                for i in range(len(atributes)):
                    if i%2==0:
                        self.source.append(atributes[i])
                    else:
                        self.value.append(atributes[i])
                    
            def getValues(self):
                print("Source: ", self.language)
                print("Value: ", self.coverage)

            def to_xml(self):
                return f""" <structure>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </structure>"""

            def __dict__(self):
                return {'Source': self.source, 'Value: ': self.value}

        def to_xml(self):
            return f"""<general>
                {'' if isinstance(self.identifier, str) else self.identifier.to_xml() if self.identifier is not None else ''}
                {'' if isinstance(self.title, str) else self.title.to_xml() if self.title is not None else ''}
                {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
                {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
                {'' if isinstance(self.keywordd, str) else self.keywordd.to_xml() if self.keywordd is not None else ''}
                {'' if isinstance(self.coverage, str) else self.coverage.to_xml() if self.coverage is not None else ''}
                {'' if isinstance(self.structure, str) else self.structure.to_xml() if self.structure is not None else ''}
                {'' if isinstance(self.aggregation_level, str) else self.aggregation_level.to_xml() if self.aggregation_level is not None else ''}
            </general>"""

        def __dict__(self):
            return {'Identifier': self.identifier.__dict__() if self.identifier is not None else '',
                    'Title': self.title, 'Language': self.language,
                    'Description': self.description, 'Keyword': self.get_keyword(), 'Coverage': self.coverage,
                    'Structure': self.structure, 'Aggregation Level': self.aggregation_level}

    class LifeCycle:
        version = None
        status = None
        contribute = None

        def __init__(self, version='', status='', contribute=None):
            self.version = version
            self.status = status
            self.contribute = contribute

        class Contribute:
            source = []
            value = []
            entity = []
            datetime = []
            description_string = []

            def __init__(self, source=[], value=[], entity=[], datetime=[], description_string=[]):
                self.source=source
                self.value=value
                self.entity=entity
                self.datetime=datetime
                self.description_string=description_string
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')
                self.entity=atributes.get('lomes:entity')
                self.datetime=atributes.get('lomes:dateTime')
                self.description_string=atributes.get('lomes:string')

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value, 'Entity': self.entity, 'Datetime': self.datetime, 'Description_string': self.description_string}

            def to_xml(self):
                return f"""<contribute>
                <role>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </role>
                <entity>{self.entity}</entity>
                <date>
                <dateTime>{self.datetime}</dateTime>
                <description>
                <string>{self.description_string}</string>
                </description>
                </date>
                </contribute>"""

        def __dict__(self):
            return {'Version': self.version, 'Status': self.status,
                    'Contribute': self.contribute.__dict__() if self.contribute is not None else self.Contribute().__dict__()}

        def to_xml(self):
            return f"""<lifeCycle>
                {'' if isinstance(self.contribute, str) else self.contribute.to_xml() if self.contribute is not None else ''}
            </lifeCycle>"""

    class MetaMetadata:

        identifier = None
        contribute = None
        metadataSchema = None
        language = None

        def __init__(self, identifier=None, contribute=None, metadataSchema=None, language=None):
            self.identifier = identifier
            self.contribute = contribute
            self.metadataSchema = metadataSchema
            self.language = language

        class Identifier:
            catalog = []
            entry = []
            
            def __init__(self, catalog=[], entry=[]):
                self.catalog=catalog
                self.entry=entry
            
            def addValues(self,atributes):
                self.catalog=atributes.get('lomes:catalog')
                self.entry=atributes.get('lomes:entry')


            def to_xml(self):
                return f"""<identifier>
                <catalog>{self.catalog}</catalog>
                <entry>{self.entry}</entry>
                </identifier>"""

            def __dict__(self):
                return {'Catalog': self.catalog, 'Entry': self.entry}
        
        class Metadataschema:

            value = []

            def __init__(self, value=[]):
                self.value = value
            
            def addValues(self,atributes):
                self.value=atributes.get('lomes:metadataSchema')


            def to_xml(self):
                return f"""<metadataSchema>{self.value}</metadataSchema>"""

            def __dict__(self):
                return {'Values': self.value}
        
        class Language:
            value = []

            def __init__(self, value=[]):
                self.value = value
            
            def addValues(self,atributes):
                self.value=atributes.get('lomes:language')


            def to_xml(self):
                return f"""<language>{self.value}</language>"""

            def __dict__(self):
                return {'Values': self.value}


        class Contribute:
            role = None
            entity = None
            date = None

            def __init__(self, role='', entity='', date=''):
                self.role = role
                self.entity = entity
                self.date = date

            def to_xml(self):
                return f"""<contribute>
                <role>
                <source>LOMv1.0</source>
                <value>{self.role}</value>
                </role>
                <entity>
                <![CDATA[{self.entity}]]>
                </entity>
                <date>
                <dateTime>{self.date}</dateTime>
                <description>
                <string language="en">EMPTY</string>
                </description>
                </date>
                </contribute>"""

            def __dict__(self):
                return {'Role': self.role, 'Entity': self.entity, 'Date': self.date}

        def to_xml(self):
            return f"""<metaMetadata>
            {'' if isinstance(self.identifier, str) else self.identifier.to_xml() if self.identifier is not None else ''}
            {'' if isinstance(self.metadataSchema, str) else self.metadataSchema.to_xml() if self.metadataSchema is not None else ''}
            {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
            </metaMetadata>"""

        def __dict__(self):
            return {
                'Identifier': self.identifier.__dict__() if self.identifier is not None else self.Identifier().__dict__(),
                'MetadataSchema': self.metadataSchema.__dict__() if self.metadataSchema is not None else self.Metadataschema().__dict__(),
                'Language': self.language.__dict__() if self.language is not None else self.Language().__dict__()}

    class Technical:
        format = None
        size = None,
        location = None
        requirement = None
        installationRemarks = None
        other_platform_requirements = None
        duration = None

        def __init__(self, technical_format='', size='', location='', requirement=None, installationRemarks='',
                     other_platform_requirements='', duration=''):
            self.format = technical_format
            self.size = size,
            self.location = location
            self.requirement = requirement
            self.installationRemarks = installationRemarks
            self.other_platform_requirements = other_platform_requirements
            self.duration = duration
        
        class Location:
            value = []

            def __init__(self, value=[]):
                self.value = value
            
            def addValues(self,atributes):
                self.value=atributes.get('lomes:location')


            def to_xml(self):
                return f"""<location>{self.value}</location>"""

            def __dict__(self):
                return {'Values': self.value}
        
        class Installationremarks:
            language = []

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')


            def to_xml(self):
                return f"""<installationRemarks>
                <string  language="{self.language}"></string>
                </installationRemarks>"""

            def __dict__(self):
                return {'Language': self.language}

        class Requirement:
            or_composite = None

            def __init__(self, or_composite=None):
                self.or_composite = or_composite

            class OrComposite:
                composite_type = None
                name = None
                minimum_version = None
                maximum_version = None

                def __init__(self, composite_type='', name='', minimum_version='', maximum_version=''):
                    self.composite_type = composite_type
                    self.name = name
                    self.minimum_version = minimum_version
                    self.maximum_version = maximum_version

                def to_xml(self):
                    return f"""<orComposite>
                    <type>
                    <source>LOMv1.0</source>
                    <value>{self.composite_type}</value>
                    </type>
                    <name>
                    <source>LOMv1.0></source>
                    <value>{self.name}</value>
                    </name>
                    <minimumVersion>{self.minimum_version}</minimumVersion>
                    <maximumVersion>{self.maximum_version}</maximumVersion>
                    </orComposite>"""

                def __dict__(self):
                    return {'Type': self.composite_type, 'Name': self.name, 'Minimum Version': self.minimum_version,
                            'Maximum Version': self.maximum_version}

            def to_xml(self):
                return f"""<requirement>
                {self.or_composite.to_xml() if self.or_composite is not None else ''}
                </requirement>"""

            def __dict__(self):
                return {
                    'OrComposite': self.or_composite.__dict__() if self.or_composite is not None
                    else self.OrComposite().__dict__()}

        def to_xml(self):
            return f"""<technical>
            {'' if isinstance(self.location, str) else self.location.to_xml() if self.location is not None else ''}
            {'' if isinstance(self.installationRemarks, str) else self.installationRemarks.to_xml() if self.installationRemarks is not None else ''}
            </technical>"""

        def __dict__(self):
            return {'Installation Remarks': self.installationRemarks.__dict__() if self.installationRemarks is not None else self.Installationremarks().__dict__(),
                    'Location': self.location.__dict__() if self.location is not None else self.Location().__dict__()}

    class Educational:
        interactivity_type = None
        learningResourceType = None
        interactivity_level = None
        semantic_density = None
        intendedEndUserRole = None
        context = None
        typical_age_range = None
        difficulty = None
        typical_learning_time = None
        description = None
        language = None

        def __init__(self, interactivity_type='', learningResourceType='', interactivity_level='',
                     semantic_density='', intendedEndUserRole='', context='', typical_age_range='', difficulty='',
                     typical_learning_time='', description='', language=''):
            self.interactivity_type = interactivity_type
            self.learningResourceType = learningResourceType
            self.interactivity_level = interactivity_level
            self.semantic_density = semantic_density
            self.intendedEndUserRole = intendedEndUserRole
            self.context = context
            self.typical_age_range = typical_age_range
            self.difficulty = difficulty
            self.typical_learning_time = typical_learning_time
            self.description = description
            self.language = language
        
        class Learningresourcetype:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')

            def to_xml(self):
                return f"""<learningResourceType >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </learningResourceType>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Intendedenduserrole:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')

            def to_xml(self):
                return f"""<intendedEndUserRole >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </intendedEndUserRole>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Context:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')

            def to_xml(self):
                return f"""<context >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </context>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}

        class Description:
            language = []

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')


            def to_xml(self):
                return f"""<description>
                <string  language="{self.language}"></description>
                </description>"""

            def __dict__(self):
                return {'Language': self.language}
        
        class Language:
            language = []

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                self.language=atributes.get('lomes:language')


            def to_xml(self):
                return f"""<language >{self.language}</language>"""

            def __dict__(self):
                return {'Language': self.language}

        def to_xml(self):
            return f"""<educational>
            {'' if isinstance(self.learningResourceType, str) else self.learningResourceType.to_xml() if self.learningResourceType is not None else ''}
            {'' if isinstance(self.intendedEndUserRole, str) else self.intendedEndUserRole.to_xml() if self.intendedEndUserRole is not None else ''}
            {'' if isinstance(self.context, str) else self.context.to_xml() if self.context is not None else ''}
            {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
            {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
            </educational>"""

        def __dict__(self):
            return {'Interactivity Type': self.interactivity_type,
                    'Learning Resource Type': self.learningResourceType.__dict__() if self.learningResourceType is not None else self.Learningresourcetype().__dict__(),
                    'Interactivity Level': self.interactivity_level, 'Semantic Density': self.semantic_density,
                    'Intended End User Roles': self.intendedEndUserRole.__dict__() if self.intendedEndUserRole is not None else self.Intendedenduserrole().__dict__(), 
                    'Context': self.context.__dict__() if self.context is not None else self.Context().__dict__(),
                    'Typical Age Range': self.typical_age_range, 'Difficulty': self.difficulty,'Typical Learning Time': self.typical_learning_time, 
                    'Description': self.description.__dict__() if self.description is not None else self.Description().__dict__(),
                    'Language':self.language.__dict__() if self.language is not None else self.Language().__dict__()}

    class Rights:
        cost = None
        copyrightAndOtherRestrictions = None
        description = None
        access =  None

        def __init__(self, cost='', copyright_and_other_restrictions='', description='', access=None):
            self.cost = cost
            self.copyrightAndOtherRestrictions = copyright_and_other_restrictions
            self.description = description
            self.access = access
        
        class Copyrightandotherrestrictions:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')

            def to_xml(self):
                return f"""<copyrightAndOtherRestrictions >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </copyrightAndOtherRestrictions>"""
            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}

        class Access:
            source = []
            value = []
            description = []
            def __init__(self, source=[], value=[], description=[]):
                self.source = source
                self.value = value
                self.description = description
            
            def addValues(self,atributes):
                self.source=atributes.get('lomes:source')
                self.value=atributes.get('lomes:value')
                self.description=atributes.get('lomes:string')

            def to_xml(self):
                return f"""<accessType >
                    <source >{self.source}</source>
                    <value >{self.value}</value>
                </accessType>
                <description >
                    <string >{self.description}</string>
                </description>"""
            
            def __dict__(self):
                return {'Source': self.source, 'Value': self.value, 'Description':self.description}

        def to_xml(self):
            return f"""<rights>
            {'' if isinstance(self.copyrightAndOtherRestrictions, str) else self.copyrightAndOtherRestrictions.to_xml() if self.copyrightAndOtherRestrictions is not None else ''}
            {'' if isinstance(self.access, str) else self.access.to_xml() if self.access is not None else ''}
            </rights>"""

        def __dict__(self):
            return {'Copyrightandotherrestrictions': self.copyrightAndOtherRestrictions.__dict__() if self.copyrightAndOtherRestrictions is not None else self.Copyrightandotherrestrictions().__dict__(),
                    'Access': self.access.__dict__() if self.access is not None else self.Access().__dict__()}

    class Relation:
        kind = None
        resource = None

        def __init__(self, kind='', resource=None):
            self.kind = kind
            self.resource = resource

        class Resource:
            description = None
            identifier = None

            def __init__(self, identifier=None, description=''):
                self.description = description
                self.identifier = identifier

            class Identifier:
                catalog = None
                entry = None

                def __init__(self, catalog='', entry=''):
                    self.catalog = catalog
                    self.entry = entry

                def __dict__(self):
                    return {'Catalog': self.catalog, 'Entry': self.entry}

                def to_xml(self):
                    return f"""<identifier>
                    <catalog>{self.catalog}</catalog>
                    <entry>{self.entry}</entry>
                    </identifier>"""

            def to_xml(self):
                return f"""<resource>
                {self.identifier.to_xml() if self.identifier is not None else ''}
                <description>
                <string language="en">{self.description}</string>
                </description>
                </resource>"""

            def __dict__(self):
                return {'Identifier': self.identifier.__dict__() if self.identifier is not None
                else self.Identifier().__dict__(),
                        'Description': self.description}

        def to_xml(self):
            return f"""<relation>
            <kind>
            <source>LOMv1.0</source>
            <value>{self.kind}</value>
            </kind>
            {self.resource.to_xml() if self.resource is not None else ''}
            </relation>"""

        def __dict__(self):
            return {'Kind': self.kind, 'Resource': self.resource.__dict__() if self.resource is not None
            else self.Resource().__dict__()}

    class Annotation:
        entity = None
        date = None
        description = None
        mode_access = None
        mode_access_sufficient = None
        rol = None

        def __init__(self, entity='', date='', description='', mode_access='', mode_access_sufficient='', rol=''):
            self.entity = entity
            self.date = date
            self.description = description
            self.mode_access = mode_access
            self.mode_access_sufficient = mode_access_sufficient
            self.rol = rol

        def to_xml(self):
            return f"""<annotation>
            <entity>
            <![CDATA[{self.entity}]]>
            </entity>
            <date>
            <dateTime>{self.date}</dateTime>
            <description>
            <string></string>
            </description>
            </date>
            <description>
            <string>{self.description}</string>
            </description>
            <modeaccess>
            <source>LOMv1.0</source>
            <value>{self.mode_access}</value>
            </modeaccess>
            <modeaccesssufficient>
            <source>LOMv1.0</source>
            <value>{self.mode_access_sufficient}</value>
            </modeaccesssufficient>
            <Rol>
            <source>LOMv1.0</source>
            <value>{self.rol}</value>
            </Rol>
            </annotation>"""

        def __dict__(self):
            return {'Entity': self.entity, 'Date': self.date, 'Description': self.description,
                    'Mode Access': self.mode_access, 'Mode Access Sufficient': self.mode_access_sufficient,
                    'Rol': self.rol}

    class Classification:
        purpose = None  # purpose
        taxon_path = None  # taxon_path
        description = None  # description
        keywordd = None  # keywordd

        def __init__(self, purpose='', taxon_path=None, description='', keywordd=''):
            self.purpose = purpose
            self.taxon_path = taxon_path
            self.description = description
            self.keywordd = keywordd

        class TaxonPath:
            source = None
            taxon = None

            def __init__(self, source='', taxon=None):
                self.source = source
                self.taxon = taxon

            class Taxon:
                taxon_id = None
                entry = None

                def __init__(self, taxon_id='', entry=''):
                    self.taxon_id = taxon_id
                    self.entry = entry

                def __dict__(self):
                    return {'Id': self.taxon_id, 'Entry': self.entry}

                def to_xml(self):
                    return f"""<taxon>
                    <id>{self.taxon_id}</id>
                    <entry>
                    <string language="en">{self.entry}</string>
                    </entry>
                    </taxon>"""

            def to_xml(self):
                return f"""<taxonPath>
                <source>
                <string language="en">{self.source}</string>
                </source>
                {self.taxon.to_xml() if self.taxon is not None else ''}
                </taxonPath>"""

            def __dict__(self):
                return {'Source': self.source, 'Taxon': self.taxon.__dict__() if self.taxon is not None
                else self.Taxon().__dict__()}

        def to_xml(self):
            return f"""<classification>
            <purpose>
            <source>LOMv1.0</source>
            <value>{self.purpose}</value>
            </purpose>
            {self.taxon_path.to_xml() if self.taxon_path is not None else ''}
            <description>
            <string language="en">{self.description}</string>
            </description>
            <keyword>
            <string language="en">{self.keywordd}</string>
            </keyword>
            </classification>"""

        def __dict__(self):
            return {'Purpose': self.purpose, 'Taxon Path': self.taxon_path.__dict__() if self.taxon_path is not None
            else self.TaxonPath().__dict__(), 'Description': self.description, 'Keyword': self.keywordd}

    class Accessibility:

        description = None
        accessibility_features = None
        accessibility_hazard = None
        accessibility_control = None
        accessibility_api = None

        def __init__(self, description='', accesibility_features=None, accessibility_hazard=None,
                     accessibility_control=None, accessibility_api=None):
            self.description = description
            self.accessibility_features = accesibility_features
            self.accessibility_hazard = accessibility_hazard
            self.accessibility_control = accessibility_control
            self.accessibility_api = accessibility_api

        class AccessibilityFeatures:
            resource_content = None

            def __init__(self, resource_content=''):
                self.resource_content = resource_content

            def __dict__(self):
                return {'Resource Content': self.resource_content}

            def get_resource_content(self):
                content = ""
                if type(self.resource_content) is OrderedDict and type(self.resource_content.get('br')) is list:
                    for resource in self.resource_content.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.resource_content.get('br')

            def to_xml(self):
                return f"""<accessibilityfeatures>
                <resourcecontent>
                {self.get_resource_content()}
                </resourcecontent>
                </accessibilityfeatures>"""

        class AccessibilityHazard:
            properties = None

            def __init__(self, properties=''):
                self.properties = properties

            def __dict__(self):
                return {'Properties': self.properties}

            def get_properties(self):
                content = ""
                if type(self.properties) is OrderedDict and type(self.properties.get('lomes:br')) is list:
                    for resource in self.properties.get('lomes:br'):
                        content += f"<lomes:br>{resource}</lomes:br>\n"
                    return content
                else:
                    return self.properties.get('lomes:br')

            def to_xml(self):
                return f"""<accessibilityhazard>
                <properties>
                {self.get_properties()}
                </properties>
                </accessibilityhazard>"""

        class AccessibilityControl:
            methods = None

            def __init__(self, methods=''):
                self.methods = methods

            def __dict__(self):
                return {'Methods': self.methods}

            def get_methods(self):
                content = ""
                if type(self.methods) is OrderedDict and type(self.methods.get('br')) is list:
                    for resource in self.methods.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.methods.get('br')

            def to_xml(self):
                return f"""<accessibilitycontrol>
                <methods>
                {self.get_methods()}
                </methods>
                </accessibilitycontrol>"""

        class AccessibilityAPI:
            compatible_resource = None

            def __init__(self, compatible_resource=''):
                self.compatible_resource = compatible_resource

            def __dict__(self):
                return {'Compatible Resource': self.compatible_resource}

            def get_compatible_resources(self):
                content = ""
                if type(self.compatible_resource) is OrderedDict and type(self.compatible_resource.get('br')) is list:
                    for resource in self.compatible_resource.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.compatible_resource.get('br')

            def to_xml(self):
                return f"""<accessibilityAPI>
                <compatibleresource>
                {self.get_compatible_resources()}
                </compatibleresource>
                </accessibilityAPI>"""

        def to_xml(self):
            return f"""<accesibility>
            <description><string language="en">{self.description}</string></description>
            {self.accessibility_features.to_xml() if self.accessibility_features is not None else ''}
            {self.accessibility_hazard.to_xml() if self.accessibility_hazard is not None else ''}
            {self.accessibility_control.to_xml() if self.accessibility_control is not None else ''}
            {self.accessibility_api.to_xml() if self.accessibility_api is not None else ''}
            </accesibility>"""

        def __dict__(self):
            return {'Description': self.description, 'Accessibility Features': self.accessibility_features.__dict__()
                    if self.accessibility_features is not None else self.AccessibilityFeatures().__dict__(),
                    'Accessibility Hazard': self.accessibility_hazard.__dict__() if self.accessibility_hazard is not None
                    else self.AccessibilityHazard().__dict__(),
                    'Accessibility Control': self.accessibility_control.__dict__() if self.accessibility_control is not None
                    else self.AccessibilityControl().__dict__(),
                    'Accessibility API': self.accessibility_api.__dict__() if self.accessibility_api is not None
                    else self.AccessibilityAPI().__dict__()}

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
                try:
                    metodo = dispatch[key1]
                    ejemplo =  metodo(dict(dictionary), is_lompad_exported)
                    return ejemplo
                except:
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
    if data is not None and not isinstance(data, list):
        attributes = object_instance.__dir__()
        
        print("===============================================================")
        # print(attributes)
        # print(object_instance)
        hijo=None
        values_labels=[]
        values_labels_dict={}
        # print(data)
        try:
            for key in data:
                # print("padre: ", key)
                key_mapping=key.replace('lomes:', '')
                # print(key_mapping)
                if key_mapping == "keyword":
                    key_mapping="keywordd"
                key_mapping_Upper=key_mapping.capitalize()
                if isinstance(data[key], str):
                    # print("hijo1: ", data[key])
                    if data[key] is None:
                        data[key]="None"
                    if key not in values_labels_dict.keys():
                        values_labels_dict[key]=[data[key]]
                    else:
                        values_labels_dict.get(key).append(data[key])
                    values_labels.append(data[key])
                else:
                    for childrens in data[key]:
                        # print("hijo: ",childrens)
                        if isinstance(childrens, str):
                            containerOfFather=data[key]
                            for val in containerOfFather:
                                # print("nieto: ", containerOfFather[val])
                                containerOfChildren=containerOfFather[val]
                                if isinstance(containerOfChildren, collections.OrderedDict):
                                    for val2 in containerOfChildren:
                                        # print("objeto de objeto: ", containerOfChildren[val2])
                                        if containerOfChildren[val2] is None:
                                            containerOfChildren[val2]="None"
                                        elif val2 not in values_labels_dict.keys():
                                            values_labels_dict[val2]=[containerOfChildren[val2]]
                                        else:
                                            values_labels_dict.get(val2).append(containerOfChildren[val2])
                                            values_labels.append(containerOfChildren[val2])
                                else:
                                    # print("data key con object: ", containerOfChildren)
                                    if containerOfChildren is None:
                                            containerOfChildren="None"
                                    elif val not in values_labels_dict.keys():
                                        values_labels_dict[val]=[containerOfChildren]
                                        values_labels.append(containerOfChildren)
                                    else:
                                        values_labels_dict.get(val).append(containerOfChildren)
                                        values_labels.append(containerOfChildren)
                            break
                        else:
                            for val_children in childrens:
                                # print("val childrens: ", childrens[val_children])
                                if isinstance(childrens[val_children],str):
                                    if childrens[val_children] is None:
                                            childrens[val_children]="None"
                                    if val_children not in values_labels_dict.keys():
                                        values_labels_dict[val_children]=[childrens[val_children]]
                                    else:
                                        values_labels_dict.get(val_children).append(childrens[val_children])
                                    values_labels.append(childrens[val_children])
                                elif childrens[val_children] is None:
                                    if childrens[val_children] is None:
                                            childrens[val_children]="None"
                                    if val_children not in values_labels_dict.keys():
                                        values_labels_dict[val_children]=[childrens[val_children]]
                                    else:
                                        values_labels_dict.get(val_children).append(childrens[val_children])
                                    values_labels.append(childrens[val_children])
                                else:
                                    containerOfChildren=childrens[val_children]
                                    if isinstance(containerOfChildren, collections.OrderedDict):
                                        for val2 in containerOfChildren:
                                            if containerOfChildren[val2] is None:
                                                containerOfChildren[val2]="None"
                                            if isinstance(containerOfChildren[val2], collections.OrderedDict):
                                                container_container=containerOfChildren[val2]
                                                for val3 in container_container:
                                                    # print("val val val children: ", container_container[val3])
                                                    if val3 not in values_labels_dict.keys():
                                                        values_labels_dict[val3]=[container_container[val3]]
                                                    else:
                                                        values_labels_dict.get(val3).append(container_container[val3])
                                                    values_labels.append(container_container[val3])
                                            else:
                                                # print("val val  childrens: ", containerOfChildren[val2])
                                                if val2 not in values_labels_dict.keys():
                                                    values_labels_dict[val2]=[containerOfChildren[val2]]
                                                else:
                                                    values_labels_dict.get(val2).append(containerOfChildren[val2])
                                                values_labels.append(containerOfChildren[val2])
                # print(values_labels)
                print(values_labels_dict)
                children_label=object_instance.__getattribute__(key_mapping_Upper)()
                children_label.addValues(values_labels_dict)
                # children_label.getValues()
                values_labels=[]   
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
    general_object = map_attributes(data, LOM.General(), is_lom)
    # if 'lomes:identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('lomes:identifier'), LOM.General.Identifier(), is_lom)
    # elif 'identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('identifier'), LOM.General.Identifier(), is_lom)

    return general_object.__dict__(), general_object


def life_cycle_leaf(data: dict, is_lom):
    """
        Function to map Life Cycle Leaf.

        :param data: data from manifest.
        :return: a LifeCycle class instance.
        """
    general_object = map_attributes(data, LOM.LifeCycle(), is_lom)
    # if 'lomes:identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('lomes:identifier'), LOM.General.Identifier(), is_lom)
    # elif 'identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('identifier'), LOM.General.Identifier(), is_lom)

    return general_object.__dict__(), general_object


def meta_metadata_leaf(data: dict, is_lom):
    """
        Function to map Meta MetaData Leaf.

        :param data: data from manifest.
        :return: a MetaMetaData class instance.
        """
    general_object = map_attributes(data, LOM.MetaMetadata(), is_lom)
    # if 'lomes:identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('lomes:identifier'), LOM.General.Identifier(), is_lom)
    # elif 'identifier' in data.keys():
    #     general_object.identifier = map_attributes(data.get('identifier'), LOM.General.Identifier(), is_lom)

    return general_object.__dict__(), general_object

    # meta_metadata_object = map_attributes(data, LOM.MetaMetadata(), is_lom)
    # meta_metadata_object.identifier = map_attributes(data.get('lomes:identifier') if data.get('lomes:identifier')
    #                                                  is not None else data,
    #                                                  LOM.MetaMetadata.Identifier(), is_lom)
    # meta_metadata_object.contribute = map_attributes(data.get('lomes:contribute')
    #                                                  if data.get('lomes:contribute') is not None
    #                                                  else data, LOM.MetaMetadata.Contribute(), is_lom)

    # return meta_metadata_object.__dict__(), meta_metadata_object


def technical_leaf(data: dict, is_lom):
    """
        Function to map Technical Leaf.

        :param data: data from manifest.
        :return: a Technical class instance.
        """
    technical_object = map_attributes(data, LOM.Technical(), is_lom)
    # orComposite = None
    # if 'lomes:requirement' in data.keys() and 'lomes:OrComposite' in data.get('lomes:requirement').keys():
    #     orComposite = map_attributes(data.get('lomes:requirement').get('lomes:OrComposite'), LOM.Technical.Requirement
    #                                  .OrComposite(), is_lom)
    # elif 'requirement' in data.keys():
    #     if data.get('requirement') is not None and 'orComposite' in data.get('requirement').keys():
    #         orComposite = map_attributes(data.get('requirement').get('orComposite'),
    #                                  LOM.Technical.Requirement.OrComposite(), is_lom)
    #     elif data.get('requirement') is not None and 'OrComposite' in data.get('requirement').keys():
    #         orComposite = map_attributes(data.get('requirement').get('OrComposite'),
    #                                  LOM.Technical.Requirement.OrComposite(), is_lom)
    # technical_object.requirement = technical_object.Requirement(orComposite)

    return technical_object.__dict__(), technical_object


def educational_leaf(data: dict, is_lom):
    """
        Function to map Educational Leaf.

        :param data: data from manifest.
        :return: a Educational class instance.
        """
    educational_object = map_attributes(data, LOM.Educational(), is_lom)

    return educational_object.__dict__(), educational_object


def rights_leaf(data: dict, is_lom):
    """
        Function to map Rights Leaf.

        :param data: data from manifest.
        :return: a Rights class instance.
        """
    rights_object = map_attributes(data, LOM.Rights(), is_lom)

    return rights_object.__dict__(), rights_object


def relation_leaf(data: dict, is_lom):
    """
        Function to map Relation Leaf.

        :param data: data from manifest.
        :return: a Relation class instance.
        """
    relation_object = map_attributes(data, LOM.Relation(), is_lom)
    resource = map_attributes(data['resource'], LOM.Relation.Resource(), is_lom)

    if 'resource' in data.keys():
        if 'identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['identifier'], LOM.Relation.Resource.Identifier(), is_lom)
        elif 'Identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['Identifier'], LOM.Relation.Resource.Identifier(), is_lom)

    resource.identifier = identifier
    relation_object.resource = resource

    return relation_object.__dict__(), relation_object


def annotation_leaf(data: dict, is_lom):
    """
        Function to map Annotation Leaf.

        :param data: data from manifest.
        :return: a Annotation class instance.
        """
    annotation_object = map_attributes(data, LOM.Annotation(), is_lom)

    return annotation_object.__dict__(), annotation_object


def classification_leaf(data: dict, is_lom):
    """
        Function to map Classification Leaf.

        :param data: data from manifest.
        :return: a Classification class instance.
        """
    classification_object = map_attributes(data, LOM.Classification(), is_lom)

    taxon_path = map_attributes(data.get('lomes:taxonPath') if data.get('lomes:taxonPath') is not None else
                                data.get('taxonPath'), classification_object.TaxonPath(), is_lom)

    taxon = None
    if data.get('lomes:taxonPath') is not None and data.get('lomes:taxonPath').get('lomes:taxon') is not None:
        taxon = map_attributes(data.get('lomes:taxonPath').get('lomes:taxon')[0]
                               if type(data.get('lomes:taxonPath').get('lomes:taxon')) is list else
                               data.get('lomes:taxonPath').get('lomes:taxon'), classification_object.TaxonPath.Taxon(),
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
    accessibility_object = map_attributes(data, LOM.Accessibility(), is_lom)
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
    'lomes:general': general_leaf, 'lomes:lifeCycle': life_cycle_leaf, 'lomes:metaMetadata': meta_metadata_leaf,
    'lomes:technical': technical_leaf, 'lomes:educational': educational_leaf,
    'lomes:rights': rights_leaf, 'lomes:relation': relation_leaf, 'lomes:annotation': annotation_leaf,
    'lomes:classification': classification_leaf, 'accesibility': accessibility_leaf
}

dispatch_update = {
    'lomes:general': general_leaf, 'lomes:lifeCycle': life_cycle_leaf, 'lomes:metaMetadata': meta_metadata_leaf,
    'lomes:technical': technical_leaf, 'lomes:educational': educational_leaf,
    'lomes:rights': rights_leaf, 'lomes:relation': relation_leaf, 'lomes:annotation': annotation_leaf,
    'lomes:classification': classification_leaf, 'accesibility': accessibility_leaf
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
