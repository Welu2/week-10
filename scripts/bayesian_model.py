"""
Bayesian Change Point Detection Module

This module implements Bayesian change point detection for Brent oil prices
using PyMC.

Author: Your Name
"""

import numpy as np
import pandas as pd
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import arviz_plots as azp


class BayesianChangePointModel:
    """
    Bayesian Change Point Model for detecting one structural break
    in a time series.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : pandas Series or numpy array
            Time series data.
        """

        self.data = np.asarray(data)
        self.n = len(self.data)

        self.model = None
        self.trace = None

    # -------------------------------------------------------
    # Build Model
    # -------------------------------------------------------

    def build_model(self):
        """
        Construct Bayesian Change Point Model.
        """

        with pm.Model() as model:

            # Prior for switch point
            tau = pm.DiscreteUniform(
                "tau",
                lower=0,
                upper=self.n - 1
            )

            # Means before and after
            mu1 = pm.Normal(
                "mu1",
                mu=np.mean(self.data),
                sigma=np.std(self.data) * 2
            )

            mu2 = pm.Normal(
                "mu2",
                mu=np.mean(self.data),
                sigma=np.std(self.data) * 2
            )

            # Shared standard deviation
            sigma = pm.HalfNormal(
                "sigma",
                sigma=np.std(self.data)
            )

            idx = np.arange(self.n)

            mean = pm.math.switch(
                idx < tau,
                mu1,
                mu2
            )

            pm.Normal(
                "obs",
                mu=mean,
                sigma=sigma,
                observed=self.data
            )

        self.model = model

        return model

    # -------------------------------------------------------
    # Sampling
    # -------------------------------------------------------

    def sample(
        self,
        draws=2000,
        tune=1000,
        chains=4,
        target_accept=0.95,
        random_seed=42
    ):
        """
        Run MCMC sampling.
        """

        if self.model is None:
            self.build_model()

        with self.model:

            self.trace = pm.sample(
                draws=draws,
                tune=tune,
                chains=chains,
                target_accept=target_accept,
                random_seed=random_seed,
                return_inferencedata=True
            )

        return self.trace

    # -------------------------------------------------------
    # Summary
    # -------------------------------------------------------

    def summary(self):

        if self.trace is None:
            raise ValueError("Run sample() first.")

        return az.summary(self.trace)

    # -------------------------------------------------------
    # Trace Plot
    # -------------------------------------------------------

    def plot_trace(self):

        if self.trace is None:
            raise ValueError("Run sample() first.")

        az.plot_trace(self.trace)

        plt.tight_layout()

        plt.show()

    # -------------------------------------------------------
    # Posterior Plot
    # -------------------------------------------------------

    def plot_posterior(self):
        if self.trace is None:
            raise ValueError("Run sample() first.")

        # Change plot_posterior to plot_dist
        plot_obj = azp.plot_dist(
            self.trace,
            var_names=["tau", "mu1", "mu2", "sigma"]
        )

        plt.show()
        return plot_obj



    # -------------------------------------------------------
    # Extract Change Point
    # -------------------------------------------------------

    def get_change_point(self):
        """
        Return posterior mean of tau.
        """

        tau = (
            self.trace
            .posterior["tau"]
            .values
            .flatten()
        )

        return int(np.mean(tau))

    # -------------------------------------------------------
    # Extract Parameters
    # -------------------------------------------------------

    def get_parameters(self):

        posterior = self.trace.posterior

        return {
            "tau": int(
                posterior["tau"].values.mean()
            ),
            "mu1": float(
                posterior["mu1"].values.mean()
            ),
            "mu2": float(
                posterior["mu2"].values.mean()
            ),
            "sigma": float(
                posterior["sigma"].values.mean()
            )
        }

    # -------------------------------------------------------
    # Percentage Change
    # -------------------------------------------------------

    def percent_change(self):

        params = self.get_parameters()

        before = params["mu1"]

        after = params["mu2"]

        return ((after - before) / before) * 100

    # -------------------------------------------------------
    # Print Report
    # -------------------------------------------------------

    def report(self):

        params = self.get_parameters()

        print("=" * 50)

        print("Bayesian Change Point Report")

        print("=" * 50)

        print(f"Change Point Index : {params['tau']}")

        print(f"Mean Before        : {params['mu1']:.2f}")

        print(f"Mean After         : {params['mu2']:.2f}")

        print(f"Std Dev            : {params['sigma']:.2f}")

        print(
            f"Percentage Change  : "
            f"{self.percent_change():.2f}%"
        )

        print("=" * 50)