import logging
import os
from atm.utils import checks

ROOT = os.path.dirname(__file__)

CONFIG_FILEPATH = os.path.join(ROOT, 'configs/script_configs.yaml')
DEFAULT_LOGDIR = os.path.join(ROOT, 'logs')

def init_logger(filename):
    logging.basicConfig(
        filename=filename,
        filemode='a',
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )


if __name__ == "__main__":
    checks.check_dir_existance(DEFAULT_LOGDIR)
    init_logger(f"{DEFAULT_LOGDIR}/atm.log")

    if checks.check_file_exitstance([CONFIG_FILEPATH], req_sts=True):
        from atm import pose_pred
        pose_pred.main(CONFIG_FILEPATH, ROOT)