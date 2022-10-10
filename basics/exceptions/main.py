""" Exception handling """

import log


class AppException(Exception):
    pass


logger = log.get_logger(__name__, log.get_file_handler())
movies = ["Interstellar", "Inception", "Source Code", "Loki"]


def sample_func():
    try:
        return movies[3]
    except IndexError as err:
        logger.exception(f"IndexError occurred - movies has only {len(movies) - 1} indices")
        raise AppException(err) from err


# sample_func()
def handler():
    try:
        res =  sample_func()
    except AppException:
        logger.exception(f"AppException occured")
    else:
        logger.info("Successfull!")
        return res


def main():
    movie = handler()
    print(f"Sci-fi movie: {movie}")


if __name__ == '__main__':
    main()
