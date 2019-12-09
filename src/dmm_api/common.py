"""Commons."""

from typing import Any, List


def to_str(val: Any) -> str:
    """To string.

    Args:
        val (Any): Value

    Returns:
        str: String.
    """
    return '' if val is None else val if isinstance(val, str) else str(val)


def dict_to_list(d: dict, rule: dict) -> List[str]:
    """Convert dict to list.

    Args:
        d (dict): Input dict.
        rule (dict): Rule.

    Returns:
        list: Result.
    """
    result = []
    for name, (keys, pattern) in rule.items():
        if keys == []:
            value = d.get(name)
        else:
            value = get_dict_value(d, keys)

        if pattern['name'] == 'str':
            result.append(to_str(value))
        elif pattern['name'] == 'dict_list':
            if value is None:
                v_l: List[str] = []
            else:
                v_l = [
                    to_str(get_dict_value(v, pattern['value'])) for v in value
                ]
            result.append('[' + ','.join(v_l) + ']')
    return result


def get_dict_value(d: dict, keys: list) -> Any:
    """Get dict value with keys.

    Args:
        d (dict): Dict.
        keys (list): Keys.

    Raises:
        KeyError

    Returns:
        Any: Result.
    """
    for k in keys:
        # Raise KeyError.
        d2 = d[k]

        if d2 is None:
            break
        else:
            d = d2
    return d
