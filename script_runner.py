import logging
from atm.utils import checks

CONFIG_FILEPATH = 'configs/script_configs.yaml'
DEFAULT_LOGDIR = 'logs'

def init_logger(filename):
    logging.basicConfig(
        filename=filename,
        filemode='a',
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )


if __name__ == "__main__":
    init_logger(f"{DEFAULT_LOGDIR}/atm.log")

    if checks.check_file_exitstance([CONFIG_FILEPATH], req_sts=True):
        from atm import pose_pred
        pose_pred.main(CONFIG_FILEPATH)