import multiprocessing as threading
import multiprocessing as queue
import SceneDesc
import sys
import warnings
from keras.callbacks import ModelCheckpoint
warnings.filterwarnings("ignore")

def train(epoch):
    sd = SceneDesc.scenedesc()
    model = sd.create_model()
    batch_size = 512
    model.load_weights('Output/Weights.h5')
    #weight_save_callback = ModelCheckpoint('Output/Weights.{epoch:02d}-{val_acc:.2f}.hdf5', monitor='val_loss', verbose=1, save_best_only=False, mode='auto')
    model.fit_generator(sd.data_process(batch_size=batch_size), steps_per_epoch=sd.no_samples/batch_size, epochs=epoch, verbose=1, callbacks=None,  workers=4, use_multiprocessing=True)
    #model.fit_generator(sd.data_process(batch_size=batch_size), steps_per_epoch=sd.no_samples/batch_size, epochs=epoch, initial_epoch=0, verbose=1, callbacks=[weight_save_callback])
    model.save('Output/Model.h5', overwrite=True)
    model.save_weights('Output/Weights.h5',overwrite=True)
 
if __name__=="__main__":
    train(int(sys.argv[1]))
