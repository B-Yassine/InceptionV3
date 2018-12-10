from __future__ import print_function

print("Verifying that the system setup is correct...")

try:
    import numpy as np

    print("numpy: OK")
except:
    print("Unable to import numpy.")
    print("You should install it with pip install numpy")
    exit(1)

try:
    import matplotlib.pyplot as plt

    print("matplotlib: OK")
except:
    print("Unable to import matplotlib.")
    print("You should install it with python -m pip install -U matplotlib")
    exit(1)

try:
    import os

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
except:
    # This just disables tensorflow obnoxious messages
    # it's okay if it fails
    pass

try:
    import tensorflow as tf

    print("tensorflow: OK")
except:
    print("Unable to import tensorflow.")
    print("You should install it with pip install tensorflow")
    exit(1)

if tf.__version__[0] != '1':
    print("You have tensorflow installed corretly, but an old version")
    print("You may want to uninstall and reinstall tensorflow.")

try:
    sess = tf.Session()
    if sess.run(tf.constant(3) + tf.constant(5)) != 8:
        print("Tensorflow is not able to do math.")
        print("This should never happen.")
        print("Try reinstalling tensorflow, or using a different version.")
        exit(1)
except:
    print("Unable instantiate a session object.")
    print("Try reinstalling tensorflow, or using a different version.")
    exit(1)

try:
    import keras
    print("keras: OK")
    has_keras = True
except:
    print("Unable to import keras.")
    print("You should install it with pip install keras")
    print("This is not strictly necessary, but will greatly improve performance.")
    has_keras = False

if has_keras:
    print("Everything is properly installed and set up, with keras.")
    print("You are good to go.")
else:
    print("Everything is properly installed and set up, but without keras.")
    print("You have to install it right now")
