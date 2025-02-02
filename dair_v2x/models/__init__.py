import sys
import os
import os.path as osp

from .detection_models import *

SUPPROTED_MODELS = {
    "single_side": SingleSide,
    "late_fusion": LateFusion,
    "early_fusion": EarlyFusion,
    "veh_only": VehOnly,
    "inf_only": InfOnly,
    "feature_fusion":FeatureFusion,
    "feature_flow":FeatureFlow
}
