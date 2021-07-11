def sgd_model_try(X_train_tensor,y_train_tensor,model_layer1):
    net = NeuralNet(
        module = model_layer1,
        criterion = torch.nn.BCELoss,
        #max_epochs=20,
        #module__dropout=0.5,
        optimizer=torch.optim.SGD,
        device='cuda',  # uncomment this to train with CUDA
    )
    parameters = [{'lr': [0.1, 0.01],
                   'optimizer__momentum':[0,0.5],
                   'optimizer__weight_decay': [0.0001],
                   #'module__dropout': [0.4, 0.5],
                   'max_epochs':[20]
                }]
    scoring = {'AUC': 'roc_auc', 'f1': make_scorer(f1_score)}
    grid_search = GridSearchCV(
                                estimator=net,
                                param_grid=parameters,
                                scoring=scoring,
                                refit='AUC',
                                return_train_score=True,
                                cv=5,
                                n_jobs=-1
                               )
    grid_search.fit(X_train_tensor,y_train_tensor)
    return grid_search

class OneLayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        """
        In the constructor we instantiate two nn.Linear modules and assign them as
        member variables.
        """
        super(OneLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        """
        In the forward function we accept a Tensor of input data and we must return
        a Tensor of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Tensors.
        """
        x = F.relu(self.linear1(x))
        x = F.sigmoid(self.linear2(x))
        return x


def create_model(newdataset):
    optimizer = ['sgd', 'adagrad']
    H = [10000, 5000, 3500, 2500, 2000, 1500, 1250, 1000, 750, 500, 250, 100, 50, 25, 10]
    D_in, H, D_out = 31, 1000, 1
    model_layer1 = OneLayerNet(D_in, H, D_out)

    X = newdataset.iloc[:, :-1]
    y = newdataset.iloc[:, -1:]
    #     X_validation = validation_dataset.iloc[:,:-1]
    #     y_validation = validation_dataset.iloc[:,-1:]
    X_train_tensor = torch.tensor(X.values.astype(np.float32))
    y_train_tensor = torch.tensor(y.values.astype(np.float32)).squeeze(1)

    grid_search = sgd_model_try(X_train_tensor, y_train_tensor, model_layer1)
    print(grid_search.cv_results_)


create_model(newdataset)