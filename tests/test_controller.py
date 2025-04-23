from pathlib import Path

import pytest

from tests.resources.tcontroller import DummyManager

# Note: The tests do only check against a DummyManager, which only validates
#       that commands are sent to the correct path, not actually triggering the
#       vbs scripts. This is done so that the module can also be developed under
#       UNIX.


def test_start_recording(tmp_path):
    bvm = DummyManager(rec_dir=tmp_path, vbs_root_path=Path("./vsbs/"))

    bvm.start_recording("test_block_1")
    eeg_files = list(tmp_path.glob("*.eeg"))
    assert len(eeg_files) == 1

    # no overwrite, so a new file should be created
    bvm.start_recording("test_block_1")
    eeg_files2 = list(tmp_path.glob("*.eeg"))
    assert len(eeg_files2) == 2

    # with overwrite, so no new file should be created
    bvm.start_recording("test_block_1", overwrite=True)
    eeg_files3 = list(tmp_path.glob("*.eeg"))
    assert len(eeg_files3) == 2


def test_other_vbs_calls(tmp_path):
    bvm = DummyManager(rec_dir=tmp_path, vbs_root_path=Path("./vsbs/"))
    ret = bvm.stop_recording()
    assert ret.stem.endswith("bvr_stoprecording")
    ret = bvm.view_signals()
    assert ret.stem.endswith("bvr_viewsignals")
