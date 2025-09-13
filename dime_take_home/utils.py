import re
from typing import List

def get_locations_from_text(text: str, locations_pattern: re.Pattern, locations_lookup: dict) -> List[str]:
    """
    Given a text article, return a list of location IDs mentioned in the article.
    """
    matches = locations_pattern.findall(text)
    return list(map(lambda x: locations_lookup.get(x.lower())[-1], matches))
    # TODO return set of matches? Discard info of repeated mentions of same location?