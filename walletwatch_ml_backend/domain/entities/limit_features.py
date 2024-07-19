class LimitFeatures:
    def __init__(self, **kwargs):
        valid_features = {'total_income', 'total_installment',
                          'personality', 'last_month_limit'}
        for key, value in kwargs.items():
            if key in valid_features:
                setattr(self, key, value)
            else:
                raise ValueError(f'Invalid feature: {key}')
