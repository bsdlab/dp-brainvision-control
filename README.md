# Brainvision recording

This python module allows to control the BV recorder and can be integrated into the Dareplane platform.

## Config

There is just two important config to make, which is the location of the BV `*.vbs` scripts, which are invoked by python in order to control the BV application, and the path to the
`BrainVision LSL Recorder`, which needs to be started in order to start the LSL stream.

```bash
./config/bv_conf.toml

bv_script_path = '<full_path_to_BV_vbs_scripts>'
bv_recording_path = '<full_path_to_recorder_exe>'
```

## TODO

- [ ] Currently, the `BrainVision` software needs to be started manually, as I was struggling to get subprocesses to run with it as either `.exe` or via `.bat` script.
