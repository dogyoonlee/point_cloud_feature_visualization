# point cloud feature visualization
**Visualization of feature activation for point cloud data.**

This code implemented for shapenet dataset.

<p align="center">
<img src='./feature_visualization_ex.png' width=600/>
</p>

## How to Use
1. Import and init the implemented class to the target network source code.
```
from tools.features_vis_save import feature_vis

self.Visualize_feature = feature_vis()
```
2. Put the xyz and feature tensors in the network and define the layer_name for save.
```
self.Visualize_feature.feature_save(xyz=li_xyz, features=li_features, layer_name=layer_name)
```

3. Visualize using **vis_shapenet.py**(Open3D tool is used) in ./visualization_tool directory.
```
python ./visualization_tool/vis_shapenet.py
```
## License
MIT License

### Citation
If you find our work useful in your research, please consider citing our repository
