function ChangePointTable({ changePoint }) {

    if (!changePoint || Object.keys(changePoint).length === 0) {
        return <p>Loading Bayesian analysis...</p>;
    }

    return (

        <section className="change-point-section">

            <h2>Bayesian Change Point Analysis</h2>

            <table className="cp-table">

                <thead>

                    <tr>
                        <th>Metric</th>
                        <th>Value</th>
                    </tr>

                </thead>

                <tbody>

                    <tr>
                        <td>Detected Change Point</td>
                        <td>{changePoint.change_point}</td>
                    </tr>

                    <tr>
                        <td>Mean Before Change (μ₁)</td>
                        <td>${changePoint.mu_before}</td>
                    </tr>

                    <tr>
                        <td>Mean After Change (μ₂)</td>
                        <td>${changePoint.mu_after}</td>
                    </tr>

                    <tr>
                        <td>Standard Deviation (σ)</td>
                        <td>{changePoint.sigma}</td>
                    </tr>

                    <tr>
                        <td>Percentage Change</td>
                        <td>{changePoint.percent_change}%</td>
                    </tr>

                </tbody>

            </table>

            <div className="interpretation-card">

                <h3>Interpretation</h3>

                <p>

                    The Bayesian model detected a structural break around

                    <strong> {changePoint.change_point}</strong>.

                </p>

                <p>

                    The average Brent crude oil price shifted from

                    <strong> ${changePoint.mu_before}</strong>

                    to

                    <strong> ${changePoint.mu_after}</strong>,

                    representing a

                    <strong> {changePoint.percent_change}%</strong>

                    increase.

                </p>

                <p>

                    This structural change may correspond to one or more
                    major geopolitical or economic events that altered
                    global oil market dynamics.

                </p>

            </div>

        </section>

    );

}

export default ChangePointTable;