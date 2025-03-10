import axios from 'axios';
import { Vehicle } from './types';

const API_BASE_URL = 'http://localhost:8000/api';

export const getVehicles = async (): Promise<Vehicle[]> => {
    const response = await axios.get(`${API_BASE_URL}/vehicles`);
    return response.data;
};
