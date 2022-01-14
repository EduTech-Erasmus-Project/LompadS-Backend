class Classification:
        purpose = None  # purpose
        taxonPath = None  # taxon_path
        description = None  # description
        keywordd = None  # keywordd

        def __init__(self, purpose=None, taxonPath=None, description=None, keywordd=None):
            self.purpose = purpose
            self.taxonPath = taxonPath
            self.description = description
            self.keywordd = keywordd
        
        class Purpose:

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
                    

            def to_xml(self):
                return f"""<purpose>
                                <source>{self.source}</source>
                                <value>{self.value}</value>
                            </purpose>"""

            def __dict__(self):
                return {'source': self.source, 'value': self.value}
                
        class Taxonpath:
            string = []
            id = []
            entry = []
            def __init__(self, string=[], id=[], entry=[]):
                self.string = string
                self.id = id
                self.entry = entry
            
            def addValues(self,atributes):
                self.string=atributes.get('string')
                if self.string is None:
                    self.string=[atributes.get('#text')[0]]
                self.id=atributes.get('id')
                if self.id is None:
                    self.id=atributes.get('lomes:id')
                self.entry=atributes.get('entry')
                if self.entry is None:
                    self.entry=atributes.get('#text')[1:]

            def to_xml(self):
                return f"""<taxonPath>
                                <source>
                                    <string>{self.string}</string>
                                </source>
                                <taxon>
                                    <id>{self.id}</id>
                                    <entry>
                                        <string>{self.entry}</string>
                                    </entry>
                                </taxon>
                            </taxonPath>"""
            
            def __dict__(self):
                return {'source': self.string, 'id': self.id, 'entry':self.entry}
        
        class Description:
            string = []

            def __init__(self, string=[]):
                self.string = string
            
            def addValues(self,atributes):
                self.string=atributes.get('string')

            def to_xml(self):
                return f"""<description>
                                <string>{self.string}</string>
                            </description>"""
            def __dict__(self):
                return {'description': self.string}

        class Keywordd:

            language=[]
            keywordd=[]

            def __init__(self, language=[], keywordd=[]):
                self.language = language
                self.keywordd = keywordd
            
            def addValues(self,atributes):
                self.language=atributes.get('@language')
                self.keywordd=atributes.get('string')

            def getValues(self):
                print("Languaje: ", self.language)
                print("Keyword: ", self.keywordd)

            def to_xml(self):
                return f"""<string  language="{self.language}">{self.keywordd}</string>"""

            def __dict__(self):
                return {'language': self.language, 'keyword': self.keywordd}


        def to_xml(self):
            return f"""<classification>
            {'' if isinstance(self.purpose, str) else self.purpose.to_xml() if self.purpose is not None else ''}
            {'' if isinstance(self.taxonPath, str) else self.taxonPath.to_xml() if self.taxonPath is not None else ''}
            {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
            {'' if isinstance(self.keywordd, str) else self.keywordd.to_xml() if self.keywordd is not None else ''}
            </classification>"""

        def __dict__(self):
            return {'purpose': self.purpose.__dict__() if self.purpose is not None else {'source': [], 'value': []}, 
                    'taxonPath': self.taxonPath.__dict__() if self.taxonPath is not None else {'source': [], 'id': [], 'entry':[]}, 
                    'description': self.description.__dict__() if self.description is not None else {'description': []}, 
                    'keyword': self.keywordd.__dict__() if self.keywordd is not None else {'language': [], 'keyword': []}}