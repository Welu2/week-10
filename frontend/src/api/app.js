import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:5000/api",
    headers: {
        "Content-Type": "application/json",
    },
});

export const getPrices = () => api.get("/prices");

export const getEvents = () => api.get("/events");

export const getKPIs = (start = null, end = null) => {

    if (start && end) {
        return api.get(`/kpis?start=${start}&end=${end}`);
    }

    return api.get("/kpis");
};

export const getChangePoints = () => api.get("/change-points");

export const getPriceRange = (start, end) =>
    api.get(`/price-range?start=${start}&end=${end}`);

export default api;