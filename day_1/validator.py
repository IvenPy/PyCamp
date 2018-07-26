import faker
import random


def get_context():
    f = faker.Faker()
    return {
        'id': random.randint(0, 100),
        'name': f.name(),
        'email': f.email(),
        'job': f.job(),
        'country': f.country(),
        'age': random.randint(0, 100)
    }


def main():
    context = get_context()
    msg = input("Enter formatting message:")
    try:
        print(msg.format(**context))

    except KeyError as e:
        print("Following key not found " + e.args[0])

    except BaseException as e:
        print(e.args)


if __name__ == '__main__':
    main()
