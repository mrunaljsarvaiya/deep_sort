import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model


if __name__ == "__main__":
  img_size = (2048, 2048,3)
  res_model = tf.keras.applications.resnet.ResNet101(weights=None, include_top=False, input_shape=(img_size))
  res_model.load_weights("/home/peanut/Documents/deep_sort/custom_model/mask_rcnn_coco.h5",by_name=True)
  for layer in res_model.layers:
      layer.trainable = False
  new_model = Model(inputs=res_model.input, outputs=res_model.get_layer("conv5_block3_out").output)
  new_model.summary()
  import pdb; pdb.set_trace()