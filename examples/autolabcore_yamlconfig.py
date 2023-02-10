from autolab_core import YamlConfig

#YamlConfig
"""Class to load a configuration file and parse it into a dictionary.
    Attributes
    ----------
    config : :obj:`dictionary`
        A dictionary that contains the contents of the configuration.
    """
if __name__ == "__main__":
    config = YamlConfig("/home/arg/gqcnn/examples/../cfg/examples/gqcnn_pj.yaml")
    print(config.keys())
    print(config.get('policy'))
    print(config['policy']['num_seed_samples'])
    config['policy']['num_seed_samples'] = 100
    print(config['policy']['num_seed_samples'])
    config.save('policy.txt')
