import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ReferenceLine,
    Legend
} from "recharts";

function PriceChart({ prices, events }) {

    if (!prices || prices.length === 0) {
        return <p>Loading price data...</p>;
    }

    return (

        <section className="chart-section">

            <h2>Historical Brent Oil Prices</h2>

            <ResponsiveContainer
                width="100%"
                height={500}
            >

                <LineChart
                    data={prices}
                    margin={{
                        top: 20,
                        right: 30,
                        left: 20,
                        bottom: 20
                    }}
                >

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis
                        dataKey="Date"
                        tick={{ fontSize: 12 }}
                        minTickGap={50}
                    />

                    <YAxis />

                    <Tooltip />

                    <Legend />

                    <Line
                        type="monotone"
                        dataKey="Price"
                        stroke="#1976d2"
                        strokeWidth={2}
                        dot={false}
                        name="Brent Price"
                    />

                    {
                        events.map((event) => (

                            <ReferenceLine
                                key={event.event_id}
                                x={event.start_date}
                                stroke="#ef5350"
                                strokeDasharray="4 4"
                                label={{
                                    value: event.event_name,
                                    angle: -90,
                                    position: "insideTop",
                                    fontSize: 10
                                }}
                            />

                        ))
                    }

                </LineChart>

            </ResponsiveContainer>

        </section>

    );

}

export default PriceChart;