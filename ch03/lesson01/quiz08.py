#!/usr/bin/env python

# Solution is available in the other "solution.py" tab
import tensorflow as tf

# Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.divide(x, y), 1)

# Print z from a session
output = None
with tf.Session() as sess:
    output = sess.run(z)
print('z: {}', output)
