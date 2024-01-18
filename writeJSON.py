import json

nnUNet_dir = 'D:/developProject/nnUNet/DATASET/' #此路径根据自己实际修改

def sts_json():
    info = {
        "channel_names": {
            "0": "CBCT"
        },
        "labels": {
            "background": 0,
            "Teeth": 1
        },
        "numTraining": 12,
        "file_ending": ".nii.gz"
    }
    with open(nnUNet_dir + 'nnUNet_raw/Dataset001_Teeth/dataset.json',
              'w') as f:
        json.dump(info, f, indent=4)

sts_json()
