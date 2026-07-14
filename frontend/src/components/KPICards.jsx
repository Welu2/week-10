function KPICards({ metrics }) {
    if (!metrics || Object.keys(metrics).length === 0) {
        return <p>Loading dashboard metrics...</p>;
    }

    const cards = [
        {
            title: "Average Price",
            value: `$${metrics.average_price}`
        },
        {
            title: "Maximum Price",
            value: `$${metrics.maximum_price}`
        },
        {
            title: "Minimum Price",
            value: `$${metrics.minimum_price}`
        },
        {
            title: "Volatility",
            value: metrics.volatility
        },
        {
            title: "Observations",
            value: metrics.observations
        }
    ];

    return (
        <section className="kpi-section">

            <h2>Dashboard Summary</h2>

            <div className="kpi-grid">

                {cards.map((card, index) => (
                    <div
                        className="kpi-card"
                        key={index}
                    >
                        <h3>{card.title}</h3>

                        <p>{card.value}</p>

                    </div>
                ))}

            </div>

        </section>
    );
}

export default KPICards;