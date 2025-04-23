from dareplane_utils.default_server.server import DefaultServer
from fire import Fire

from brainvision_recording.main import init_bvm
from brainvision_recording.utils.logging import logger


def main(port: int = 8080, ip: str = "127.0.0.1", loglevel: int = 10):
    logger.setLevel(loglevel)
    bvm = init_bvm()
    pcommand_map = {
        "SET_SAVE_PATH": bvm.set_rec_dir,
        "START_SAVE": bvm.start_recording,
        "STOP_SAVE": bvm.stop_recording,
    }

    server = DefaultServer(
        port, ip=ip, pcommand_map=pcommand_map, name="bv_command_server"
    )

    # initialize to start the socket
    server.init_server()
    # start processing of the server
    server.start_listening()

    return 0


if __name__ == "__main__":
    Fire(main)
