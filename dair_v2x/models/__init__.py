import sys
import os
import os.path as osp

root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(root)
sys.path.extend([os.path.join(path, name) for path, dirs, _ in os.walk(root) for name in dirs])

from detection_models import *

SUPPROTED_MODELS = {
    "single_side": SingleSide,
    "late_fusion": LateFusion,
    "early_fusion": EarlyFusion,
    "veh_only": VehOnly,
    "inf_only": InfOnly,
    "feature_fusion":FeatureFusion,
    "feature_flow":FeatureFlow
}
