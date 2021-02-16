import tensorflow as tf
import os

if __name__ == '__main__':
    model_path = "./models/my_model_10_feb"
    #if os.path.exists(model_path):
    os.chmod(model_path, 777)


    # model = tf.keras.models.load_model(model_path)
    with tf.Session() as sess:
        model = tf.compat.v1.saved_model.load(sess=sess,export_dir=model_path, tags=['serve'])

    print(help(model))