import time
from pathlib import Path

from brainvision_recording.controller import BrainvisionManager
from brainvision_recording.utils.logging import logger


class DummyManager(BrainvisionManager):

    def _run_vbs_cmd(self, script_name: str, params: None | list = []) -> Path:
        script_path = self.vbs_root_path.joinpath(script_name)
        logger.debug(f"vbs script called at: {script_path}")
        return script_path

    def start_recording(self, rec_name: str, overwrite: bool = False):

        self.rec_dir.mkdir(parents=True, exist_ok=True)

        fname = self.rec_dir.joinpath(f"{rec_name}.eeg")
        if fname.exists() and not overwrite:
            # find latest suffix and add next
            fname = fname.parent.joinpath(
                fname.stem + "_" + time.strftime("%Y%m%d%H%M%S") + fname.suffix
            )

        # Dummy write here
        with open(fname, "w") as fh:
            fh.write(">> " + time.strftime("%Y%m%d%H%M%S"))

        return self._run_vbs_cmd("bvr_startrecording.vbs", [str(fname)])
