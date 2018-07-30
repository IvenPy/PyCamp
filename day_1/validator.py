"""

Module provides checking if sent string
can be filled with the specified dict

"""
import faker
import string


def get_context(keys_set):
    """
    Takes a set (or any iterable object where all elements are hashable)
    of keys and return dict filled with random strings

    Returns:
        dict: key(hashable object) -> string
    """
    dict_data = {}
    f = faker.Faker()
    for x in keys_set:
        dict_data[x] = f.word()
    return dict_data


def check_validation(template, dict_data):
    """
    Check if template string can be filled with parameters from dict_data
    In case success return filled string, unless return False

    Args:
        template: string where unfilled parameters surrounded with braces {}
        dict_data: dict where keys supposed to fill template

    Returns:
        string: template with filled parameters

    """
    context = string.Template(template.replace("{", "${"))
    try:
        str_filled = context.substitute(dict_data)
        return str_filled
    except KeyError as e:
        raise KeyError("Following key not found: {}".format(e)) from e

    except BaseException as e:
        print(e.args)


def main():
    data = get_context({'name', 'age', 'job', 'a', 'c'})
    print(check_validation("{name}, {age}, {job}, {a}, {c}", data))


if __name__ == '__main__':
    main()


