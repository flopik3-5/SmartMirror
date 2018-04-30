
class ConfigField:
    def __init__(self, name, value, configFieldType, availableValues, configFields):
        self.name = name
        self.value = value
        self.configFieldType = configFieldType
        self.availableValues = availableValues
        self.configFields = configFields
