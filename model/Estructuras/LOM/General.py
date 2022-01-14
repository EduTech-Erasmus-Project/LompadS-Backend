class General:
        identifier = None
        title = None
        catalogentry = None
        language = None
        description = None
        keywordd = None
        coverage = None
        structure = None
        aggregation_level = None

        def __init__(self, identifier=None, title=None, language=None, description=None, keywordd=None, coverage=None,
                     structure=None, aggregation_level=None, catalogentry=None):
            self.identifier = identifier
            self.title = title
            self.catalogentry = catalogentry
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
                self.catalog=atributes.get('catalog')
                if self.catalog is None:
                    self.catalog=atributes.get('lomes:catalog')

                self.entry=atributes.get('entry')
                if self.entry is None:
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
                return {'catalog': self.catalog, 'entry': self.entry}

        class Title:
            language=[]
            title=[]

            def __init__(self, language=[], title=[]):
                self.language = language
                self.title = title
            
            def addValues(self,atributes):
                # for val in atributes.keys():
                #     self.title=atributes.get(val)
                #     self.language.append(val)
                self.title=atributes.get("#text")
                if self.title is None:
                    self.title=atributes.get("string")
                self.language=atributes.get("@language")
                    
            def getValues(self):
                print("Languaje: ", self.language)
                print("Title: ", self.title)

            def to_xml(self):
                return f"""<title>
                <string language="{self.language}">{self.title}</string>
                </title>"""

            def __dict__(self):
                return {'language': self.language, 'title': self.title}
        
        class Catalogentry:
            catalog=[]

            def __init__(self, catalog=[], title=[]):
                self.catalog = catalog
                self.title = title
            
            def addValues(self,atributes):
                self.catalog=atributes.get("catalog")
                    
            def getValues(self):
                print("Catalog: ", self.catalog)

            def to_xml(self):
                return f"""<catalogentry>
                <langstring>{self.catalog}</string>
                </catalogentry>"""

            def __dict__(self):
                return {'Catalog': self.catalog}
        
        class Language:
            language=[]

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                self.language=atributes.get('language')
                if self.language is None:
                    self.language=atributes.get('lomes:language')        
                    
            def getValues(self):
                print("Language: ", self.language)
            

            def to_xml(self):
                return f"""<language>{self.language}</language>"""

            def __dict__(self):
                return {'language': self.language}
        
        class Description:

            languageDescription=[]
            description=[]

            def __init__(self, languageDescription=[], description=[]):
                self.languageDescription = languageDescription
                self.description = description
            
            def addValues(self,atributes):
                self.description=atributes.get("#text")
                if self.description is None:
                    self.description=atributes.get("string")
                self.languageDescription=atributes.get("@language")
                    
            def getValues(self):
                print("Languaje: ", self.languageDescription)
                print("Description: ", self.description)

            def to_xml(self):
                return f"""<description>
                <string language="{self.languageDescription}">{self.description}</string>
                </description>"""

            def __dict__(self):
                return {'language': self.languageDescription, 'description': self.description}
        
        class Keywordd:

            languageKeyword=[]
            keywordd=[]

            def __init__(self, languageKeyword=[], keywordd=[]):
                self.languageKeyword = languageKeyword
                self.keywordd = keywordd
            
            def addValues(self,atributes):
                self.languageKeyword=atributes.get('@language')
                self.keywordd=atributes.get('string')
                if self.keywordd is None:
                    self.keywordd=atributes.get('#text')

            def getValues(self):
                print("Languaje: ", self.languageKeyword)
                print("Keyword: ", self.keywordd)

            def to_xml(self):
                return f"""<string  language="{self.languageKeyword}">{self.keywordd}</string>"""

            def __dict__(self):
                return {'language': self.languageKeyword, 'keyword': self.keywordd}
        
        
        class Coverage:

            language=[]
            coverage=[]

            def __init__(self, language=[], coverage=[]):
                self.language = language
                self.coverage = coverage
            
            def addValues(self,atributes):
                self.coverage=atributes.get("string")
                    
            def getValues(self):
                print("Language: ", self.language)
                print("Coverage: ", self.coverage)

            def to_xml(self):
                return f"""<coverage>
                <string language="{self.language}">{self.coverage}</string>
                </coverage>"""

            def __dict__(self):
                return {'language': self.language, 'coverage': self.coverage}
        
        class Structure:
            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get("source")
                self.value=atributes.get("value")
                    
            def getValues(self):
                print("Source: ", self.language)
                print("Value: ", self.coverage)

            def to_xml(self):
                return f""" <structure>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </structure>"""

            def __dict__(self):
                return {'source': self.source, 'value': self.value}
        
        class Aggregationlevel:

            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                if self.source is None:
                    self.source=atributes.get('lomes:source')
                
                self.value=atributes.get('value')
                if self.value is None:
                    self.value=atributes.get('lomes:value')
                    
            def getValues(self):
                print("Source: ", self.source)
                print("Value: ", self.value)

            def to_xml(self):
                return f"""<aggregationLevel>
                <source>{self.source}</source>
                <value>{self.value}</value>
                </aggregationLevel>"""

            def __dict__(self):
                return {'source': self.source, 'value': self.value}

        def to_xml(self):
            return f"""<general>
                {'' if isinstance(self.identifier, str) else self.identifier.to_xml() if self.identifier is not None else ''}
                {'' if isinstance(self.title, str) else self.title.to_xml() if self.title is not None else ''}
                {'' if isinstance(self.catalogentry, str) else self.catalogentry.to_xml() if self.catalogentry is not None else ''}
                {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
                {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
                {'' if isinstance(self.keywordd, str) else self.keywordd.to_xml() if self.keywordd is not None else ''}
                {'' if isinstance(self.coverage, str) else self.coverage.to_xml() if self.coverage is not None else ''}
                {'' if isinstance(self.structure, str) else self.structure.to_xml() if self.structure is not None else ''}
                {'' if isinstance(self.aggregation_level, str) else self.aggregation_level.to_xml() if self.aggregation_level is not None else ''}
            </general>"""

        def __dict__(self):
            return {'identifier': self.identifier.__dict__() if self.identifier is not None else  {'catalog': [], 'entry': []},
                    'title': self.title.__dict__() if self.title is not None else {'language': [], 'title': []}, 
                    'language': self.language.__dict__() if self.language is not None else {'language': []},
                    'description': self.description.__dict__() if self.description is not None else {'language': [], 'description': []},
                    'keyword': self.keywordd.__dict__() if self.keywordd is not None else {'language': [], 'keyword': []},
                    'coverage': self.coverage.__dict__() if self.coverage is not None else {'language': [], 'coverage': []},
                    'structure': self.structure.__dict__() if self.structure is not None else {'source': [], 'value': []},
                    'aggregationLevel': self.aggregation_level.__dict__() if self.aggregation_level is not None else {'source': [], 'value': []}}