class PersonalityFeatures:
    def __init__(self, **kwargs):
        valid_features = {f'f{i:02d}' for i in range(1, 37)}
        for key, value in kwargs.items():
            if key in valid_features:
                if 1 <= value <= 5:
                    setattr(self, key, value)
                else:
                    raise ValueError(
                        f'Invalid value for {key}: {value}. Must be within the range 1 to 5.')
            else:
                raise ValueError(f'Invalid feature: {key}')
