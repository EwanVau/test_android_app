# test_android_app

Testing different apps created using the kivy framework

## Files:
...

# Pushing to an Android App

Use the following steps on an ubunutu virtual machine (buildozer does not work on windows machines):
```console
user@user_name:~$ sudo apt install git
```

```console
user@user_name:~$ git clone https://github.com/kivy/buildozer.git
```

```console
user@user_name:~$ cd buildozer
```

```console
user@user_name:~/buildozer$ sudo apt-get install python3.6
```
Note: python3.6 is used and not later versions for compatiability issues

```console
user@user_name:~/buildozer$ sudo apt-get install -y python3-setuptools
```

```console
user@user_name:~/buildozer$ sudo python3 setup.py install
```

```console
user@user_name:~/buildozer$ cd ..
```

```console
user@user_name:~$ git clone https://github.com/EwanVau/test_android_app.git
```

```console
user@user_name:~$ cd test_android_app/app
```

```console
user@user_name:~/test_android_app/app$ buildozer init
```

```console
user@user_name:~/test_android_app/app$ sudo apt update
```

```console
user@user_name:~/test_android_app/app$ sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev
```

Note: refer to [this](https://buildozer.readthedocs.io/en/latest/installation.html#android-on-ubuntu-20-04-64bit) for the dependencies needed
```console
user@user_name:~/test_android_app/app$ pip3 install --user --upgrade cython virtualenv
```

Note: `--user` is not needed if using virtualenv
```console
user@user_name:~/test_android_app/app$ sudo apt-get install cython
```

```console
user@user_name:~/test_android_app/app$ buildozer android debug deploy run
```







