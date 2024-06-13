import tomllib
from pathlib import Path

from brainvision_recording.controller import BrainvisionManager


# This is a bit different from other dareplane modules, as we do not need
# a continously running process/thread but simply fire off calls to the
# BV vbs scripts, or start the LSL recorder

cfg = tomllib.load(open('./configs/bv_conf.toml', 'rb'))

# Define a controller instance here and use it


def init_bvm(
    vbs_path: Path = Path(cfg['bv_script_path']),
    bv_recording_path: Path = Path(cfg['bv_recording_path']),
) -> BrainvisionManager:
    return BrainvisionManager(rec_dir=bv_recording_path,
                              vbs_root_path=vbs_path)
