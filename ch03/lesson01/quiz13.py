#!/usr/bin/env python

# Solution is available in the other "solution.py" tab
import tensorflow as tf

def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)
    
    # Calculate the softmax of the logits
    softmax = tf.nn.softmax(logit_data)    
    
    with tf.Session() as sess:
        # Feed in the logit data
        output = sess.run(softmax, feed_dict={logits: logit_data})

    return output

print(run())
