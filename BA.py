import os
import numpy as np
import Func as Fun

# Sparse-Bundle-Adjustments-with-GCPs
# This python implementation of Sparse bundle adjustment is based on the sparse Levenberg-Marquardt algorithm with Ground Control Points (GCPs).
# Bundle adjustment is used in 3D reconstruction to optimize the 3D coordinates of points and camera parameters based on image observations.

# 0 ---------------------------------User Inputs Dataset Address---------------------------------
# Define the directory containing the dataset
dir_files = os.getcwd() + '/Dataset-1'

# Define accuracy parameters and algorithm settings
sigma_img = 0.6             # Image Accuracy (standard deviation of image measurement noise)
sigma_obj = 0.15            # Object Accuracy (standard deviation of object measurement noise)
Max_iter = 100              # Maximum number of iterations for the optimization algorithm
th = 1e-9                   # Convergence criteria (threshold for stopping the optimization)

# 1 -------------------- Import Data --------------------
# Import data from the dataset directory
EOP_ref, EOP_init, IOP, TieXYZ, TieObs = Fun.Import_Data(dir_files)
# EOP_ref: Reference Exterior Orientation Parameters
# EOP_init: Initial guess for Exterior Orientation Parameters
# IOP: Interior Orientation Parameters
# TieXYZ: 3D coordinates of tie points
# TieObs: Observations of tie points in images

# 2 -------------------- Preprocess --------------------
# Preprocess the imported data for bundle adjustment
Observation_Tie, TieXYZ, camera_params = Fun.preprocess(TieXYZ, TieObs, EOP_init)
# Observation_Tie: Preprocessed observations of tie points
# camera_params: Initial camera parameters

# Import Ground Control Points (GCPs) from XML file
GCP, Observation_gcp = Fun.Control_from_xml(dir_files, Control_start_id=TieXYZ[-1, 0] + 1)
# GCP: Ground Control Points coordinates
# Observation_gcp: Observations of GCPs in images

# Compile all necessary information for bundle adjustment
Info = Fun.Bundle_information(dir_files, GCP, TieXYZ, Observation_Tie, Observation_gcp, camera_params, IOP)
# Info: Contains all the compiled information needed for bundle adjustment

# 3 -------------------- Weight Matrix --------------------
# Create a weight matrix for the observations
Weight = Fun.Weight(Info.Tie_indices, Info.Gcp_indices, sigma_img, sigma_obj)
# Weight: Matrix that defines the importance of each observation in the optimization

# 4 -------------------- Approximate Value --------------------
# Combine initial camera parameters and 3D point coordinates into a single vector
x0 = np.hstack((camera_params.ravel(), Info.points_3d.ravel()))
# x0: Initial guess for the optimization vector (camera parameters + 3D points)

# 5 -------------------- Sparse Bundle Adjustment --------------------
# Perform Sparse Bundle Adjustment using the initial guess and weight matrix
BA = Fun.SBA(x0, Weight, Info, Max_iter, th, 1, Show=True)
# BA: Result of the bundle adjustment (optimized camera parameters and 3D points)