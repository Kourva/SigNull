<p align="center" >
    <img align="center" src="https://user-images.githubusercontent.com/118578799/222961586-6208d079-0ed0-439d-9e4f-8eb3311aee8d.png" />
    <h1 align="center"> SigNull XxX </h1>
    <p align="center"><b> Simple "Social media Template" app for android made in Python (Kivy) </b><p>
</p>

#### features
+ MultiScreen
+ Simple & Beautiful
+ Main menu
+ Console menu
+ Notification menu
+ Profile menu
+ Profile edit menu

# Setup
+ clone
```bash
git clone https://github.com/kozyol/SigNull & cd SigNull
```
+ requirements
```bash
chmod +x Lib/install.sh && ./Lib/install.sh
```
+ run
```bash
python3 main.py
```

<p align="center">
    <img align="center" src="https://user-images.githubusercontent.com/118578799/219371927-2ebe765b-cdef-4b61-94d5-abd2b63d56f9.png" width=90 height=90 />
    <h1 align="center"> Kivy to APK </h1>
    <p align="center"><b> Convert your Kivy file into apk </b></p>
</p>

###### You have 2 ways to do this. first way is [Google Colab](https://colab.research.google.com/). you can convert your Kivy file into APK fast and easy.
###### Second way is manual way. you need to do following stuff step by step
+ install required python libraries
```bash
pip install buildozer cython kivy pillow plyer
```
+ install required developer packages
```bash
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
```
+ install required plugins
```bash
sudo apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good
```
+ install required packages
```bash
sudo apt-get install -y \
    build-essential \
    libsqlite3-dev \
    sqlite3 \
    bzip2 \
    libbz2-dev \
    zlib1g-dev \
    libssl-dev \
    openssl \
    libgdbm-dev \
    libgdbm-compat-dev \
    liblzma-dev \
    libreadline-dev \
    libncursesw5-dev \
    libffi-dev \
    uuid-dev \
    libffi6
```
+ install this package
```bash
sudo apt-get install libffi-dev
```
+ init buildozer file (If you don't have **buildozer.spec** file. otherwise skip this step)
```bash
buildozer init
```
+ build the app
```bash
buildozer -v android debug
```
+ if you get any error, clear the data and rebuild again
```bash
buildozer android clean
```


# Thanks
###### You can give me a star if you find this tool helpfull. Wishing you all the best.
