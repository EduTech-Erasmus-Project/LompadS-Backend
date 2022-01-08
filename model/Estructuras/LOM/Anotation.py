class Annotation:
        entity = None
        date = None
        description = None
        mode_access = None
        mode_access_sufficient = None
        rol = None

        def __init__(self, entity=None, date=None, description=None, mode_access=None, mode_access_sufficient=None, rol=None):
            self.entity = entity
            self.date = date
            self.description = description
            self.mode_access = mode_access
            self.mode_access_sufficient = mode_access_sufficient
            self.rol = rol
        
        class Entity:
            entity=[]

            def __init__(self, entity=[]):
                self.entity = entity
            
            def addValues(self,atributes):
                self.entity=atributes.get("entity")
                    
            def getValues(self):
                print("Entity: ", self.entity)

            def to_xml(self):
                return f"""<entity>{self.entity}</entity>"""

            def __dict__(self):
                return {'Entity': self.entity}

        class Date:

            dateTime=[]
            string=[]

            def __init__(self, dateTime=[], string=[]):
                self.dateTime = dateTime
                self.string = string
            
            def addValues(self,atributes):
                self.dateTime=atributes.get("dateTime")
                self.string=atributes.get("string")
                    

            def to_xml(self):
                return f"""<date>
                                <dateTime>{self.dateTime}</dateTime>
                                <description>
                                    <string>{self.string}</string>
                                </description>
                            </date>"""

            def __dict__(self):
                return {'DateTime': self.dateTime, 'Description': self.string}
        
        class Description:
            Description=[]

            def __init__(self, description=[]):
                self.description = description
            
            def addValues(self,atributes):
                self.description=atributes.get("string")
                    
            def getValues(self):
                print("Description: ", self.description)

            def to_xml(self):
                return f"""<description>
                                <string>{self.description}</string>
                            </description>"""

            def __dict__(self):
                return {'Description': self.description}
        
        class Modeaccess:

            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get("source")
                self.value=atributes.get("value")
                    

            def to_xml(self):
                return f"""<modeaccess>
                                <source>{self.source}</source>
                                <value>{self.value}</value>
                            </modeaccess>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Modeaccesssufficient:

            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get("source")
                self.value=atributes.get("value")
                    

            def to_xml(self):
                return f"""<modeaccesssufficient>
                                <source>{self.source}</source>
                                <value>{self.value}</value>
                            </modeaccesssufficient>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}
        
        class Rol:

            source=[]
            value=[]

            def __init__(self, source=[], value=[]):
                self.source = source
                self.value = value
            
            def addValues(self,atributes):
                self.source=atributes.get("source")
                self.value=atributes.get("value")
                    

            def to_xml(self):
                return f"""<Rol>
                                <source>{self.source}</source>
                                <value>{self.value}</value>
                            </Rol>"""

            def __dict__(self):
                return {'Source': self.source, 'Value': self.value}

        def to_xml(self):
            return f"""<annotation>
            {'' if isinstance(self.entity, str) else self.entity.to_xml() if self.entity is not None else ''}
            {'' if isinstance(self.date, str) else self.date.to_xml() if self.date is not None else ''}
            {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
            {'' if isinstance(self.mode_access, str) else self.mode_access.to_xml() if self.mode_access is not None else ''}
            {'' if isinstance(self.mode_access_sufficient, str) else self.mode_access_sufficient.to_xml() if self.mode_access_sufficient is not None else ''}
            {'' if isinstance(self.rol, str) else self.rol.to_xml() if self.rol is not None else ''}
            </annotation>"""

        def __dict__(self):
            return {'Entity': self.entity.__dict__() if self.entity is not None else [], 
                    'Date': self.date.__dict__() if self.date is not None else [], 
                    'Description': self.description.__dict__() if self.description is not None else [],
                    'Mode Access': self.mode_access.__dict__() if self.mode_access is not None else [],
                    'Mode Access Sufficient': self.mode_access_sufficient.__dict__() if self.mode_access_sufficient is not None else [],
                    'Rol': self.rol.__dict__() if self.rol is not None else []}