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