# Training a YOLOv3 With Sequential Frames: Building a Custom Object Detector from POV videos [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repo let's you train a custom image detector on the sequential frames of a video simulating the visual stimuli presented to humans using the state-of-the-art [YOLOv3](https://pjreddie.com/darknet/yolo/) computer vision algorithm. This repo works with TensorFlow 2.3 and Keras 2.4

### Pipeline Overview

To build and test your YOLO object detection algorithm follow the below steps:

 1. [Image Annotation](/Image_Annotation/)
	 - Compile csv file with the following structure:
	 "image","xmin","ymin","xmax","ymax","label"
	 "frame0000000.jpg",0,165,966,550,"car"
 2. [Training](/Training/)
 	- Download pre-trained weights
 	- Train your custom YOLO model on annotated images 
 3. [Inference](/Inference/)
 	- Detect objects in new images and videos

## Repo structure
+ [`1_Image_Annotation`](/Image_Annotation/): Formating the annotating images
+ [`2_Training`](/Training/): Scripts and instructions on training your YOLOv3 model
+ [`3_Inference`](/Inference/): Scripts and instructions on testing your trained YOLO model on new images and videos
+ [`Data`](/Data/): Input Data, Output Data, Model Weights and Results
+ [`Utils`](/Utils/): Utility scripts used by main scripts

## Getting Started

### Requisites
The only hard requirement is a running version of python 3.6 or 3.7. To install python 3.7 go to 
- [python.org/downloads](https://www.python.org/downloads/release/python-376/) 

and follow the installation instructions. Note that this repo has only been tested with python 3.6 and python 3.7 thus it is recommened to use either `python3.6` or `python3.7`.

### Installation

#### Setting up Virtual Environment [Linux or Mac]

Clone this repo with:
```bash
git clone https://github.com/WilliamDavis22/SequentialYOLO
cd Sequential_YOLO/
```
Create Virtual **(Linux/Mac)** Environment:
```bash
python3 -m venv env
source env/bin/activate
```
Make sure that, from now on, you **run all commands from within your virtual environment**.

#### Setting up Virtual Environment [Windows]
Use the [Github Desktop GUI](https://desktop.github.com/) to clone this repo to your local machine. Navigate to the `SequentialYOLO` project folder and open a power shell window by pressing **Shift + Right Click** and selecting `Open PowerShell window here` in the drop-down menu.

Create Virtual **(Windows)** Environment:

```powershell
py -m venv env
.\env\Scripts\activate
```
![PowerShell](/Utils/Screenshots/PowerShell.png)
Make sure that, from now on, you **run all commands from within your virtual environment**.

#### Install Required Packages [Windows, Mac or Linux]
Install required packages (from within your virtual environment) via:

```bash
pip install -r requirements.txt
```
If this fails, you may have to upgrade your pip version first with `pip install pip --upgrade`.

## Full Start (Training and Inference)

Please follow the instructions detailed in README files located in the following sections:
- [`Image_Annotation`](/Image_Annotation/),
- [`Training`](/Training/) and
- [`Inference`](/Inference/).
 
**To make everything run smoothly it is highly recommended to keep the original folder structure of this repo!**

Each `*.py` script has various command line options that help tweak performance and change things such as input and output directories. All scripts are initialized with good default values that help accomplish all tasks as long as the original folder structure is preserved. To learn more about available command line options of a python script `<script_name.py>` run:

```bash
python <script_name.py> -h
```
### **NEW:** Weights and Biases
SequentialYOLO supports [Weights & Biases](https://wandb.ai/home/) to track your experiments online. Sign up at [wandb.ai](https://wandb.ai/home) to get an API key and run:
```bash
wandb -login <API_KEY>
```
where `<API_KEY>` is your Weights & Biases API key. 

### Multi-Stream-Multi-Model-Multi-GPU
If you want to run multiple streams in parallel, head over to [github.com/bertelschmitt/multistreamYOLO](https://github.com/bertelschmitt/multistreamYOLO). Thanks to @bertelschmitt for putting the work into this.

## License

Unless explicitly stated otherwise at the top of a file, all code is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This repo makes use of [**ilmonteux/logohunter**](https://github.com/ilmonteux/logohunter) which itself is inspired by [**qqwweee/keras-yolo3**](https://github.com/qqwweee/keras-yolo3).

## Troubleshooting

0. If you encounter any error, please make sure you follow the instructions **exactly** (word by word). Once you are familiar with the code, you're welcome to modify it as needed but in order to minimize error, I encourage you to not deviate from the instructions above. If you would like to file an issue, please use the provided template and make sure to fill out all fields. 

1. If you encounter a `FileNotFoundError`, `Module not found` or similar error, make sure that you did not change the folder structure. Your directory structure **must** look exactly like this: 
    ```text
    SequentialYOLO
    └─── Image_Annotation
    └─── Training
    └─── Inference
    └─── Data
    └─── Utils
    ```
    If you use a different name such as e.g. `SequentialYOLO-master` you will have to specify the correct paths as command line arguments in every function call.

    Don't use spaces in file or folder names, i.e. instead of `my folder` use `my_folder`.

2. If you are a Linux user and having trouble installing `*.snap` package files try:
    ```bash
    snap install --dangerous vott-2.1.0-linux.snap
    ```
    See [Snap Tutorial](https://tutorials.ubuntu.com/tutorial/advanced-snap-usage#2) for more information.

## Need more help? File an Issue!
If you would like to file an issue, please use the provided issue template and make sure to complete all fields. This makes it easier to reproduce the issue for someone trying to help you. 

## Stay Up-to-Date

- ⭐ **star** this repo to get notifications on future improvements and
- 🍴 **fork** this repo if you like to use it as part of your own project.


## Licensing 
This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by]. This means that you are free to:

 * **Share** — copy and redistribute the material in any medium or format
 * **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:

 * **Attribution** 
 
Thanks to:

AntonMu
	His github repo located at https://github.com/AntonMu/TrainYourOwnYOLO heavily influenced my work and this github repo and most of the credit should be given to him. The majority of my own work came in the form of collecting POV videos and rewriting scripts from him and qqwwee so the network was presented with sequential frames in batches instead of the industry standard of heavily randomized work
 
If you would like to cite this repo:
  ```text
  @misc{SequentialYOLO,
    title={Training a YOLOv3 With Sequential Frames: Building a Custom Object Detector from POV videos},
    author={William Davis},
    year={2020},
    url={https://github.com/WilliamDavis22/SequentialYOLO}
  }
  ```
If your work doesn't include a citation list, simply link this [github repo](https://github.com/WilliamDavis22/SequentialYOLO)!
 
[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

