# UNet implementation and application on self labelled images and synthese images 

UNet for Multiclass Semantic Segmentation, on Keras, based on Segmentation Models' Unet libray

## Requirements

You must have Python 3 and an NVIDIA GPU with CUDA 10 support, by means of the pip tool you can install the packages using the following command on the repository folder:

```code
pip install -r requirements.txt
```

Some important libraries:

* keras >= 2.2.0 or tensorflow >= 1.13
* albumentations==0.3.0
* segmentation-models==1.0.*

**Install Segmentation Models**

```code
 pip install git+https://github.com/qubvel/segmentation_models
```

## Project Structure
    .
    ├──augmentation.py: Module with functions for image sets augmentation.
    ├──data_loader.py: Module with the class for the manipulation of the image sets
    ├──expe_real.ipynb: 2 expe for the model train on real images
    ├──expe_synthese.ipynb: 2 expe for the model train on syntheses images.
    ├──utils.py: Module with auxiliary functions.
    └──requirements.txt: File containing a list of the libraries required to run all the modules.

## How to Use

A call must be made to the main module, passing it the arguments corresponding to the dataset paths and the training parameters.

### Dataset

the data used are little satellites images of 512*512 pixels from the Hautes Alpes french department 
The data for "the synthese dataset" has been created from the same dataset.

