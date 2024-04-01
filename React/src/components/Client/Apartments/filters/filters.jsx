import React, { useEffect, useState, useContext } from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import ApartmentService from '../../../../services/ApartmentService';
import Form from 'react-bootstrap/Form';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';
import { grey } from '@mui/material/colors';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Button from 'react-bootstrap/esm/Button';
import { useApartments } from '../../../../hooks/useApartments';
import ApartmentContext from "../../../../context/ApartmentContext";

export default function Filters() {
        // const { apartments, setApartments } = useContext(ApartmentContext);
        const history = useHistory();
        const location = useLocation();
        const [AVCities, setAVCities] = useState([]);
        const [filters, setFilters] = useState({});
    
        useEffect(() => {
            const searchParams = new URLSearchParams(location.search);
            const queryParams = {};
            for (let [key, value] of searchParams) {
                queryParams[key] = value;
            }
            setFilters(queryParams);
        }, [location]);
    
        useEffect(() => {
            // Fetch available cities
            ApartmentService.getAvailableCities()
                .then(response => {
                    setAVCities(response.data);
                })
                .catch(error => {
                    console.error('Error fetching available cities:', error);
                });
        }, []);
    
        const handleChange = (e) => {
            setFilters(prevFilters => ({
                ...prevFilters,
                [e.target.name]: e.target.value || null,
            }));
        };
        
        const applyFilters = () => {
            const searchParams = new URLSearchParams();
            for (const key in filters) {
                searchParams.append(key, filters[key]);
            }
            history.push(`?${searchParams.toString()}`);
        };
        
        const clearFilters = () => {
            setFilters({});
            history.push('/');
        };
    
        return (
            <>
                <h5 style={{ marginLeft: '10px' }}>Filters</h5>
                <hr />
                <div style={{ display: 'flex', gap: '20px', margin: '10px', justifyContent: 'start', alignItems: 'center'}}>
                    <div>
                        <Form.Label>Rooms</Form.Label>
                        <Form.Select    
                            style={{ width: '170px' }} 
                            name='num_rooms'
                            value={filters.num_rooms || ""}
                            onChange={handleChange}
                        >
                            <option value="">Select number of rooms</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </Form.Select>
                    </div>
                    <div>
                        <Form.Label>Cities</Form.Label>
                        <Form.Select
                            name='city' 
                            value={filters.city || ""}
                            style={{ width: '170px' }}
                            onChange={handleChange}
                        >
                            <option value="">Select a city</option>
                            {AVCities.map(city => <option key={city.slug} value={city.slug}>{city.name}</option>)}
                        </Form.Select>
                    </div>
                    <div style={{marginTop: '30px'}}>
                        <Button variant="success" onClick={applyFilters}>Apply Filters</Button>            
                    </div>
                    <div style={{marginTop: '30px'}}>
                        <Button variant="warning" onClick={clearFilters}>Clear Filters</Button>            
                    </div>
                </div>
            </>
        );
    };
    
