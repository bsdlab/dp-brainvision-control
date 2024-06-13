import time
import subprocess
from pathlib import Path

from brainvision_recording.utils.logging import logger


class BrainvisionManager():
    def __init__(self,
                 rec_dir: Path,
                 vbs_root_path: Path,
                 ):
        self.rec_dir = rec_dir
        self.vbs_root_path = vbs_root_path

    def set_rec_dir(self, rec_dir: str | Path) -> int:
        rec_dir = Path(rec_dir)
        if rec_dir.exists():
            self.rec_dir = rec_dir
        else:
            logger.error(f"Recording dir {rec_dir=} does not exits!")

        return 0

    def _run_vbs_cmd(self, script_name: str, params: None | list = []):
        script_path = self.vbs_root_path.joinpath(script_name)
        ret_output = subprocess.check_output(f'cscript {script_path} {params}')
        logger.debug(f'vbs call returned {ret_output}')

        return 0

    def start_recording(self, fname: str,
                        overwrite: bool = False):

        self.rec_dir.mkdir(parents=True, exist_ok=True)
        time.sleep(0.3)
        fname = self.rec_dir.joinpath(f'{fname}.eeg')
        if fname.exists() and not overwrite:
            # find latest suffix and add next
            fname = fname.parent.joinpath(
                fname.stem + '_' + time.strftime('%Y%m%d%H%M%S') + fname.suffix)

        logger.debug(f"Sending save name {fname}")

        return self._run_vbs_cmd(
            'bvr_startrecording.vbs',
            str(fname))

    def stop_recording(self):
        return self._run_vbs_cmd('bvr_stoprecording.vbs')

    def view_signals(self):
        return self._run_vbs_cmd('bvr_viewsignals.vbs')
