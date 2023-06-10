# openmmlab-learning

## Train

```
06/10 10:40:58 - mmengine - INFO - Epoch(val) [45][28/28]    accuracy/top1: 91.5541  accuracy/top3: 97.2973  data_time: 0.0050  time: 0.0355
06/10 10:41:07 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:07 - mmengine - INFO - Epoch(train) [46][100/109]  lr: 1.0000e-03  eta: 0:00:40  time: 0.0897  data_time: 0.0010  memory: 875  loss: 0.0907
06/10 10:41:08 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:08 - mmengine - INFO - Saving checkpoint at 46 epochs
06/10 10:41:10 - mmengine - INFO - Epoch(val) [46][28/28]    accuracy/top1: 91.5541  accuracy/top3: 97.0721  data_time: 0.0058  time: 0.0387
06/10 10:41:19 - mmengine - INFO - Epoch(train) [47][100/109]  lr: 1.0000e-03  eta: 0:00:30  time: 0.0894  data_time: 0.0008  memory: 875  loss: 0.0751
06/10 10:41:20 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:20 - mmengine - INFO - Saving checkpoint at 47 epochs
06/10 10:41:22 - mmengine - INFO - Epoch(val) [47][28/28]    accuracy/top1: 91.1036  accuracy/top3: 97.4099  data_time: 0.0046  time: 0.0367
06/10 10:41:31 - mmengine - INFO - Epoch(train) [48][100/109]  lr: 1.0000e-03  eta: 0:00:20  time: 0.0892  data_time: 0.0007  memory: 875  loss: 0.0920
06/10 10:41:32 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:32 - mmengine - INFO - Saving checkpoint at 48 epochs
06/10 10:41:34 - mmengine - INFO - Epoch(val) [48][28/28]    accuracy/top1: 91.2162  accuracy/top3: 97.1847  data_time: 0.0068  time: 0.0343
06/10 10:41:43 - mmengine - INFO - Epoch(train) [49][100/109]  lr: 1.0000e-03  eta: 0:00:10  time: 0.0896  data_time: 0.0007  memory: 875  loss: 0.0731
06/10 10:41:44 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:44 - mmengine - INFO - Saving checkpoint at 49 epochs
06/10 10:41:46 - mmengine - INFO - Epoch(val) [49][28/28]    accuracy/top1: 90.9910  accuracy/top3: 97.4099  data_time: 0.0056  time: 0.0332
06/10 10:41:55 - mmengine - INFO - Epoch(train) [50][100/109]  lr: 1.0000e-03  eta: 0:00:00  time: 0.0896  data_time: 0.0008  memory: 875  loss: 0.0617
06/10 10:41:56 - mmengine - INFO - Exp name: resnet18_finetune_20230610_103144
06/10 10:41:56 - mmengine - INFO - Saving checkpoint at 50 epochs
06/10 10:41:58 - mmengine - INFO - Epoch(val) [50][28/28]    accuracy/top1: 90.9910  accuracy/top3: 97.5225  data_time: 0.0051  time: 0.0327
Training finished successfully.
```


## Inference


```
>>> from mmpretrain import ImageClassificationInferencer
>>> inferencer = ImageClassificationInferencer("resnet18_finetune.py", pretrained="exp/epoch_50.pth")
Loads checkpoint by local backend from path: exp/epoch_50.pth
>>> inferencer("xigua_800x.jpg")
Inference ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
[{'pred_scores': array([4.6947813e-15, 3.5985428e-15, 9.0804071e-16, 1.5747855e-18,
       1.0251412e-14, 1.4207329e-16, 7.6143580e-10, 1.3467467e-14,
       3.0054865e-18, 1.9951881e-12, 5.8641248e-13, 1.7198265e-14,
       1.8697850e-16, 3.6581409e-15, 4.0129450e-17, 8.0343551e-19,
       4.0143922e-13, 8.8923655e-13, 3.6343478e-12, 5.3297155e-15,
       1.4988188e-17, 2.4724896e-19, 1.5035734e-15, 1.7425131e-15,
       2.5198936e-16, 1.0000000e+00, 9.6304571e-15, 1.0281882e-14,
       1.1742988e-15, 8.0957923e-12], dtype=float32), 'pred_label': 25, 'pred_score': 1.0, 'pred_class': 'xigua'}]
```
