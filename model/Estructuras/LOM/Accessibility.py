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

        class Accessibilityfeatures:
            br=[]

            def __init__(self, br=[]):
                self.br = br
            
            def addValues(self,atributes):
                self.br=atributes.get("br")[0]

            def to_xml(self):
                return f"""<accessibilityfeatures>
                                <resourcecontent>
                                    <br>{self.br}</br>
                                </resourcecontent>
                            </accessibilityfeatures>"""

            def __dict__(self):
                return {'Accessibilityfeatures': self.br}
        
        class Accessibilityhazard:
            br=[]

            def __init__(self, br=[]):
                self.br = br
            
            def addValues(self,atributes):
                self.br=atributes.get("br")[0]

            def to_xml(self):
                return f"""<accessibilityhazard>
                                <properties>
                                    <br>{self.br}</br>
                                </properties>
                            </accessibilityhazard>"""

            def __dict__(self):
                return {'Accessibilityhazard': self.br}

        class Accessibilitycontrol:
            br=[]

            def __init__(self, br=[]):
                self.br = br
            
            def addValues(self,atributes):
                self.br=atributes.get("br")[0]

            def to_xml(self):
                return f"""<accessibilitycontrol>
                                <methods>
                                    <br>{self.br}</br>
                                </methods>
                            </accessibilitycontrol>"""

            def __dict__(self):
                return {'Accessibilitycontrol': self.br}
        
        class Accessibilityapi:
            br=[]

            def __init__(self, br=[]):
                self.br = br
            
            def addValues(self,atributes):
                self.br=atributes.get("br")[0]

            def to_xml(self):
                return f"""<accessibilityAPI>
                                <compatibleresource>
                                    <br>{self.br}</br>
                                </compatibleresource>
                            </accessibilityAPI>"""

            def __dict__(self):
                return {'Accessibilityapi': self.br}

        def to_xml(self):
            return f"""<accesibility>
            {'' if isinstance(self.description, str) else self.description.to_xml() if self.description is not None else ''}
            {'' if isinstance(self.accessibility_features, str) else self.accessibility_features.to_xml() if self.accessibility_features is not None else ''}
            {'' if isinstance(self.accessibility_hazard, str) else self.accessibility_hazard.to_xml() if self.accessibility_hazard is not None else ''}
            {'' if isinstance(self.accessibility_control, str) else self.accessibility_control.to_xml() if self.accessibility_control is not None else ''}
            {'' if isinstance(self.accessibility_api, str) else self.accessibility_api.to_xml() if self.accessibility_api is not None else ''}
            </accesibility>"""

        def __dict__(self):
            return {'Description': self.description.__dict__() if self.description is not None else [],
                    'Accessibility Features': self.accessibility_features.__dict__() if self.accessibility_features is not None else [], 
                    'Accessibility Hazard': self.accessibility_hazard.__dict__() if self.accessibility_hazard is not None else [], 
                    'Accessibility Control': self.accessibility_control.__dict__() if self.accessibility_control is not None else [], 
                    'Accessibility API': self.accessibility_api.__dict__() if self.accessibility_api is not None else []}