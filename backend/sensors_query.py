import re

import pandas as pd

from backend import HardwareQuery


class SensorsQuery(HardwareQuery):
    """Query for the GPU.
    """

    def get_bash_command(self):
        """inherited
        """
        return "sensors"

    def get_custom_index(self) -> list:
        """Gets the index for the resulting dataframe.
        """
        return ['Adapter']

    def parse_values(self, raw_key, raw_value) -> dict:
        """Parses the value from the sensor reading.
        """
        if '(' not in raw_value:
            return {raw_key.strip(): raw_value.strip()}

        values = raw_value.split('(')
        original = values[0].strip()
        others = values[-1].replace(')', '').split(',')

        values = {raw_key: original}

        for other in others:
            key, value = other.split('=')
            values[raw_key + ' (' + key.strip() + ')'] = value.strip()

        return values

    def clean_numeric_values(self, values: dict):
        """Extracts the numeric value from the given values and appends the
        unit to the key.
        """
        cleaned_values = {}
        for key, value in values.items():
            value_is_numeric = bool(re.search(r'[-+]?\d*\.\d+|\d+', value))
            if not value_is_numeric:
                cleaned_values[key] = value
                continue
            cleaned_value = re.findall(r'[-]?\d*\.\d+|\d+', value)[0]
            cleaned_key = f"{key} [{value.split(cleaned_value)[-1].strip()}]"
            cleaned_values[cleaned_key] = cleaned_value
        return cleaned_values

    def parse_query_result(self, result) -> pd.DataFrame:
        """inherited
        """
        lines = result.splitlines()
        adapters = {}
        for line in lines:
            if not line:
                continue
            if ':' not in line:
                name = line
                adapters[name] = {'timestamp': [self.timestamp]}
                continue
            key, value = line.split(':')

            values = self.parse_values(key, value)
            cleaned_values = self.clean_numeric_values(values)
            for key, value in cleaned_values.items():
                adapters[name][key] = [value]

        dfs = {}
        for adapter, values in adapters.items():
            dfs[adapter] = pd.DataFrame(data=values)
        return dfs


if __name__ == "__main__":
    SensorsQuery().query()
