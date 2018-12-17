from keras.models import load_model

#model = load_model('DeepCSV_model.h5')

#arch = model.to_json()
#with open('DeepCSV_arch.json', 'w') as arch_file:
#    arch_file.write(arch)

#model.save_weights('DeepCSV_weights.h5')


from models import dense_model
from DeepJetCore.training.training_base import training_base

from keras.layers import Dense, Dropout, Flatten, Convolution2D, merge, Convolution1D, Conv2D
from keras.models import Model, Sequential

#also does all the parsing
#train=training_base(testrun=False)
#print 'Inited'
#
#if not train.modelSet():
#    from models import sequential_model 
#    print 'Setting model'
#    train.setModel(sequential_model,dropoutRate=0.1)
#
#    train.compileModel(learningrate=0.003,
#                       loss='categorical_crossentropy',
#                       metrics=['accuracy'])
#

dropoutRate = 0.25
nclasses = 4

model = Sequential( [

     Dense(100, activation='relu',kernel_initializer='lecun_uniform', input_shape=(66,1)),
     Dropout(dropoutRate),
     Dense(100, activation='relu',kernel_initializer='lecun_uniform'),
     Dropout(dropoutRate),
     Dense(100, activation='relu',kernel_initializer='lecun_uniform'),
     Dropout(dropoutRate),
     Dense(100, activation='relu',kernel_initializer='lecun_uniform'),
     Dropout(dropoutRate),
     Dense(100, activation='relu',kernel_initializer='lecun_uniform'),
     Dense(nclasses, activation='softmax',kernel_initializer='lecun_uniform')
])

arch = model.to_json()
with open('DeepCSV_arch.json', 'w') as arch_file:
    arch_file.write(arch)


