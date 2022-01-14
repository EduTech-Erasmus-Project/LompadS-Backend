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
                self.catalog=atributes.get('catalog')
                if self.catalog is None:
                    self.catalog=atributes.get('lomes:catalog')

                self.entry=atributes.get('entry')
                if self.entry is None:
                    self.entry=atributes.get('lomes:entry')


            def to_xml(self):
                return f"""<identifier>
                <catalog>{self.catalog}</catalog>
                <entry>{self.entry}</entry>
                </identifier>"""

            def __dict__(self):
                return {'catalog': self.catalog, 'entry': self.entry}
        
        class Metadataschema:

            value = []

            def __init__(self, value=[]):
                self.value = value
            
            def addValues(self,atributes):
                self.value=atributes.get('metadataSchema')
                if self.value is None:
                    self.value=atributes.get('lomes:metadataSchema')

            def to_xml(self):
                return f"""<metadataSchema>{self.value}</metadataSchema>"""

            def __dict__(self):
                return {'metadataSchema': self.value}
        
        class Language:
            value = []

            def __init__(self, value=[]):
                self.value = value
            
            def addValues(self,atributes):
                self.value=atributes.get('language')
                if self.value is None:
                    self.value=atributes.get('lomes:language')

            def to_xml(self):
                return f"""<language>{self.value}</language>"""

            def __dict__(self):
                return {'language': self.value}


        class Contribute:
            source=[]
            value=[]
            entity=[]
            dateTime=[]
            description=[]

            def __init__(self, source=[], value=[], entity=[], dateTime=[], description=[]):
                self.source = source
                self.value = value
                self.entity = entity
                self.dateTime = dateTime
                self.description = description
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')
                self.entity=atributes.get('entity')
                self.dateTime=atributes.get('dateTime')
                self.description=atributes.get('description')

            def to_xml(self):
                return f"""<contribute>
                <role>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </role>
                <entity>{self.entity}
                </entity>
                <date>
                <dateTime>{self.dateTime}</dateTime>
                <description>
                <string>{self.description}</string>
                </description>
                </date>
                </contribute>"""

            def __dict__(self):
                return {'source': self.source, 'value': self.value, 'entity': self.entity, 
                'date': self.dateTime, 'description':self.description}

        def to_xml(self):
            return f"""<metaMetadata>
            {'' if isinstance(self.identifier, str) else self.identifier.to_xml() if self.identifier is not None else ''}
            {'' if isinstance(self.metadataSchema, str) else self.metadataSchema.to_xml() if self.metadataSchema is not None else ''}
            {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
            {'' if isinstance(self.contribute, str) else self.contribute.to_xml() if self.contribute is not None else ''}
            </metaMetadata>"""

        def __dict__(self):
            return {
                'identifier': self.identifier.__dict__() if self.identifier is not None else {'catalog': [], 'entry': []},
                'metadataSchema': self.metadataSchema.__dict__() if self.metadataSchema is not None else {'metadataSchema': []},
                'language': self.language.__dict__() if self.language is not None else {'language': []},
                'contribute': self.contribute.__dict__() if self.contribute is not None else {'source': [], 'value': [], 'entity': [], 'date': [], 'description':[]}}