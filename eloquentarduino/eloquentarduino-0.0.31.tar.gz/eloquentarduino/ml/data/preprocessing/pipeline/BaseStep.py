from eloquentarduino.utils import jinja


class BaseStep:
    """
    Base class for the pipeline steps
    """
    def __init__(self, name):
        self.name = name
        self.input_dim = None
        self.inplace = False
        self.working_dim = 0

    def set_X(self, X):
        """
        Update input dim
        :param X:
        """
        self.input_dim = X.shape[1]

    def fit(self, X, y):
        """
    Fit step to input
        """
        raise NotImplemented

    def transform(self, X):
        """
        Transform input
        """
        raise NotImplemented

    def get_template_data(self):
        """
        Get data for jinja template
        :return: dict
        """
        raise NotImplemented('get_template_data')

    def port(self, pipeline):
        """
        Port to plain C++
        :param pipeline: str pipeline name
        :return: str C++ code
        """
        template_name = type(self).__name__
        template_data = self.get_template_data()
        template_data.update(name=self.name, input_dim=self.input_dim, pipeline=pipeline)

        return jinja('ml/data/preprocessing/pipeline/%s.jinja' % template_name, template_data)
