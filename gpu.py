import os

def count_gpus():
    devs = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    if len(devs) == 0 or devs == "NoDevFiles":
        return 0
    return len(devs.split(","))
