function EventTimeline({ events }) {

    if (!events || events.length === 0) {
        return <p>Loading historical events...</p>;
    }

    return (

        <section className="timeline-section">

            <h2>Major Oil Market Events</h2>

            <div className="timeline">

                {events.map((event) => (

                    <div
                        key={event.event_id}
                        className="event-card"
                    >

                        <div className="event-header">

                            <h3>{event.event_name}</h3>

                            <span className="event-date">
                                {event.start_date}
                            </span>

                        </div>

                        <p>
                            <strong>Category:</strong> {event.category}
                        </p>

                        <p>
                            {event.description}
                        </p>

                        <p>

                            <strong>Expected Market Impact:</strong>

                            {" "}

                            <span className="impact">

                                {event.expected_direction}

                            </span>

                        </p>

                    </div>

                ))}

            </div>

        </section>

    );

}

export default EventTimeline;