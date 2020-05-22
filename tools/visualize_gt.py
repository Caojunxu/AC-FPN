#!/usr/bin/env python2

# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Script for visualizing results saved in a detections.pkl file."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import cv2
import os
import sys
import numpy as np
import json

import detectron.utils.vis as vis_utils

# OpenCL may be enabled by default in OpenCV3; disable it because it's not
# thread safe and causes unwanted GPU memory allocations.
cv2.ocl.setUseOpenCL(False)
# imgIds = [168337, 168619, 175438, 176901, 184324, 185292, 197658, 198489, 200162]
dataDir = 'detectron/datasets/data/coco'
# dataType = 'val2017'
# annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType)
images = '{}/coco_val2017/'.format(dataDir)
# coco = COCO(annFile)
gts = json.load(open("../cnet/gt.txt"))


def vis(output_dir='mask/gt'):
    for key, gt in gts.items():
        try:
            bboxes = []
            cls = []
            for ob in gt:
                cat, bbox = ob
                cls.append(cat)
                bbox[2] = bbox[0] + bbox[2]
                bbox[3] = bbox[1] + bbox[3]
                bboxes.append(bbox)
            im = cv2.imread(os.path.join(images, key))
            vis_utils.vis_one_image_gt(
                im[:, :, ::-1],
                '{}_gt'.format(key.split(".")[0]),
                os.path.join(output_dir, 'vis'),
                np.vstack(bboxes).astype(np.int),
                cls,
                box_alpha=0.8,
                show_class=True,
                ext='jpg'
            )
        except:
            continue


if __name__ == '__main__':
    vis()
