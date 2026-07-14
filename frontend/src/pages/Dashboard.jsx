import { useEffect, useState } from "react";

import {
    getPrices,
    getEvents,
    getKPIs,
    getChangePoints,
    getPriceRange,
} from "../api/app";

import PriceChart from "../components/PriceChart";
import KPICards from "../components/KPICards";
import Filters from "../components/Filters";
import EventTimeline from "../components/EventTimeline";
import ChangePointTable from "../components/ChangePointTable";

function Dashboard() {
    const [prices, setPrices] = useState([]);
    const [events, setEvents] = useState([]);
    const [kpis, setKPIs] = useState({});
    const [changePoints, setChangePoints] = useState({});
    
    // FIX 1: Declared the missing filters state variable here
    const [filters, setFilters] = useState({ start: null, end: null });

    useEffect(() => {
        loadDashboard();
    }, []);

    const handleFilter = async (start, end) => {
        // FIX 2: Save the user's selected dates to state when filtering
        setFilters({ start, end });

        if (!start || !end) {
            const prices = await getPrices();
            const kpis = await getKPIs();

            setPrices(prices.data);
            setKPIs(kpis.data);
            return;
        }

        const prices = await getPriceRange(start, end);
        const kpis = await getKPIs(start, end);

        setPrices(prices.data);
        setKPIs(kpis.data);
    };

    const loadDashboard = async () => {
        try {
            const priceResponse = await getPrices();
            const eventResponse = await getEvents();
            const kpiResponse = await getKPIs();
            const cpResponse = await getChangePoints();

            setPrices(priceResponse.data);
            setEvents(eventResponse.data);
            setKPIs(kpiResponse.data);
            setChangePoints(cpResponse.data);
        } catch (error) {
            console.error(error);
        }
    }; // <-- FIX 3: Closed loadDashboard function here securely!

    /* ========================================================= */
    /*  FIX 4: MOVED OUTSIDE OF LOADDASHBOARD                    */
    /*     This now sits correctly in the main component body    */
    /* ========================================================= */
    const filteredEvents = events.filter(event => {
        if (!filters.start || !filters.end) return true;
        
        return event.start_date >= filters.start && event.start_date <= filters.end;
    });

    return (
        <div className="dashboard">
            <header className="header">
                <h1>Brent Oil Price Dashboard</h1>
                <p>
                    Bayesian Change Point Analysis &
                    Historical Event Visualization
                </p>
            </header>

            <KPICards metrics={kpis} />

            <Filters onFilter={handleFilter} />

            <PriceChart
                prices={prices}
                events={events}
            />

            <EventTimeline
                events={filteredEvents}
            />

            <ChangePointTable
                changePoint={changePoints}
            />
        </div>
    );
}

export default Dashboard;
