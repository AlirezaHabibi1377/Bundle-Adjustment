# Bundle Adjustment

This repository contains a Python implementation of Bundle Adjustment (BA) based on the sparse Levenberg-Marquardt algorithm, incorporating Ground Control Points (GCPs). Bundle adjustment is crucial in 3D reconstruction tasks, optimizing the 3D coordinates of points and camera parameters from image observations.

## Introduction

In photogrammetry and computer vision, bundle adjustment is used to refine 3D coordinates of scene points and camera parameters to produce accurate 3D reconstructions. This project focuses on implementing BA with additional constraints from GCPs, enhancing the accuracy and robustness of the 3D reconstruction process.

## Features
- Sparse implementation of the Levenberg-Marquardt algorithm.
- Incorporates Ground Control Points (GCPs) for improved accuracy.
- Handles large datasets efficiently using sparse matrix operations.
- Configurable accuracy parameters and optimization settings.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AlirezaHabibi1377/Bundle-Adjustment.git
   cd Sparse-Bundle-Adjustments-with-GCPs
