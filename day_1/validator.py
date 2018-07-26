"""

Module provides checking if sent string
can be filled with the specified dict

"""
import faker
import random
import string


def get_context():
    """

    Creates dict of data, for tests
    Returns:
        dict:

    """
    f = faker.Faker()
    return {
        'id': random.randint(0, 100),
        'name': f.name(),
        'email': f.email(),
        'job': f.job(),
        'country': f.country(),
        'age': random.randint(0, 100)
    }


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
    str_filled = False
    context = string.Template(template.replace("{", "${"))
    try:
        str_filled = context.substitute(dict_data)
    except KeyError as e:
        KeyError("Following key not found: {}".format(e))

    except BaseException as e:
        print(e.args)
    finally:
        return str_filled


def main():
    data = get_context()
    print(check_validation("{name}, {age}, {job}, {a}, {c}", data))


if __name__ == '__main__':
    main()


