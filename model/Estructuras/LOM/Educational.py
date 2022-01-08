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

        def __init__(self, interactivity_type=None, learningResourceType=None, interactivity_level=None,
                     semantic_density=None, intendedEndUserRole=None, context=None, typical_age_range=None, difficulty=None,
                     typical_learning_time=None, description=None, language=None):
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
                self.source=atributes.get('source')
                self.value=atributes.get('value')

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
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<intendedEndUserRole >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </intendedEndUserRole>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Interactivitylevel:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<interactivityLevel>
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </interactivityLevel>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Semanticdensity:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<semanticDensity>
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </semanticDensity>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Context:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<context>
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </context>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Difficulty:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<Difficulty>
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </Difficulty>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Typicallearningtime:
            duration = []
            string = []

            def __init__(self, duration=[], string=[]):
                self.duration = duration
                self.string = string
            
            def addValues(self,atributes):
                self.source=atributes.get('duration')
                self.value=atributes.get('string')

            def to_xml(self):
                return f"""<typicalLearningTime>
                                <duration>{self.duration}</duration>
                                <description>
                                    <string>{self.string}</string>
                                </description>
                            </typicalLearningTime>"""

            def __dict__(self):
                return {'Duration': self.source, 'Description': self.value}

        class Description:
            description = []

            def __init__(self, description=[]):
                self.description = description
            
            def addValues(self,atributes):
                self.description=atributes.get('string')
                if self.description is None:
                    self.description=atributes.get('#text')
            def to_xml(self):
                return f"""<description>
                <string>{self.description}</description>
                </description>"""

            def __dict__(self):
                return {'Description': self.description}
        
        class Typicalagerange:
            string = []

            def __init__(self, string=[]):
                self.string = string
            
            def addValues(self,atributes):
                self.string=atributes.get('string')


            def to_xml(self):
                return f"""<typicalAgeRange>
                                <string>{self.string}</string>
                            </typicalAgeRange>"""

            def __dict__(self):
                return {'typicalAgeRange': self.string}
        
        class Language:
            language = []

            def __init__(self, language=[]):
                self.language = language
            
            def addValues(self,atributes):
                self.language=atributes.get('language')


            def to_xml(self):
                return f"""<language >{self.language}</language>"""

            def __dict__(self):
                return {'Language': self.language}
        
        class Interactivitytype:
            source = []
            value = []

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get('source')
                self.value=atributes.get('value')

            def to_xml(self):
                return f"""<interactivityType >
                                <source >{self.source}</source>
                                <value >{self.value}</value>
                            </interactivityType>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}

        def to_xml(self):
            return f"""<educational>
            {'' if isinstance(self.interactivity_type, str) else self.interactivity_type.to_xml() if self.interactivity_type is not None else ''}
            {'' if isinstance(self.learningResourceType, str) else self.learningResourceType.to_xml() if self.learningResourceType is not None else ''}
            {'' if isinstance(self.interactivity_level, str) else self.interactivity_level.to_xml() if self.interactivity_level is not None else ''}
            {'' if isinstance(self.semantic_density, str) else self.semantic_density.to_xml() if self.semantic_density is not None else ''}
            {'' if isinstance(self.intendedEndUserRole, str) else self.intendedEndUserRole.to_xml() if self.intendedEndUserRole is not None else ''}
            {'' if isinstance(self.context, str) else self.context.to_xml() if self.context is not None else ''}
            {'' if isinstance(self.typical_age_range, str) else self.typical_age_range.to_xml() if self.typical_age_range is not None else ''}
            {'' if isinstance(self.difficulty, str) else self.difficulty.to_xml() if self.difficulty is not None else ''}
            {'' if isinstance(self.typical_learning_time, str) else self.typical_learning_time.to_xml() if self.typical_learning_time is not None else ''}
            {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
            {'' if isinstance(self.language, str) else self.language.to_xml() if self.language is not None else ''}
            </educational>"""

        def __dict__(self):
            return {'Interactivity Type': self.interactivity_type.__dict__() if self.interactivity_type is not None else [],
                    'Learning Resource Type': self.learningResourceType.__dict__() if self.learningResourceType is not None else [],
                    'Interactivity Level': self.interactivity_level.__dict__() if self.interactivity_level is not None else [],
                    'Intended End UserRole': self.intendedEndUserRole.__dict__() if self.intendedEndUserRole is not None else [],
                    'Semantic Density': self.semantic_density.__dict__() if self.semantic_density is not None else [],
                    'Context': self.context.__dict__() if self.context is not None else [],
                    'Difficulty': self.difficulty.__dict__() if self.difficulty is not None else [],
                    'Description': self.description.__dict__() if self.description is not None else [],
                    'Typical Age Range': self.typical_age_range.__dict__() if self.typical_age_range is not None else [],
                    'Typical Learning Time': self.typical_learning_time.__dict__() if self.typical_learning_time is not None else [],
                    'Language': self.language.__dict__() if self.language is not None else []}