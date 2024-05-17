import api from './api';

const CitiesService = {

    getAllApartments() {
        return api().get('/apartments');
    },
    getOneApartment(slug) {
        return api().get(`apartments/${slug}`);
    },
    createApartment(data) {
        return api().post('apartments/', data);
    },
    updateApartment(slug, data) {
        return api().put(`apartments/${slug}`, data);
    },
    deleteApartment(slug) {
        return api().delete(`apartments/${slug}`);
    },
    getApartmentsByZone(slug) {
        return api().get(`apartments/zone/${slug}`)
    },
    getOneApartmentById(id) {
        return api().get(`apartment_id/${id}`)
    },
    getAvailableCities() {
        return api().get(`apartments/av_cities/`)
    },

    sendFiltersApartments(filters) {
        return api().post(`apartments/filters/`, filters)
    }
};
export default CitiesService;