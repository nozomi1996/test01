fit = model.fit(
    X_train, y_train,    # training data
    batch_size=n_split,  # no mini-batches, see next lecture
    epochs= 3416,       # number of training epochs
    verbose=2,           # verbosity of shell output (0: none, 1: high, 2: low)
    validation_data=(X_valid, y_valid),  # validation data
    callbacks=[])        # optional list of functions to be called once per epoch
