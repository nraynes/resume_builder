from typing import Any, Type


class BaseModel:
    def extract(self, object: dict, key: str, alternative: Any, constructor: Type = None) -> Any:
        """Extracts a value from a dictionary if it exists. Otherwise, returns an alternative.

        Args:
            object (dict): The dictionary object to choose from.
            key (str): The key to use when extracting a value from the dictionary.
            alternative (Any): The alternative value to use if that key does not exist in the dictionary.
            constructor: (Type): A constructor to supply the dictionary value to as an 
            argument instead of returning the value itself. 

        Returns:
            Any: Either the dictionary value or the alternative value if the dictionary value could not be retreived.
        """
        try:
            return object[key] if constructor is None else constructor(object[key])
        except KeyError:
            return alternative
