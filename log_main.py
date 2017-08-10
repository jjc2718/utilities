import os
import sys
import logging
import traceback

def log_main(main_function):
    """ Decorates a main function to provide informative logging.

    Mostly useful for jobs that run for a long time and don't always write
    error messages to a useful location, e.g. long-running jobs on a remote
    server.

    """
    def wrapper():

        logging.basicConfig(filename='log.txt', level=20,
                            format="%(asctime)s\n%(message)s")

        # get name of file for redirection, and write whole command to log
        # this is a bit of a hack and might not work on all systems,
        # tread carefully
        stdout_filename = os.readlink('/proc/self/fd/1')
        command = '{} > {}'.format(' '.join(sys.argv), stdout_filename)

        try:
            main_function()
        except Exception:
            logging.error('{}\n{}'.format(command, traceback.format_exc()))
            sys.exit(traceback.format_exc())

        # if no exception was thrown, write confirmation to the log
        logging.info('{}\n{}\n'.format(command, 'Completed successfully'))

    return wrapper

if __name__ == '__main__':
    log_main()

