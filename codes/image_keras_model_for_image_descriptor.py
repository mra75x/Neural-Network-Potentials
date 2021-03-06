
def model_paper():
  model = Sequential()

  model.add(Conv2D(input_shape=(256,256,1),filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1,padding="same", activation="relu"))
  model.add(Conv2D(filters=16,kernel_size=(4,4),strides= 1 ,padding="same", activation="relu"))

  model.add(Conv2D(filters=64,kernel_size=(3,3),strides=(2,2),padding="same", activation="relu"))

  model.add(Flatten())
  model.add(Dense(units=1024,activation="relu"))

  model.add(Dense(units = 1, activation="linear"))

  return model
