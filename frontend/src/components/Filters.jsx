import { useState } from "react";

function Filters({ onFilter }) {
    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");

    const handleApply = () => {
        if (!startDate || !endDate) {
            alert("Please select both start and end dates.");
            return;
        }

        if (onFilter) {
            onFilter(startDate, endDate);
        }
    };

    const handleReset = () => {
        setStartDate("");
        setEndDate("");

        if (onFilter) {
            onFilter(null, null);
        }
    };

    return (
        <section className="filter-section">

            <h2>Filter Data</h2>

            <div className="filter-controls">

                <div className="filter-group">

                    <label>Start Date</label>

                    <input
                        type="date"
                        value={startDate}
                        onChange={(e) => setStartDate(e.target.value)}
                    />

                </div>

                <div className="filter-group">

                    <label>End Date</label>

                    <input
                        type="date"
                        value={endDate}
                        onChange={(e) => setEndDate(e.target.value)}
                    />

                </div>

                <button
                    className="btn-primary"
                    onClick={handleApply}
                >
                    Apply
                </button>

                <button
                    className="btn-secondary"
                    onClick={handleReset}
                >
                    Reset
                </button>

            </div>

        </section>
    );
}

export default Filters;