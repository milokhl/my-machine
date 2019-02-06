# Ubuntu Setup
Setup for my Ubuntu environment.

Dell XPS 156 4K Ultra HD TouchScreen Laptop Intel Core i7 16GB Memory NVIDIA GeForce GTX 1050 512GB SSD Silver

## Sublime Text 3
Copy stuff from ```sublime/``` into ```~/.config/sublime-text-3/Packages/User/```


## Indicator Multiload

https://askubuntu.com/questions/406204/how-can-i-add-the-current-cpu-usage-to-my-menu-bar-as-a-percentage

```bash
sudo add-apt-repository ppa:indicator-multiload/stable-daily 
sudo apt-get update 
sudo apt-get install indicator-multiload
```

## Git Setup
```bash
git config --global user.name "Milo Knowles"
git config --global user.email "mknowles@mit.edu"
git config --global push.default simple
```

## Apt Packages
```bash
sudo apt install git
```

## Terminator
Solarized dark color, infinite scrollback.
```bash
cp terminal/terminator-config ~/.config/terminator/config
```

## NVIDIA Drivers
```bash
sudo nano /etc/default/grub # Add stuff to blacklist nouveau...

# If stuck in endless login loop, do this.
sudo apt-get remove nvidia-*
sudo apt-get autoremove
sudo nvidia-uninstall # If anything was installed using a runfile.

## 1: NVIDIA Drivers
# Link: https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html

# Stop lightdm. This caused all kinds of weird problems...
sudo service lightdm stop

# Installed drivers this way instead of with runfile.
sudo ubuntu-drivers list
sudo ubuntu-drivers autoinstall

# Restart lightdm. Should flash back to login screen.
sudo service lightdm restart

## 2: CUDA install.
sudo dpkg -i cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

# Update environment variables for CUDA.
export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64\
                       ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

## 3: Install cuDNN7 (developer version has samples).
# Link: https://developer.nvidia.com/rdp/cudnn-download
sudo dpkg -i libcudnn7-dev_7.0.3.11-1+cuda9.0_amd64.deb
```

## Tensorflow from Source
I had to do some extra stuff to use CUDA10, cuDNN7.3 with Tensorflow 1.12

```bash
# Install Bazel 0.15.0
# Don't install APT repository to make sure you get correct version.
# Find 0.15.0 at https://github.com/bazelbuild/bazel/releases

sudo apt-get install pkg-config zip g++ zlib1g-dev unzip python
chmod +x bazel-0.15.0-installer-linux-x86_64.sh
./bazel-0.15.0-installer-linux-x86_64.sh --user
export PATH="$PATH:$HOME/bin" # Add to .bashrc

# Install Tensorflow.
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow

# Use release 1.10: https://github.com/tensorflow/tensorflow/issues/23200
git checkout r1.10 # Checkout desired release.

# This took a long time.
# It should be fine to skip it.
bazel test -c opt -- //tensorflow/... -//tensorflow/compiler/... -//tensorflow/contrib/lite/...

# Make sure the cuDNN libraries are copied into the cuda install dir.
# Installing cuDNN with dpkg -i put them in a weird directory.
sudo cp /usr/lib/x86_64-linux-gnu/libcudnn.so.7 /usr/local/cuda/lib64/

# Configure: make sure you're in virtualenv to use the right python executable.
# Most options were set to 'no' except for CUDA and cuDNN.
# Do you want to use clang as CUDA compiler? [y/N]: n
./configure

# This builds an executable to build the wheel.
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package

# This build the wheel.
./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

# Install with pip (make sure you're in virtualenv).
pip install /tmp/tensorflow_pkg/tensorflow-1.10.1-cp35-cp35m-linux_x86_64.whl
```

Check for GPU support in Python:
```python
import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
```

# Useful commands
```bash
# Delete all OpenCV4 libraries in current directory
find . -name 'libopencv*.4.0*' -print0 | xargs -0 rm -rf
```

# Where is stuff?
```bash
# Cmake package config stuff
/usr/local/lib/cmake/
```
