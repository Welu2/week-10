import numpy as np

from scripts.bayesian_model import BayesianChangePointModel


def test_model_creation():
    """
    Test that the Bayesian model can be built.
    """

    np.random.seed(42)

    data = np.concatenate([
        np.random.normal(20, 1, 50),
        np.random.normal(40, 1, 50)
    ])

    model = BayesianChangePointModel(data)

    pymc_model = model.build_model()

    assert pymc_model is not None


def test_sampling_runs():
    """
    Test that MCMC sampling completes.
    """

    np.random.seed(42)

    data = np.concatenate([
        np.random.normal(10, 1, 40),
        np.random.normal(20, 1, 40)
    ])

    model = BayesianChangePointModel(data)

    model.build_model()

    trace = model.sample(
        draws=100,
        tune=100,
        chains=2,
        target_accept=0.9,
        random_seed=42
    )

    assert trace is not None


def test_parameter_extraction():
    """
    Test parameter extraction after sampling.
    """

    np.random.seed(42)

    data = np.concatenate([
        np.random.normal(5, 1, 40),
        np.random.normal(15, 1, 40)
    ])

    model = BayesianChangePointModel(data)

    model.build_model()

    model.sample(
        draws=100,
        tune=100,
        chains=2,
        target_accept=0.9,
        random_seed=42
    )

    params = model.get_parameters()

    assert "tau" in params
    assert "mu1" in params
    assert "mu2" in params
    assert "sigma" in params


def test_percent_change_returns_float():
    """
    Test that percent_change() returns a float.
    """

    np.random.seed(42)

    data = np.concatenate([
        np.random.normal(30, 1, 50),
        np.random.normal(60, 1, 50)
    ])

    model = BayesianChangePointModel(data)

    model.build_model()

    model.sample(
        draws=100,
        tune=100,
        chains=2,
        target_accept=0.9,
        random_seed=42
    )

    pct = model.percent_change()

    assert isinstance(pct, float)