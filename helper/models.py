#iseng doang ini

from sklearn import linear_model

SGDClass = {
    "sgdclass": linear_model.SGDClassifier(
        max_iter=800,
        loss='log_loss',
        random_state=241,
        learning_rate='adaptive'
    )
}