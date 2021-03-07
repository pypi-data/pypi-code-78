import numpy as np
from eloquentarduino.ml.data.preprocessing.pipeline.BaseStep import BaseStep
from sklearn.feature_selection import SelectKBest as KBest, chi2


class SelectKBest(BaseStep):
    """
    Implementation of sklearn.feature_selection.SelectKBest
    """
    def __init__(self, k, name='SelectKBest', score_func=chi2):
        """
        Constructor
        :param k: int k best features
        :param score_func: callable scoring function
        """
        assert isinstance(k, int) and k > 0, 'k MUST be positive'

        super().__init__(name)
        self.k = k
        self.kbest = KBest(k=k, score_func=score_func)
        self.inplace = True

    def fit(self, X, y):
        """
        Fit
        """
        self.set_X(X)
        self.kbest.fit(X, y)

        return self.transform(X), y

    def transform(self, X):
        """
        Transform
        """
        return self.kbest.transform(X)

    def get_template_data(self):
        """
        Template data
        """
        idx = (-self.kbest.scores_).argsort()[:self.k]
        idx = np.sort(idx)
        return {
            'k': self.k,
            'idx': idx
        }