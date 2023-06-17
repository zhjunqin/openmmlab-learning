# openmmlab-learning

Task4: https://github.com/open-mmlab/OpenMMLabCamp/issues/145

## pspnet

```
2023/06/17 10:35:59 - mmengine - INFO - Iter(val) [11/11]    aAcc: 87.4300  mIoU: 50.4000  mAcc: 55.4800  data_time: 0.0040  time: 0.1462
2023/06/17 10:36:22 - mmengine - INFO - Iter(train) [2500/3000]  lr: 9.4416e-03  eta: 0:01:52  time: 0.2249  data_time: 0.0040  memory: 3777  loss: 0.0417  decode.loss_ce: 0.0292  decode.acc_seg: 84.9457  aux.loss_ce: 0.0125  aux.acc_seg: 84.4452
2023/06/17 10:36:44 - mmengine - INFO - Iter(train) [2600/3000]  lr: 9.4191e-03  eta: 0:01:30  time: 0.2247  data_time: 0.0040  memory: 3777  loss: 0.0407  decode.loss_ce: 0.0283  decode.acc_seg: 87.7258  aux.loss_ce: 0.0123  aux.acc_seg: 87.5732
2023/06/17 10:37:07 - mmengine - INFO - Iter(train) [2700/3000]  lr: 9.3967e-03  eta: 0:01:07  time: 0.2249  data_time: 0.0042  memory: 3777  loss: 0.0319  decode.loss_ce: 0.0231  decode.acc_seg: 84.6832  aux.loss_ce: 0.0088  aux.acc_seg: 85.3485
2023/06/17 10:37:29 - mmengine - INFO - Iter(train) [2800/3000]  lr: 9.3743e-03  eta: 0:00:45  time: 0.2245  data_time: 0.0040  memory: 3777  loss: 0.0331  decode.loss_ce: 0.0226  decode.acc_seg: 74.3011  aux.loss_ce: 0.0104  aux.acc_seg: 75.1617
2023/06/17 10:37:31 - mmengine - INFO - per class results:
2023/06/17 10:37:31 - mmengine - INFO -
+------------+-------+-------+
|   Class    |  IoU  |  Acc  |
+------------+-------+-------+
| backgroud  | 87.76 | 97.51 |
|    red     |  84.5 |  88.7 |
|   green    | 51.71 | 57.37 |
|   white    | 73.59 | 79.12 |
| seed-black | 58.53 |  65.1 |
| seed-white |  1.61 |  1.61 |
+------------+-------+-------+
2023/06/17 10:37:31 - mmengine - INFO - Iter(val) [11/11]    aAcc: 90.8000  mIoU: 59.6200  mAcc: 64.9000  data_time: 0.0041  time: 0.1467
2023/06/17 10:37:53 - mmengine - INFO - Iter(train) [2900/3000]  lr: 9.3518e-03  eta: 0:00:22  time: 0.2249  data_time: 0.0041  memory: 3777  loss: 0.0444  decode.loss_ce: 0.0318  decode.acc_seg: 77.3621  aux.loss_ce: 0.0126  aux.acc_seg: 77.6886
2023/06/17 10:38:16 - mmengine - INFO - Exp name: pspnet-watermelon2_20230617_102640
2023/06/17 10:38:16 - mmengine - INFO - Iter(train) [3000/3000]  lr: 9.3294e-03  eta: 0:00:00  time: 0.2249  data_time: 0.0040  memory: 3777  loss: 0.0371  decode.loss_ce: 0.0268  decode.acc_seg: 91.1163  aux.loss_ce: 0.0103  aux.acc_seg: 93.8477
2023/06/17 10:38:16 - mmengine - INFO - Saving checkpoint at 3000 iterations
```

## segformer Train

```
2023/06/17 12:07:48 - mmengine - INFO - Iter(train) [3550/5000]  lr: 5.9224e-05  eta: 0:03:18  time: 0.1347  data_time: 0.0031  memory: 2760  loss: 0.1023  decode.loss_ce: 0.1023  decode.acc_seg: 98.7438
2023/06/17 12:07:54 - mmengine - INFO - Iter(train) [3600/5000]  lr: 5.9205e-05  eta: 0:03:11  time: 0.1346  data_time: 0.0031  memory: 2760  loss: 0.0965  decode.loss_ce: 0.0965  decode.acc_seg: 96.8376
2023/06/17 12:08:01 - mmengine - INFO - Iter(train) [3650/5000]  lr: 5.9186e-05  eta: 0:03:04  time: 0.1348  data_time: 0.0029  memory: 2759  loss: 0.0502  decode.loss_ce: 0.0502  decode.acc_seg: 98.0926
2023/06/17 12:08:08 - mmengine - INFO - Iter(train) [3700/5000]  lr: 5.9168e-05  eta: 0:02:58  time: 0.1345  data_time: 0.0030  memory: 2760  loss: 0.0748  decode.loss_ce: 0.0748  decode.acc_seg: 95.4870
2023/06/17 12:08:14 - mmengine - INFO - Iter(train) [3750/5000]  lr: 5.9149e-05  eta: 0:02:51  time: 0.1344  data_time: 0.0030  memory: 2758  loss: 0.0780  decode.loss_ce: 0.0780  decode.acc_seg: 97.4797
2023/06/17 12:08:21 - mmengine - INFO - Iter(train) [3800/5000]  lr: 5.9130e-05  eta: 0:02:44  time: 0.1344  data_time: 0.0031  memory: 2760  loss: 0.0678  decode.loss_ce: 0.0678  decode.acc_seg: 98.7201
2023/06/17 12:08:28 - mmengine - INFO - Iter(train) [3850/5000]  lr: 5.9111e-05  eta: 0:02:37  time: 0.1344  data_time: 0.0030  memory: 2759  loss: 0.0814  decode.loss_ce: 0.0814  decode.acc_seg: 94.5114
2023/06/17 12:08:35 - mmengine - INFO - Iter(train) [3900/5000]  lr: 5.9092e-05  eta: 0:02:30  time: 0.1345  data_time: 0.0031  memory: 2760  loss: 0.0646  decode.loss_ce: 0.0646  decode.acc_seg: 96.7533
2023/06/17 12:08:41 - mmengine - INFO - Iter(train) [3950/5000]  lr: 5.9073e-05  eta: 0:02:23  time: 0.1345  data_time: 0.0031  memory: 2760  loss: 0.0873  decode.loss_ce: 0.0873  decode.acc_seg: 93.3670
2023/06/17 12:08:48 - mmengine - INFO - Exp name: segformer-watermelo_20230617_02_20230617_115929
2023/06/17 12:08:48 - mmengine - INFO - Iter(train) [4000/5000]  lr: 5.9054e-05  eta: 0:02:16  time: 0.1344  data_time: 0.0031  memory: 2760  loss: 0.0808  decode.loss_ce: 0.0808  decode.acc_seg: 98.4899
2023/06/17 12:08:48 - mmengine - INFO - Saving checkpoint at 4000 iterations
2023/06/17 12:08:49 - mmengine - INFO - per class results:
2023/06/17 12:08:49 - mmengine - INFO -
+------------+-------+-------+
|   Class    |  IoU  |  Acc  |
+------------+-------+-------+
| backgroud  | 96.55 | 97.54 |
|    red     | 93.98 | 98.76 |
|   green    | 87.35 | 94.24 |
|   white    | 78.87 | 85.89 |
| seed-black | 65.82 | 90.48 |
| seed-white | 23.94 | 24.61 |
+------------+-------+-------+
2023/06/17 12:08:49 - mmengine - INFO - Iter(val) [11/11]    aAcc: 96.6700  mIoU: 74.4200  mAcc: 81.9200  data_time: 0.0038  time: 0.0732
2023/06/17 12:08:49 - mmengine - INFO - The previous best checkpoint /data/github/openmmlab/mmsegmentation/work_dirs/segformer/best_mIoU_iter_3500.pth is removed
2023/06/17 12:08:50 - mmengine - INFO - The best checkpoint with 74.4200 mIoU at 4000 iter is saved to best_mIoU_iter_4000.pth.
```

## segformer

```
06/17 12:12:27 - mmengine - INFO - Load checkpoint from work_dirs/segformer/best_mIoU_iter_4000.pth
06/17 12:12:30 - mmengine - INFO - per class results:
06/17 12:12:30 - mmengine - INFO -
+------------+-------+-------+
|   Class    |  IoU  |  Acc  |
+------------+-------+-------+
| backgroud  | 96.55 | 97.54 |
|    red     | 93.98 | 98.76 |
|   green    | 87.35 | 94.23 |
|   white    | 78.87 | 85.89 |
| seed-black | 65.82 | 90.48 |
| seed-white | 23.94 | 24.61 |
+------------+-------+-------+
06/17 12:12:30 - mmengine - INFO - Iter(test) [11/11]    aAcc: 96.6700  mIoU: 74.4200  mAcc: 81.9200  data_time: 0.0137  time: 0.2430

```

## segformer test

```
python demo/image_demo.py Watermelon87_Semantic_Seg_Mask/Watermelon_test.jpg segformer-watermelo.py work_dirs/segformer/best_mIoU_iter_4000.pth --device cuda:0 --out-file watermelon_result.jpg
```

![](./Watermelon_test.jpg)
![](./watermelon_result.jpg)
